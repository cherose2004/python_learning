from pypinyin import lazy_pinyin,TONE,TONE2,TONE3

a = "我要给圆圆发消息"
az = "woyaogeiyuanyuanfaxiaoxi"
#换成字母
b = "我要给元元发消息"
bz = "woyaogeiyuanyuanfaxiaoxi"
#换成字母
c = "我要给苑苑发消息"
cz = "woyaogeiyuanyuanfaxiaoxi"

resa = lazy_pinyin(a,style=TONE)
resb = lazy_pinyin(b,style=TONE2)
resc = lazy_pinyin(c,style=TONE3)

print(resa)
print(resb)
print(resc)

print("".join(resc))
print("".join(resb))
