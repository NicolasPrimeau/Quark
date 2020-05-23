from argparse import ArgumentParser

import requests

DEFAULT_HOST = "https://9jsmzaxdn9.execute-api.us-east-1.amazonaws.com/api"


def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--host", dest="host", help="Host", required=False, default=DEFAULT_HOST, type=str)
    parser.add_argument("-l", "--link", dest="link", help="Link", required=True, type=str)
    args = parser.parse_args()
    host, link = args.host, args.link
    result = requests.post(f"{host}/register", json={"link": link})
    print(f"{host}/l/{result.json()['alias']}")


if __name__ == '__main__':
    main()
