#find largest product

number = int(input('Input number'))
number1 = [int(x) for x in number]
for d in number1:
    if d == 0:
        number1.remove(d)

print(f'The list is {number1}')
