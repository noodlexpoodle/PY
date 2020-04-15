def ninja_intro(dictionary):
    for ke, va in dictionary.items():
            print(f'i am {ke} and i am a {va} belt')
#if you print the dict.items() will print all.
#in order to print a single value, you must use dict.keys and dict.values

def belt_count(dictionary):
    belts = list(dictionary.values())
#create a list from a dict
    for belt in set(belts):
#set will remove duplicate from list
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
