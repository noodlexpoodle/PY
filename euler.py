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


a=13195
b=60085
c=2
e=0
f = 100000
while e  <b:
    while c < b :
        d= b%c
        if d == 0:
            e=c
        c += f
    f=f/2
    round (f,0)
print (e)
