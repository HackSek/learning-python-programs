limit = 60
counter = 0

while counter <= limit:
    if counter == 0:
        counter += 1
        continue
    if counter % 5 == 0 and counter != 60:
        print(f'{counter} seconds')
    if counter == 60:
        print('1 minute')
    counter += 1
