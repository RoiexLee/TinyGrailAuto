import os

import requests


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
            self.get_bonus2()


if __name__ == '__main__':
    cookies = os.environ.get("COOKIES", "").split("&")
    if len(cookies) == 0:
        raise Exception("no cookies")
    else:
        for cookie in cookies:
            API(cookie).start()
