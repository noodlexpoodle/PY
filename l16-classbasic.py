class Planet():
#class has no variable hence it's all default value
    def __init__(self): #set up a class, with specific values. but the values dont have to be specific
        self.name='Hoth'
        self.gravity=5.5
        self.system='Hoth System'
        self.radius=20000
        pass

    def orbit(self): #another function to give a value within the class.
        return f'{self.name} is orbiting in the {self.system}'

#attaching a method to the class
hoth=Planet()
print('The name is' + hoth.name)
# hoth is now the class
print(f'The gravity is {hoth.gravity} in the system {hoth.system}')
print('The radius is ',hoth.radius)
print(hoth.orbit()) #print out the result of the function
#the function is accessible via the class
