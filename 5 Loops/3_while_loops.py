a = 3
while a >= 3:
    print("CSK Wins")
    break


user_input = input('Enter City')
while user_input == 'Chennai':
    print('Chennai pasanga da')
    break


user_in = input('Enter Country')
while type(user_in) == str:
    if user_in == 'India':
        print('India is the best')
        break
    else:
        print('Other country is the best')
        break
