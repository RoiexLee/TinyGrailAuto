import argparse
import logging

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class API(object):
    URL = "https://tinygrail.com/api"
    BONUS_URL = URL + "/event/scratch/bonus2"

    def __init__(self, cookie):
        self.headers = {
            "Cookie": cookie
        }

    def get_bonus2(self):
        res = requests.get(self.BONUS_URL, headers=self.headers)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception(e)
        res = res.json()
        if res["State"] == 0:
            return res["Value"]
        else:
            raise Exception(res["Message"])

    def start(self):
        for _ in range(3):
            logger.info(self.get_bonus2())


parser = argparse.ArgumentParser()
parser.add_argument("--cookies", type=str, required=True, help="Cookies")
args = parser.parse_args()

if __name__ == '__main__':
    cookies = args.cookies.split("&")
    if len(cookies) == 0:
        raise Exception("no cookies")
    else:
        for cookie in cookies:
            API(cookie).start()
