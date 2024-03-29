from urllib.parse import urlparse, ParseResult

from chalicelib.items import Registration

_ACCEPTED_SCHEMES = {'http', 'https', 'file', 's3'}


def has_valid_host(url_parts: ParseResult) -> bool:
    return url_parts.hostname and url_parts.hostname != "localhost"


def is_valid_protocol(url_parts: ParseResult):
    return not url_parts.scheme or url_parts.scheme in _ACCEPTED_SCHEMES


def is_valid_registration(registration: Registration) -> bool:
    url_parts = urlparse(registration.link)
    return all([
        has_valid_host(url_parts),
        is_valid_protocol(url_parts)
    ])
