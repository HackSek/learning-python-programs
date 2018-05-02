# 'w' stands for 'write'
with open('./text_files/target.txt', 'w') as target_file:
    target_file.write('Currently learning how to write to files on a computer')

# 'a' stands for 'ammend'
with open('./text_files/target.txt', 'a') as target_file:
    target_file.write('\nStill have a lot to learn before becoming a python expert')

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('./text_files/target.txt', 'a') as target_file:
    target_file.writelines(quotes)
