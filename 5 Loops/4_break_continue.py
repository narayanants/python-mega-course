user_in = input('Enter Country: ')
while type(user_in) == str:
    if user_in == 'India':
        print('India is the best')
        break
    else:
        print('Other country is the best')
        break




def sentence_maker(ph):
    if ph.startswith(('how','Hello','hi')):
        cp = ph.upper()
        return "{}".format(cp)


print(sentence_maker('Hello this is narayanan'))