# def greet():
#     print('hello world')
#
# greet()
# greet()
# greet()
# greet()
# def greet(a='sir',d='day'):
#     print(f'Good {d}, {a}')
# # f'text {variable}
# # f is for formatting, the {} will be the variable
# b=input("What's your name ")
# c=input("What's the time ")
# if b is not None and c is not None:
#     greet(b,c)
#     print(1)
# elif b is not None and c is None:
#     greet(c='day')
#     print(2)
# elif b is None:
#     greet(b='sir')
#     print(3)
# else:
#     greet()
#     print(4)
#     pass

# First define the function with def name (var)
# Then call function by name and input the variable
# SIMPLE!
# You can input a default value in case value is missing

def area(rad):
    area=3.142*rad*rad
    print(f'The area of circle with radius of {rad:.2f} is {area:.2f}')
#this function will perform the actions

def areavalue(rad):
    return 3.142*rad*rad
    pass
#this function will give the number. that is the diff from the above fn
def vol(area,len):
    vol=area*len
    print(f'The volume is {vol}')
rad=int(input('please input the radius '))
len=int(input('please input the height '))

area(rad)
areacalc=areavalue(rad)
#this fn must use the areavalue to get the value instead of the area()
#you need the areacalc to be an int value
vol(areacalc,len)
vol(areavalue(rad),len)
