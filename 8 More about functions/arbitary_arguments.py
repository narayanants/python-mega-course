def foo(*args):
    return sum(args) / len(args)

print(foo(1,3,5))