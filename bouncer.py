import os
import time
import logging
import requests


logger = logging.getLogger(__name__)


def main():
    urls = os.environ.get('URLS', None)
    interval = os.environ.get('INTERVAL', 55)

    if not urls:
        return

    urls = urls.split(",")

    for url in urls:
        logger.info('Hittingg %s' % url)
        requests.get(url)

    time.sleep(interval * 60)
    main()


if __name__ == '__main__':
    main()
