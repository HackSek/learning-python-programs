integer1 = 3.1082012093928012
integer2 = 1.210928347667898

# formatting using the mainstream way
print('the first integer is', integer1, 'and the second integer is', integer2)

# formatting using the format method
# using the colon after the index indicates the use of formatting options (in this case the precision formatting option)
print('the first integer is {0:.3f} and the second integer is {1:.3f}'.format(integer1, integer2))

# formatting using f-strings
# we use the same syntax for formatting options
print(f'the first integer is {integer1:.3f} and the second integer is {integer2:.3f}')
