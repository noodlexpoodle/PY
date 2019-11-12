meatoption = input('Do you eat meat (y/n): ')
meatmenu = ['Steak','Chicken','Lamb']
vegmenu = ['Kangkong','Broccoli','Kailan']

if meatoption == 'y':
    print('Here is the menu:')
    print(*meatmenu,*vegmenu,sep="\n")
else:
    print('Here is the menu:')
    print(*vegmenu,sep="\n")
