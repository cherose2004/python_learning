import os

from aip import AipSpeech


""" 你的 APPID AK SK """
APP_ID = '16981685'
API_KEY = '9yjA1ijtDpy6SNzxOrsFFlns'
SECRET_KEY = 'o4GrQeXlUDWmGFefntxdU1cCKiVj9y3k'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    cmd_str = f"ffmpeg -y  -i {filePath}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
    os.system(cmd_str)
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

# 识别本地文件
res = client.asr(get_file_content('wyn.m4a'), 'pcm', 16000, {
    'dev_pid': 1536,
})

print(res.get("result")[0])

# 文档呢? √
# PCM文件呢?
# FFMPEG

# ffmpeg -y  -i audio.wav  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 audio.pcm


# baidu ASR
# 需要的语音文件为 PCM 格式 转换PCM格式文件
# ffmpeg 的工具 ffmpeg -y  -i audio.wav  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 audio.pcm
# Pycharm 环境变量没有重新加载 出现了错误  重启Pycharm 如果重启不好使 restart PC
# 更改读取文件的函数 os.system(ffmpeg -y  -i audio.wav  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 audio.pcm)
# open文件时 需要使用 PCM格式的文件
