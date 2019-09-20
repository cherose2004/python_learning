import json

from redis import Redis

redis_cli = Redis(host="192.168.12.87",port=6379,db=6)

user_info = json.dumps({"name":"娟儿","age":999,"gender":"女"})

# redis_cli.set("userinfo",user_info)
res = redis_cli.get("userinfo")
print(json.loads(res))

# print(res.decode("utf8"))