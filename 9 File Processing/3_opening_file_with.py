myfile = open('fruits.txt','r')
print(myfile.read())
myfile.close()


with open('fruits.txt','r') as myfile:
    z = myfile.read()
print(z)