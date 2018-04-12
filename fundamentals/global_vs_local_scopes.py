def print_name():
    global var_a
    var_a = 'Ash'
    print('the variable inside the function is equal to', var_a)

print_name()
print('the variable outside the function is equal to', var_a)
