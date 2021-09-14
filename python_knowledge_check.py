def foo(a = 1, b = 2):
    return a + b
price = foo(b = 4)


for item in [[1, 2, 3], [4, 5, 6]]:
    print(item[0])

mylist = [['abc'], ['def', 'ghi']]
mylist[-1][-1][-1]



def eur_to_usd(euros, rate=0.8):
    return euros * rate
print(eur_to_usd(10))

weight = input("How many kg?")
price = weight * 2.5
print(price)



x = [len(item) for item in ['abc', 'def', 'ghi']]


y = [i * 2 if i > 0 else 0 for i in [1, -2, 10]]


def foo(x):
    return x ** 2
print(foo("Hello"))


def foo(a = 1, b = 'John'):
    return a + b
foo()