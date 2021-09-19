# Name: Peter Dauenhauer
# Assignment Number: 3
# Date: 9/27/19
# 9:30-11
# This program is created for the proprietor of a donut shop to track her inventory and number of donuts sold throughout a day
# it can also give her a summary of the profits earned at the end of the day

PINEPRICE = 2.4
FIGPRICE = 4
PINEMARGIN = .12        #named constants - prices and profit margins
FIGMARGIN = .25

pineOrder = 0
figOrder = 0            #individual order amounts
inventoryP = 500
inventoryF = 500        #cumulative inventories
soldP = 0
soldF = 0               #cumulative totals sold
totalSold = 0
pineProfit = 0
figProfit = 0           #profits for business report
totalProfit = 0

loopAgain = 'y'
while loopAgain == 'y' or loopAgain == 'Y':         #outer loop
    
    print('''Welcome to Delicious Fruity Donuts
    ==================================
    P or p - Pineapple Donut ($2.40)
    F or f - Fig Donut ($4.00)''')                  #welcome message
    donutType = input('What donut does the customer want?: ')
    if donutType == 'P' or donutType == 'p':                #begin condition for pineapple donuts
        pineOrder = int(input('How many pineapple donuts would they like?: '))
        while pineOrder < 0:            #validation loop
            print('You have entered an invalid number. Try again.')
            pineOrder = int(input('How many pineapple donuts would they like?: '))
        if pineOrder <= inventoryP:         #condition for valid order amount
            soldP = soldP + pineOrder
            inventoryP = inventoryP - pineOrder         #keeping track of inventory
            print('You have sold', pineOrder, 'pineapple donuts')
        else:               #condition for excess order amount
            print('You dont have enough donuts for that order!')
            print('You only have', inventoryP, 'pineapple donuts in stock.')
    elif donutType == 'F' or donutType == 'f':              #begin condition for fig donuts
        figOrder = int(input('How many fig donuts would they like?: '))
        while figOrder < 0:             #validation loop
            print('You have entered an invalid number. Try again.')
            figOrder = int(input('How many fig donuts would they like?: '))
        if figOrder <= inventoryF:          #condition for valid order amount
            soldF = soldF + figOrder
            inventoryF = inventoryF - figOrder      #keeping track of inventory
            print('You have sold', figOrder, 'fig donuts')
        else:               #condition for excess order amount
            print('You dont have enough donuts for that order!')
            print('You only have', inventoryF, 'fig donuts in stock.')
    else:                                           #condition for invalid donut type entered
        print('You have entered an invalid letter.')
    print('Do you want to make another sale?')
    loopAgain = input('Enter Y or y for yes and any other letter to quit: ')        #prompt to loop again
print('Business report for Mrs. Donu')      #beginning of business report(outside loop)
print('You have sold', soldP, 'pineapple donut(s).')
print('You have sold', soldF, 'fig donut(s).')
totalSold = soldP + soldF               #calculating total donuts sold
print('You have sold', totalSold, 'total donut(s).')
pineProfit = (soldP * PINEPRICE) * PINEMARGIN
figProfit = (soldF * FIGPRICE) * FIGMARGIN          #calculating specific profits
print('Your profit for pineapple donuts is $', format(pineProfit,'.2f'), sep='')
print('Your profit for fig donuts is $', format(figProfit,'.2f'), sep='')
totalProfit = pineProfit + figProfit            #calculating total profit
print('Your total profit is $', format(totalProfit,'.2f'), sep='')


    
    

