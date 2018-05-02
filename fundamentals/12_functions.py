var_x = int(input('what is the radius of the circle in meters? '))
var_y = int(input('what is the length of the cylinder in meters? '))

def calc_area(radius):
    area = 3.142 * radius ** 2
    print(f'the area of the circle is {area} square meters')
    return area

def calc_volume(area, length):
    volume = area * length
    print(f'the volume of the cylinder is {volume} cube meters')

calc_volume(calc_area(var_x), var_y)
