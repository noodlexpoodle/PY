# Part 1, import module
# from l16classbasic import Planet
#
# naboo = Planet('Naboo',300000,8,'Naboo System')
# print(f'Name:{naboo.name}')
# print(naboo.spin('a very high speed'))


# Part 2, import package
from space.planet import Planet
from space.calc import planet_vol,planet_mass

naboo = Planet('Naboo',8,300000,'Naboo System')

naboo_mass = planet_mass(naboo.gravity,naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print (f'Planet {naboo.name} has a mass of {naboo_mass:.3f} and a volume of {naboo_vol:.3f}')
