def ninja_intro(dictionary):
    for ke, va in dictionary.items():
            print(f'i am {ke} and i am a {va} belt')

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print (f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input ('enter name: ')
    ninja_belt = input ('enter belt: ')
    ninja_belts[ninja_name]=ninja_belt

    another=input('add another? (y/n)')
    if another =='y':
        continue
    else:
        break

belt_count(ninja_belts)
x= ninja_belts.items(0)
print (x)
