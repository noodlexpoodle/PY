#a is list of the factors
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=[]
for x in range(1,21):
    a.append(x)
b=a.copy()
b.reverse()
print (a) #correct
print (b) #correct
#a is 1 to 20
#b is 20 to 1
for y in b:
    for x in a:
        if (y % x == 0 and x in b and y!=x):
            b.remove(x)
print (b)
#correct
d = 1
for x in range (2,20):
    i=2
    while i > 1:
        i = 0
        for y in b:
            if (y % x == 0): #and y != x):
                i += 1
        if i>1:
            c = [y/x if (y % x == 0) else y for y in b ]
            d = d * x
        b = c.copy()
    print (b)
e = 1
for i in b:
    e *= i
d = d * e
print (b)
print (d)


# for x in range(2,20):
#     for y in a:
#         z =
#
