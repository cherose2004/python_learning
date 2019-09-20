class Foo(object):
    def __call__(self, *args, **kwargs):
        print("你执行了call方法")


foo = Foo()

foo()