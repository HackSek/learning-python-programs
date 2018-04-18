from random import shuffle

def shuffle_a_word(argument):
    word_to_shuffle = list(argument)
    shuffle(word_to_shuffle)
    return ''.join(word_to_shuffle)

words_to_shuffle = list()

while True:
    add_a_word = input('what word would you like to shuffle? ')
    add_another = input('would you like to add another word? (y/n) ')
    if add_another == 'n':
        words_to_shuffle.append(add_a_word)
        break
    else:
        words_to_shuffle.append(add_a_word)
        continue

# shuffled_words = list()
#
# for word_to_shuffle in words_to_shuffle:
#     shuffled_words.append(shuffle_a_word(word_to_shuffle))
#
# print(shuffled_words)

# print([ shuffle_a_word(word_to_shuffle) for word_to_shuffle in words_to_shuffle ])


print(list(map(shuffle_a_word, words_to_shuffle)))
