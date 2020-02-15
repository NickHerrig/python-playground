
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo("hello",)
foo("hello",1,2,3,)
foo("hello", 1, 2, 3, key1='hello', key2=999)

