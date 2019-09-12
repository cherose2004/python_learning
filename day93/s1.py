import json

from pymongo import MongoClient
from bson import ObjectId

MC = MongoClient("127.0.0.1",27017)
MongoDB = MC["S21DAY93"]


# MongoDB.player.insert_one({"name":"Q哥","act":15})

res = MongoDB.player.find_one({"name":"Q哥"})

res["act"] = 999
res["_id"] = str(res.get("_id"))

print(json.dumps(res))


# MongoDB.player.update_one({"name":"Q哥"},{"$set":res})





# res = MongoDB.Users.insert_one({"name":"YWB","age":999})
# res = MongoDB.Users.insert_many([{"name":"JWB","age":999},{"name":"wpq","age":999}])
# print(res.inserted_id,type(res.inserted_id))
# print(res.inserted_ids,type(res.inserted_ids))

# res = MongoDB.Users.find({"_id":ObjectId("5d50e778b2a72712f5ee54c5")})
# res = MongoDB.Users.find_one({"name":"YWB"})
# <pymongo.cursor.Cursor object at 0x000001F6C5027550> 生成器
# for row in res :
#     print(row)
# print(res)


# 改:
# MongoDB.Users.update_one({},{"$inc":{"age":1}})
# MongoDB.Users.update_many({"age":1000},{"$inc":{"age":1}})

# 删除数据
# MongoDB.Users.delete_one({})
# MongoDB.Users.delete_many({})



# 高级函数
# from pymongo import DESCENDING,ASCENDING
# res = MongoDB.Users.find({}).sort("age",ASCENDING)
# for row in res:
#     print(row)