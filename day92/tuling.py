# -*- coding: utf-8 -*-
# __author__ = "maple"


tl_url = "http://openapi.tuling123.com/openapi/api/v2"

import requests

tl_data = {
    "perception": {
        "inputText": {
            "text": "北京今天天气怎么样"
        }
    },
    "userInfo": {
        "apiKey": "51ff3d2dd9464ba6bba97ff1bb9427ab",
        "userId": "123456789123"
    }
}

res = requests.post(tl_url,json=tl_data)

res_json = res.json()
print(res_json.get("results")[0].get("values").get("text"))