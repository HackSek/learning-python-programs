radius = input('give the radius IN METERS of a particular circle  and I\'ll calculate its area : ')

# using the type casting process to convert the radius variable from one data type (string) to another data type (integer)
area = 3.142 * int(radius) ** 2

print(f'the area of this circle is : {area} square meters')
