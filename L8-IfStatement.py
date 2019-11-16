meatoption = input('Do you eat meat (y/n): ')
meatmenu = ['Steak','Chicken','Lamb']
vegmenu = ['Kangkong','Broccoli','Kailan']

if meatoption == 'y':
    print('Here is the menu:')
    print(*meatmenu,*vegmenu,sep="\n")
    # Asterisk * is to display wout sq bracket
    # sep="\n" means separates with a line
else:
    print('Here is the menu:')
    print(*vegmenu,sep="\n")
