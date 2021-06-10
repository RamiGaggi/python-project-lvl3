#!/usr/bin/env python

"""Main script."""

import logging
import sys

from page_loader.download_engine import KnownError, download
from page_loader.parsers import create_arg_parser


def main():
    """Run the programm."""  # noqa: DAR401
    args = create_arg_parser()
    url = args.url
    output_path = args.output
    numeric_level_log = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level_log, int):
        raise ValueError('Invalid log level: %s' % numeric_level_log)

    logging.basicConfig(
        format='%(message)s',
        level=numeric_level_log,
    )

    logging.info("Downloading page: '%s'", url)
    try:
        res_path = download(url, output_path)
    except KnownError:
        sys.exit(1)

    if res_path == 'ERROR':
        logging.error("Page wasn't successfully downloaded")
    else:
        logging.info("Page was successfully downloaded into '%s'", res_path)


if __name__ == '__main__':
    main()
