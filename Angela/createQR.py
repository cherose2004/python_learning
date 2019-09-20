import os

import requests
from Config import LT_URL, QRCODE_PATH, MongoDB
from uuid import uuid4
import time,hashlib
#创建 二维码 设备编号字符串

def create_qr(count):
    device_list = []
    for i in range(count):
        DeviceKey = hashlib.md5(f"{uuid4()}{time.time()}{uuid4()}".encode("utf8")).hexdigest()
        res = requests.get(LT_URL%(DeviceKey))
        qr_name = f"{DeviceKey}.jpg"
        qr_file_path = os.path.join(QRCODE_PATH,qr_name)
        with open(qr_file_path,"wb") as f:
            f.write(res.content)

        # 存放在数据库中 Devices
        # 结构?
        device_key = {
            "device_key":DeviceKey
        }
        device_list.append(device_key)

    MongoDB.Devices.insert_many(device_list)

create_qr(5)


