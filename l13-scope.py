my_name='ryu'

def print_name():
    my_name='yoshi'
    print('the name inside function is ',my_name)

print_name()
print('outside function name is ',my_name)

# when you call a function, all the commands inside only affect inside
# in order to make it affect global, must put global to make the variable global
