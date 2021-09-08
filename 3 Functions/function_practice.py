def foo(a,b,c):
    if a > 7 and b <=8 and c ==10:
        return a,b,c
    elif a == 5 or b==7 or c == 12:
        print('Greater than if')
        return a,b,c
    else:
        return 'Lesser'

print(foo(5,7,12))
