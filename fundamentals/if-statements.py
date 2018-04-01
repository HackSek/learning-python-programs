# age = int(input('How old are you? '))
#
# if age <= 18:
#     print('You\'re not allowed to vote yet...')
# elif age <= 30:
#     print('You wish to go back to the days when you still weren\'t allowed to vote')
# else:
#     print('You\'re just old')

meatLover = input('Are you a meat lover? (y/n) ')

if meatLover == 'n':
    print('Let me get you the veggie menu')
elif meatLover == 'y':
    print('Let me get you the meaty menu')
else:
    print('IT\'S A Y OR N QUESTION !!! try again!')
