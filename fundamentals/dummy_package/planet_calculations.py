def calculate_mass(radius, gravity):
    mass = (gravity * gravity ** 2) / (6.67 * 10 ** -11)
    return mass

def calculate_volume(radius):
    volume = (4 * 3.142 * radius ** 2) / 3 
    return volume
