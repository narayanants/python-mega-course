
temps = list(range(10,100,10))

temp_1 = [temp/10 for temp in temps]

temp_2 = [temp / 10 for temp in temps if temp != 90]

print(temp_1)

print(temp_2)
