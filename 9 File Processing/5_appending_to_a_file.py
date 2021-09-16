
with open('fruits.txt','a') as myfile:
    myfile.write('\nLitchie')
    print(myfile)
    myfile.close()


with open('fruits.txt','a+') as myfile:
    myfile.write('\nLitchie')
    myfile.seek(0)
    print(myfile)
    myfile.close()


with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)

