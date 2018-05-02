from dummy_package.planet_class import Planet
from dummy_package.planet_calculations import calculate_mass, calculate_volume

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(naboo.define_speed(str(5000)), 'mph')

naboo_mass = calculate_mass(naboo.radius, naboo.gravity)
naboo_volume = calculate_volume(naboo.radius)
print(f'{naboo.name} has a mass of {naboo_mass} KG and and a volume of {naboo_volume} cube meters')
