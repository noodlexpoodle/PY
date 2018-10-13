#euler6

a = []
for i in range (1,101):
    a.append(i)
print(a)

#sumofsq
b = [i**2 for i in a]
print(b)
c = int(0)
for i in b:
    c += i
print(c)

#sq of sum
d = int(0)
print(a)
for i in a:
    d += i
print (d)
d = d**2
print (d)
e = abs(c-d)
print (e)
