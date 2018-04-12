martial_arts_dictionary = dict()

while True:
    martial_art = input('What martial art would you like to add? ')
    origin = input('Where has it originated from? ')
    martial_arts_dictionary[martial_art] = origin

    prompt = input('Would you like to add another martial art? (y/n) ')
    if prompt == 'n':
        break
    else:
        continue

def count_countries(variable):
    origins = list(variable.values())
    for origin in set(origins):
        count = origins.count(origin)
        print(f'{origin} has been mentioned {count} times')

count_countries(martial_arts_dictionary)
