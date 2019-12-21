#max is 997799
import math
max = 0
n1 = 0
n2 = 0
count = 0
for i in reversed(range(99,998)):
# run through all the palindrome
    cur = [x for x in str(i)]
    curfull = cur
    for n in reversed(cur):
        curfull.append(n)
    num = int("".join(curfull))
    # create the full number
    for n in reversed(range(99,math.floor(math.sqrt(num)))):
        if (num % n == 0 and num/n < 999 and num/n > 99):
            if num > max:
                max = num
                n1 = n
                n2 =num/n
    #check for the satisfying product

print(f'Largest palindrome is {max}, as the product of {n1} and {n2}')
print(n1*n2)
