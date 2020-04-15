# a+b+c = 1000
#a^2 + b^2 = c^2
a = int()
b = int()
c = int()
for c1 in reversed(range(1000)):
    for b1 in reversed(range(1,1000-c1)):
        a1 = 1000 - c1 - b1
        asq = c1**2 - b1**2
        if a1**2 == asq and a1 > 0:
            print(a1,b1,c1,asq)
            a = a1
            b = b1
            c = c1
            break

print(f'a is {a}, b is {b}, and c is {c}')
print('Product is ', a*b*c)
