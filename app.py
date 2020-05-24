import json
from dataclasses import asdict
from http import HTTPStatus

from chalice import Chalice, Response

from chalicelib.alias import RandomAliasGenerator
from chalicelib.config import Config
from chalicelib.db import DDBClient
from chalicelib.items import Registration, Alias
from chalicelib.validation import is_valid_registration

app = Chalice(app_name='quark')

generator = RandomAliasGenerator()
db_client = DDBClient()


@app.route('/check', methods=['GET'], cors=True)
def _ping():
    return Response(body="Ok", status_code=HTTPStatus.OK)


@app.route('/register', methods=['POST'], cors=True)
def _register():
    alias_retry = Config.alias_retry()
    alias_length = Config.alias_length()
    registration = Registration(**app.current_request.json_body)
    if not is_valid_registration(registration):
        return Response(body=json.dumps({'alias': None}), status_code=HTTPStatus.BAD_REQUEST)

    item = Alias(alias=generator.generate_alias(alias_length), link=registration.link)
    cnt = 0
    while not db_client.put_new_redirect(item) and cnt < alias_retry:
        app.log.warning("Collision on %s", item.alias)
        item = Alias(alias=generator.generate_alias(alias_length), link=registration.link)
        cnt += 1

    if cnt >= alias_retry:
        app.log.error("No valid aliases found")
        return Response(body=json.dumps({'alias': None}), status_code=HTTPStatus.INSUFFICIENT_STORAGE)

    return Response(body=json.dumps(asdict(item)), status_code=HTTPStatus.OK)


@app.route('/{alias}', methods=['GET'], cors=True)
def _redirect(alias):
    item = db_client.get_redirect(alias=alias)
    return redirect_response(item.link) if item else redirect_response('/404')


def redirect_response(location):
    return Response(
        '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
        "<title>Redirecting...</title>\n"
        "<h1>Redirecting...</h1>\n"
        "<p>You should be redirected automatically to target URL: "
        '<a href="%s">%s</a>.  If not click the link.'
        % (location, location),
        status_code=HTTPStatus.TEMPORARY_REDIRECT,
        headers={
            'mimetype': 'text/html',
            'Location': location
        }
    )
