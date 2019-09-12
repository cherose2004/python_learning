import json

from Config import RDB


# 设置未读消息 , 在哪儿设置?
# sender 向 receiver 发起消息时 向receiver 的数据中 +1 或 创建
def set_msg(sender, receiver):
    # 1.当前没有这个receiver的数据 创建receiver的字典
    msg_count = RDB.get(receiver)
    if msg_count:
        # 2.当receiver收到 sender 的消息, 对应当前sender + 1
        msg_count_dict = json.loads(msg_count)
        # sender 是不是第一次给 receiver 发消息
        if msg_count_dict.get(sender):
            msg_count_dict[sender] += 1
        else:
            msg_count_dict[sender] = 1
        msg_count = json.dumps(msg_count_dict)
    else:
        msg_count = json.dumps({sender: 1})

    RDB.set(receiver, msg_count)


# 获取未读消息
def get_msg_one(sender, receiver):
    msg_count = RDB.get(receiver)

    # 可以优化的
    if msg_count:
        msg_count_dict = json.loads(msg_count)
        count = msg_count_dict.get(sender, 0)

        if count == 0:
            for k, v in msg_count_dict.items():
                if v != 0:
                    sender = k
                    count = v

        msg_count_dict[sender] = 0
    else:
        msg_count_dict = {sender: 0}
        count = 0

    RDB.set(receiver, json.dumps(msg_count_dict))

    return count, sender


def get_msg_all(receiver):
    msg_count = RDB.get(receiver)
    msg_count_dict = {"count": 0}
    if msg_count:
        msg_count_dict = json.loads(msg_count)
        msg_count_dict["count"] = sum(msg_count_dict.values())
    return msg_count_dict

# set_msg("user2","user3")
