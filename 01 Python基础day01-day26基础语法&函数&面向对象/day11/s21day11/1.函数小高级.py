def func():
    print('花费查询')


def bar():
    print('语音沟通')


def base():
    print('xxx')


def show():
    print('xxx')


def test():
    print('xxx')

info = {
    'f1': func,
    'f2': bar,
    'f3':base,
    'f4':show,
    'f5':test
}
choice = input('请选择要选择功能：')
function_name = info.get(choice)
if function_name:
    function_name()
else:
    print('输入错误')
