stud = {
    'Madhan':24,
    'Raj':30,
    'Narayanan':29
}

for s1 in stud.keys():
    print(s1)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key,value in phone_numbers.items():
    print("{} has phone number {}".format(key,value))


names = {
    'Girija':53,
    'Subramanian':62,
    'Narayanan':29,
    'Gopal':65,
    'Vijayam':65
}

for n in names.keys():
    print(n)

for n1 in names.values():
    print(n1)

for n1,n2 in names.items():
    print("{} has age {}".format(n1,n2))