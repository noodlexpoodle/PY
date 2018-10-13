# def euler3(a):
#     b = 2
#     while a > b:
#         if a%b == 0:
#             a==a/b
#             b=2
#         else:
#             b +=1
#
#     print (f'largest prime factor is {b}')
#
# euler3(60085147514)

#euler 3
# a = 2
# b = 600851475143
# while a < b:
#     if b % a == 0:
#         b = b/a
#     else:
#         a += 1
# print (a)

#euler4
a=999
b=999
c=0
g=0
while b > 100:
    c = b*a
    d = list(str(c))
    e = d[0:3]
    f = d[3:6]
    #print(e)
    f.reverse()
    #print(f)
    if (e == f and c > g) :
        g = c
        h = a
        i = b
    a -= 1
    if a == 100:
        b -= 1
        a = b
print (f'Largest such number is {g}')
print (f'It is the product of {h} and {i}')
