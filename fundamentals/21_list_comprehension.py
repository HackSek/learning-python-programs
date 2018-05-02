# comprehension is an alternative method of constructing lists and dictionaries based on other collections
# It utilises less syntax compared to writing such program using iteration with for loops

monetary_prizes = ['20', '40', '50', '100', '200', '500', '1000']

# doubled_monetary_prizes = []
# for prize in monetary_prizes:
#     doubled_monetary_prizes.append(int(prize) * 2)

doubled_monetary_prizes = [ int(prize) * 2 for prize in monetary_prizes ]

print(doubled_monetary_prizes)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for integer in integers:
#     if integer % 2 == 0:
#         transformed_integers.append(integer ** 2)
#     else:
#         transformed_integers.append(integer ** 3)

transformed_integers = [integer ** 2 for integer in integers if integer % 2 == 0] + [integer ** 3 for integer in integers if integer % 2 != 0]

print(transformed_integers)
