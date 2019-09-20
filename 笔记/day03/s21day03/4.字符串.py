#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""

# ############## 1. upper/lower #################
# value = "alex SB"
# new_value = value.upper()
# new_value = value.lower()
# print(value,new_value)

# #### 验证码示例
"""
check_code = 'iyUF'
message = '请输入验证码 %s：' %(check_code,)
code = input(message)
new_check_code = check_code.lower()
new_code = code.lower()
if new_code == new_check_code:
    print('输入成功')
"""
# #### 验证码示例
"""
check_code = 'iyUF'
code = input('请输入验证码 %s :' %(check_code,))
if code.lower() == check_code.lower():
    print('登陆成功')
"""

# ############## 2. isdigit #################
# print("""欢迎致电10086
# 1.花费查询
# 2.业务办理
# 3.款单
# """)
# while True:
#     num = input('请选择服务：')
#     # 判断用户输入 字符串 是否可以转换成 数字。 # “999”  “阿斯顿发生”
#     flag = num.isdigit()
#     # print(flag) # "1" -> True   "asdf" --> False
#     if flag:
#         num = int(num)
#         print(num)
#     else:
#         print('请输入数字')

# ############## 3. 去除空白 strip/lstrip/rstrip ##############
"""
user = input('请输入用户名:') # "  alex  "

# new_user1 = user.rstrip() # new_user1 = "    alex"    user="  alex  "
# new_user2 = new_user1.lstrip()
# 或
new_user2 = user.strip()

data = new_user2.upper()
print('---->',data,'<-----')
"""

# ############## 4. 替换 replace ##############
"""
message = input('请说话：')
print(message) # “我去你大爷的家里玩”
# data = message.replace('大爷',"**")
data = message.replace('大爷',"**",2)
print(data)
"""

# ############## 5. 切割  split/rsplit ##############
"""
message = "小黑现在一脸懵逼，因为昨天晚上一直在学习，直到深夜。"
# result = message.split('，')
# result = message.split('，',1)

# result = message.rsplit('，')
result = message.rsplit('，',1)

print(result)
"""



