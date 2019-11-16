

meatoption = 'y'
#meatoption = input('Do you eat meat (y/n): ')
meatmenu = ['Steak','Chicken','Lamb']
vegmenu = ['Kangkong','Broccoli','Kailan']

for meat in meatmenu[0:2]:
    print(meat)

# if meatoption == 'y':
#     print('Here is the menu:')
#     print(*meatmenu,*vegmenu,sep="\n")
# else:
#     print('Here is the menu:')
#     print(*vegmenu,sep="\n")
for n in range(len(meatmenu)-1,0,-1):
    print(n,meatmenu[n])
for n in range(len(meatmenu)):
    print(n,meatmenu[n])
print(len(meatmenu))
