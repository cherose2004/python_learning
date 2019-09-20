import os

import pypinyin
import requests
from bson import ObjectId

from Config import AUDIO_CLIENT, VOICE, CHAT_PATH, MongoDB, TL_URL, TL_DATA
from uuid import uuid4

from my_nlp import my_gensim_nlp


def text2audio(text):
    filename = f"{uuid4()}.mp3"
    file_path = os.path.join(CHAT_PATH, filename)
    res = AUDIO_CLIENT.synthesis(text, "zh", 1, VOICE)
    if type(res) == dict:
        pass
    with open(file_path, "wb") as f:
        f.write(res)

    return filename


def audio2text(filepath):
    res = get_file_content(filepath)
    # 识别本地文件
    ret = AUDIO_CLIENT.asr(res, 'pcm', 16000, {
        'dev_pid': 1536,
    })

    print(ret.get("result")[0])
    return ret.get("result")[0]


def my_nlp_lowB(Q:str, toy_id):
    # 理解 Q 的意图  Q = 我想听小毛驴
    # 1.点播歌曲 - 我想听小毛驴 - 我要听 - 请播放
    if "我想听" in Q or "我要听" in Q or "请播放" in Q:
        # 升级 NLP LowB - NLP LowB Plus
        q = Q
        q = q.replace("我想听","")
        q = q.replace("我要听","")
        q = q.replace("请播放","")
        print(q)
        content_dict = my_gensim_nlp(q)
        print(Q)
        if content_dict:
            return {"from_user": "ai", "music": content_dict.get("music")}
        # content_list = list(MongoDB.Content.find({})) # 300万内容 2000人
        # for content in content_list:
        #     if content.get("title") in Q:  # 百度NLP 中的文本相似度来实现 QPS的限制
        #         return {"from_user": "ai", "music": content.get("music")}

    # 2.主动发起聊天
    # Q = 我要给爸爸发消息  我要和baba聊聊天 说说话
    if "发消息" in Q or "聊天" in Q:
        Q_py = "".join(pypinyin.lazy_pinyin(Q, pypinyin.TONE3))
        toy = MongoDB.Toys.find_one({"_id": ObjectId(toy_id)})
        for friend in toy.get("friend_list"):
            nick_py = "".join(pypinyin.lazy_pinyin(friend.get("friend_nick"), pypinyin.TONE3))
            remark_py = "".join(pypinyin.lazy_pinyin(friend.get("friend_remark"), pypinyin.TONE3))
            if nick_py in Q_py or remark_py in Q_py:
                filename = text2audio(f"现在可以给{friend.get('friend_remark')}发消息了")
                return {
                    "from_user": friend.get("friend_id"),
                    "chat": filename,
                    "friend_type": friend.get("friend_type")
                }

    # 3.对接图灵机器人
    TL_DATA["perception"]["inputText"]["text"] = Q
    TL_DATA["userInfo"]["userId"] = toy_id
    res = requests.post(TL_URL, json=TL_DATA)
    res_json = res.json()
    filename = text2audio(res_json.get("results")[0].get("values").get("text"))
    return {"from_user": "ai", "chat": filename}

# 转PCM并且读取PCM文件流
def get_file_content(filePath):
    cmd_str = f"ffmpeg -y  -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
    os.system(cmd_str)
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()
