def f1(*args, **kw):
    print(args)
    print(type(args))
    print(kw)
    print(type(kw))


f1(1,2,23,34,45, x=122, y='1234')