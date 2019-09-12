from functools import partial

def ab(a,b):
    print(a,b)
    return a+b

# print(ab(1,2))

new_func = partial(ab,1,3)


print(new_func())


from flask import request