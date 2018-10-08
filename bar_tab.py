class tab:

    #dictionary
    menu = {
        'wine':5,
        'beer':2,
        'coke':3,
        'chicken':9,
        'dessert':7
    }

    #set up the class
    def __init__(self):
        #set up empty initial total and item list, test add comment
        #customer will add items and total will add up
        #these variables will exist within the class
        self.total = 0
        self.items = []

    #function for add items to tab
    def add(self,item):
        self.items.append(item)
        #add the value from menu dictionary for the 'item'
        self.total += self.menu[item]

    def pay_bill (self,tax,service):
        #tax will only exist within this function in the class
        tax=(tax/100) *self.total
        service=(service/100)*self.total
        total=self.total + tax + service

        for item in self.items:
            print(f'{item:20} ${self.menu[item]}')

        print(f'{"Total":20} ${total:.2f}')
