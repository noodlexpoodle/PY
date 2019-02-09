y = 13
a = [2,3,5,7,11,13]
#note that a[-1] comes after x for the value
while a[-1] < 2000000:
    z = 0
    y += 2
    for i in a:
        if y % i == 0:
            z += 1
    if z == 0:
        a.append(y)

print(a[-2])
print(x)
