def mean(x,y):
    if type(x) == int and type(y) == float:
        x = x
        y = y
        z = x + y
        return z
    else:
        print('Invalid argument')
    
print(mean(1,2.0))



def mean(mylist):
    if type(mylist) == list:
        mymean = sum(mylist) / len(mylist)
        return mymean

list= [1,2,3,4,5,6,7]
print(mean(list))