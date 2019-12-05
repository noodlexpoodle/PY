class Planet():
#class has no variable hence it's all default value
    shape='round'# this is class level attribute
    def __init__(self,name,gravity,system,radius): #set up a class, with specific values. but the values dont have to be specific
        self.name=name
        self.gravity=gravity
        self.system=system
        self.radius=radius
        pass
# this init self is the attribute of the class
    def orbit(self): #another function to give a value within the class. This is a method of the class
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'
    #will apply to all instances, and even the self class

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins at a {speed}'
#attaching a method to the class
hoth=Planet('Hoth',5.5,'Hoth System',20000)
print('The name is' + hoth.name)
# hoth is now the class
print(f'The gravity is {hoth.gravity} in the system {hoth.system}')
print('The radius is ',hoth.radius)
print(hoth.orbit()) #print out the result of the function
#the function is accessible via the class

naboo=Planet('Naboo',10,'Naboo System',34000)
print(naboo.orbit())
#you can have both instance and class level attribute
#you can also have instance level method, and class level method
print(Planet.commons()) #ok to use class with class method
print(naboo.commons()) #ok to use instance with class method
#cannot use class with instance classmethod
print(Planet.spin('a very high speed'))
