num = 3
n = 1
while n < 10001:
    x = 1
    for i in range(2,num):
        if num % i == 0:
            x = 0
            break
    if x == 1:
        n += 1
        max = num
    print(n)
    num += 2
    # print(num)

print(max)
