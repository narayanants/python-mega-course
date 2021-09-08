def sm(ph):
    intro = ('How','Hello','Why')
    cp = ph.capitalize()
    if ph.startswith('How'):
        return "{}".format(cp)
    else:
        return "{}".format(cp)

results = []
while True:
    user_input = input('Enter Country: ')
    if user_input == '\end':
        break
    else:
        results.append(sm(user_input))

print(' '.join(results))