import csv


class Shop:
    all = []

    def __init__(self, name: str, price: int, quantity: int):
        #Run validation
        assert 0 <= price
        assert 0 <= quantity

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Shop.all.append(self)

    def calculate(self):
        print(self.price*self.quantity)

    @classmethod
    def opencsv(cls):
        with open('products.csv', 'r') as f: #otvorí csv file (r) - prečíta
            reader = csv.DictReader(f)
            items = list(reader) #uloží do items
        for item in items:
            print(item)

    def __repr__(self): #preloží do normalného jazyka AKA nedá iba kod
        return f"{self.name} - {self.price}, {self.quantity}."



Shop.opencsv()



