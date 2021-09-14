def mean(x,y):
    if type(x) == int and type(y) == float:
        x = x
        y = y
        z = x + y
        return z
    else:
        print('Invalid argument')
    
print(mean(1,2.0))