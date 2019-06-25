"""class Product:
    def getProduct(self):
        self.id = input('Enter id: ')
        self.name = input('Enter name: ')
        self.price = int(input('Enter price: '))
        self.stock = int(input('Enter stock available: '))
    def putProduct(self):
        print(self.id, self.name, self.price, self.stock)
    def search_id(self, id):
        if id == self.id:
            return True
        else: return False
    def search_price(self, min, max):
        if self.price > min and self.price < max:
            return True
        else: return False
L = []
for _ in range(int(input('Enter no. of Products: '))):
    s = Product()
    s.getProduct()
    L.append(s)
while True:
    print('\n::: Menu :::')
    print('1. Display all Products')
    print('2. Search by ID')
    print('3. Search by Price')
    print('4. Exit')
    c = int(input('Enter your choice: '))
    if c == 1:
        for x in L:
            x.putProduct()
    elif c == 2:
        id = input('Enter ID: ')
        found = False
        for x in L:
            if x.search_id(id):
                x.putProduct()
                found = True
        if not found:
            print('ID not found.')
    elif c == 3:
        min, max = (int(x) for x in input('Enter Min and Max price seperated by a space: ').split())
        found = False
        for x in L:
            if x.search_price(min, max):
                x.putProduct()
                found = True
                break
        if not found:
            print('No Product found within the given range.')
    elif c == 4:
        break
    else:
        print('Invalid Choice.')"""

class Product:
    def getProduct(self):
        self.id = input('Enter id: ')
        self.name = input('Enter name: ')
        self.price = int(input('Enter price: '))
        self.stock = int(input('Enter stock available: '))
    def putProduct(self):
        print(self.id, self.name, self.price, self.stock)
    def search_price(self, min, max):
        if self.price > min and self.price < max:
            return True
        else: return False
    def sale(self):

L = []
for _ in range(int(input('Enter no. of Products: '))):
    s = Product()
    s.getProduct()
    L.append(s)
while True:
    print('\n::: Menu :::')
    print('1. Display all Products')
    print('2. Search by Price')
    print('3. Sale')
    print('4. Purchase')
    print('5. Exit')
    c = int(input('Enter your choice: '))
    if c == 1:
        for x in L:
            x.putProduct()
    elif c == 2:
        id = input('Enter ID: ')
        found = False
        for x in L:
            if x.search_id(id):
                x.putProduct()
                found = True
        if not found:
            print('ID not found.')
    elif c == 3:
        min, max = (int(x) for x in input('Enter Min and Max price seperated by a space: ').split())
        found = False
        for x in L:
            if x.search_price(min, max):
                x.putProduct()
                found = True
                break
        if not found:
            print('No Product found within the given range.')
    elif c == 4:
        break
    else:
        print('Invalid Choice.')

