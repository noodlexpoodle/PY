# file=open("055 fruits.txt",'r')
# content = file.readlines()
# file.close()
# for i in content:
#     print(i)

temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c>= -273.15:
        f=c*9/5+32
        f=str(f)
        with open('066.txt','a') as test:
            test.write('\n'+f)

for t in temperatures:
    c_to_f(t)
