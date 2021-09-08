x = 1
y = 'Hello'
z = 10.123

d = x + z
print(d)

print(type(x))
print(type(y))
print(y.upper())
print(y.lower())
print(type(z))

a = [1,2,3,4,5,6,6,7,8]

print(len(a))
print(a.count(6))




b = list(range(10,100,10))
print(b)


stud_marks = {"Madhan":90, "Raj":25,"Mani":80}
print(stud_marks.keys())
print(stud_marks.values())


ab = list(range(10,100,10))
ab.append(100)
ab.append(110)
ab.remove(110)

print(ab[0:2])