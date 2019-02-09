#10001 prime number
x = 6
y = 13
a = [2,3,5,7,11,13]
#note that a[-1] comes after x for the value
while x < 10001:
    z = 0
    y += 2
    for i in a:
        if y % i == 0:
            z += 1
    if z == 0:
        a.append(y)
        x += 1
print(a)
print(a[-1])
print(x)

#inefficient stackoverflow code
# counter = 2
# n = 10001
# for i in range(3, 1000000, 2):
#  k = 1
#  while k < i:
#   k += 2
#   if i % k == 0:
#    break
#   if k + 2 == i:
#    counter += 1
#   if counter == n:
#    print(i)
#    raise ZeroDivisionError


# for i in range (1,5):
#     if i < 4:
#         print(i)
#     else:
#         break
# print('break successful')
