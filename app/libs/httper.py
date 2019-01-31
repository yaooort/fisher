"""
Created by Oort on 2018/12/6 2:51 PM.
"""

__author__ = 'Oort'

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url, headers={'Connection': 'close'})
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
