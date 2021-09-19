#Peter Dauenhauer
#Assignment 7
#Date: 11/15/19
#Section: MW 9:30-11
#This program uses the Bread class created in a different file to process
#business functions

import bread      #import class from other file

breadList = []   #initializing empty list

def menu():    #defining menu function
    print('''Welcome to Delicious Bread!
Please select an option from the menu below:
A: Output information for all breads
B: Set a new price for a bread      
C: Output inventory for a specific bread
X: Exit the program
''')   #all text for menu
    choice = str(input('Your choice: '))    #receive choice
    choice = choice.upper()
    while choice != 'A' and choice != 'B' and choice != 'C' and choice != 'X':  #validation loop for menu selection
        choice = input('Invalid choice! Try again: ')
        choice = choice.upper()     #make choice uppercase
    return choice

def printAllBreads(list1):
    for item in range(3):       #iterating function to print all objects in breadList
        print(list1[item])

def setPrice(list2, bType, bPrice):   #defining setPrice
    flagFound = 0     #defining a flag 
    for item in range(3):
        if bType == list2[item].get_breadType():  #searching for bread type within list
            list2[item].set_price(bPrice)   #running the set_price function from bread.py
            flagFound = 1    #making sure flag is set to true
            break
    if flagFound == 0:    #returning 0 if no matching bread type was found
        return 0
    
    
def outputBreadInventory(list3,bType):  #defining output bread inventories
    flagFound = 0           #defining another flag
    for item in range(3):
        if bType == list3[item].get_breadType():   #searching for bread type in breadList
            inventory = list3[item].get_inventory() #running get_inventory function from bread.py
            print('Inventory is: ', inventory)
            flagFound = 1
            break       #breaking out of loop
    if flagFound == 0:    #returning 0 if flag is false and no breadtype was found
        return 0
    
        
try:   #try clause
    
    def main():   #defining main() function

        bread1 = bread.Bread("BUTTER", '10', '3.50')
        breadList.append(bread1)
        bread2 = bread.Bread("WHEAT", '50', '4.00')       #instantiating the three bread objects
        breadList.append(bread2)
        bread3 = bread.Bread("RAISIN", '25', '3.50')
        breadList.append(bread3)
    
    
        loop = 'y'
        while loop != 'X':     #validation loop 
            choice = menu()    #receive menu selection
            if choice == 'A':
                printAllBreads(breadList)  #running printAllBreads for selection A
            elif choice == 'B':
                breadType = input('What type of bread would you like?: ')  #receive desired bread type
                breadType = breadType.upper()
                price = float(input('Enter a price: '))    #receive new price
                fail = setPrice(breadList,breadType,price)
                if fail == 0:      #if clause for condition that bread type was not found
                    print('Bread type was not found')
            elif choice == 'C':
                breadType = input('What type of bread would you like?: ')  #receive desired bread type
                breadType = breadType.upper()
                fail = outputBreadInventory(breadList,breadType)
                if fail == 0:               #if clause for condition that bread type was not found
                    print('Bread type was not found')
            elif choice == 'X':
                break   #breaking out of loop
            
    main()

except ValueError:     #handling value error exception
    print("Don't enter strings in number fields!")
except Exception as err:    #handling all other exceptions
    print('System Message:', err)
    
