from aiohttp import web
from configargparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import logging

from aiomisc.log import basic_config


def parse_args():
    parser = ArgumentParser(auto_env_var_prefix="FILE_MANAGER", formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("--api-address", default="0.0.0.0", help="IPV4 address on which API server would listen")
    parser.add_argument("--api-port", default="8081", help="API server port")

    return parser.parse_args()


def main():
    args = parse_args()
    basic_config(logging.DEBUG, buffered=True)

    app = web.Application()
    web.run_app(app, host=args.api_address, port=args.api_port)


if __name__ == "__main__":
    main()
