# dummy_file = open('./text_files/ipsum.txt')
#
# for line in dummy_file:
#     print(line.rstrip())
#
# dummy_file.seek(0)
#
# lines_list = dummy_file.readlines()
# print(lines_list)
#
# dummy_file.seek(25)
#
# sample_text = dummy_file.read(75)
# print(sample_text)
#
# dummy_file.close()

with open('./text_files/dna_sequences.txt') as dna_sequences:
    # print([ sequence for sequence in dna_sequences if '>' not in sequence ])
    sequences_list = list(filter(lambda line: '>' not in line, dna_sequences))
    print(sequences_list)
