import time
import os

while True:
    if os.path.exists('fruits.txt'):
        with open('fruits.txt','r') as myfile:
            print(myfile.read())
    else:
        print('File is not present')
        time.sleep()