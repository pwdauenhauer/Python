#Name: Peter Dauenhauer
#Assignment number: 4
#Date: 10/10/19
#Section: MW 9:30-11
#This is a program to keep track of all t shirt orders, charges, and donations
#made by cool t-shirts, incorporating functions into the program 

def main():             #main opener
    TAX = 0.085
    PURPLE_PRICE = 16
    YELLOW_PRICE = 16   #prices
    BLUE_PRICE = 22
    MAX_PURPLE = 10
    MAX_YELLOW = 15     #max orders
    MAX_BLUE = 20
    DONATION_RATE = 0.01
                        #begin initializing accumulator variables
    purNum = 0
    yelNum = 0          #type numbers
    bluNum = 0
    purCharge = 0
    yelCharge = 0       #type charges
    bluCharge = 0
    totNum = 0          #total number and charge
    totCharge = 0

    num = 0             #initializing parameters and extra variables
    num1 = 0
    price = 0
    tax = 0             
    rest = 0            #for buymore function
    donation = 0
    
    def displayMenu():
        print("Welcome to Cool T-shirts!")
        print('''Purple(A) - $16.00
Yellow(B) - $16.00
Blue(C) - $22.00''')
    def getCustomerChoice():
        choice = input("What T-shirt would you like?(A,B, or C): ")
        while choice != 'A' and choice != 'B' and choice != 'C':  #validation loop
            print('Invalid choice. Please select either A, B, or C')
            choice = input("What T-shirt would you like?(A,B, or C): ")
        return choice       #return variable(shirt color)
    def getTShirtNumber(max):
        tNum = int(input('How many T shirts would you like?: '))  #prompt
        while tNum < 1:  #validation loop - one if/else decision structure
            print('Invalid number entered; Please enter a positive, nonzero integer.')
            tNum = int(input('How many T shirts would you like?: '))
        if tNum > max:
            print('You can only order', max, 'of this type of shirt. Please try again')
            tNum = int(input('How many T shirts would you like?: '))
            return tNum
        else:
            return tNum
    def calculateCharge(price,tax,num):
        charge = price*num*(1+tax)
        return charge
    def buymore(num1):
        if num1 < 5:
            rest = 5 - num1
            print('If you buy', rest, 'more, you will qualify for a free key-chain')
        else:
            print('Yay! you will receive a free key-chain!')
    loop = 'Y'
    while loop == 'Y' or loop == 'y':
        displayMenu()
        choice = getCustomerChoice()
        if choice == 'A':
            orderNum = getTShirtNumber(MAX_PURPLE)
            charge = calculateCharge(PURPLE_PRICE,TAX,orderNum)
            purNum = purNum + orderNum
            purCharge = purCharge + charge
            totNum = totNum + orderNum
            totCharge = totCharge + charge
            print('You have ordered', totNum, 'shirts')
        elif choice == 'B':
            orderNum = getTShirtNumber(MAX_YELLOW)
            charge = calculateCharge(YELLOW_PRICE,TAX,orderNum)
            yelNum = yelNum + orderNum
            yelCharge = yelCharge + charge
            totNum = totNum + orderNum
            totCharge = totCharge + charge
            print('You have ordered', totNum, 'shirts')
        else:
            orderNum = getTShirtNumber(MAX_BLUE)
            charge = calculateCharge(BLUE_PRICE,TAX,orderNum)
            bluNum = bluNum + orderNum
            bluCharge = bluCharge + charge
            totNum = totNum + orderNum
            totCharge = totCharge + charge
            print('You have ordered', totNum, 'shirts')
        buymore(totNum)
        loop = input('Would you like to continue shopping?(Y or y for yes): ')
    print("Sales Summary")
    print('Purple: ', purNum, ' $', format(purCharge,'.2f'), sep='')
    print('Yellow: ', yelNum, ' $', format(yelCharge,'.2f'), sep='')
    print('Blue: ', bluNum, ' $', format(bluCharge,'.2f'), sep='')
    print('Total: ', totNum, ' $', format(totCharge,'.2f'), sep='')
    print()
    donation = DONATION_RATE*(totCharge/(1+TAX))
    print('Thank you for your purchase! we will donate $', format(donation,'.2f'), ' to Food for the Poor',sep='')

main()
    
