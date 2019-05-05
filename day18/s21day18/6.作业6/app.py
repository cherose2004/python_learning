#!/usr/bin/env python
# -*- coding:utf-8 -*-



def run():
    """
    主函数
    :return:
    """
    while True:
        num = int(input('请选择页码:')) # >0 # 2
        per_page_count = 10
        # 每页显示10条数
        start = (num-1) * per_page_count # 10
        end = num * per_page_count # 20

        result = []
        count = 0
        with open('db.txt',mode='r',encoding='utf-8') as f:
            first_line = f.readline()
            for line in f:
                if count == end:
                    break

                if count >= start: # 10
                    result.append(line)

                count += 1

        for i in range(len(result)):
            print(i+1,result[i])





if __name__ == '__main__':
    run()