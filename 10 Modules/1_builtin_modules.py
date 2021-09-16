import time
while True:
    with open('fruits.txt','r') as myfile:
        print(myfile.read())
        time.sleep(10)