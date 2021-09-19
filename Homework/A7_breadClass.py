#Assignment 7 Class

class Bread:
    def __init__(self,breadType,inventory,price):
        self.__breadType = breadType
        self.__inventory = inventory
        self.__price = price

    def __str__(self):
        return 'Bread type is ' + self.__breadType + '\n' + \
               'Inventory is ' + self.__inventory + '\n' + \
               'Price is ' + self.__price + '\n'
    def set_breadType(self, newType):
        self.__breadType = newType

    def get_breadType(self):
        return self.__breadType

    def set_inventory(self, newInventory):
        if newInventory > 0:
            self.__inventory = newInventory
        else:
            print("Please enter a positive, nonzero number")
    def get_inventory(self):
        return self.__inventory

    def set_price(self, newPrice):
        if newPrice <= 0:
            print("Please enter a positive, nonzero number")
        elif newPrice > 5.5:
            print("The price can't be greater that $5.50!")
        else:
            self.__price = newPrice

    def get_price(self):
        return self.__price
    
        
