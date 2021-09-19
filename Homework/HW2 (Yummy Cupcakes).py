#HW2 (Yummy Cupcakes)
#Make sure to use nested if/else statements(within elif)
#all constants are UPPERCASE
#the else statement at bottom of elif chain is to catch invalid entries

MAGPRICE = 2.5
DELPRICE = 2.8          #named constants
STRAWPRICE = 4
TAX = 0.075
DISCRATE = 0.075        # discount for strawberry cupcakes 

magNum = 0          #initializing variables
delNum = 0          #Num variables are for order numbers
strawNum = 0
order = 0
preorder = 0        #others are to store arithmetic expressions
discount = 0

loop_again = 'y'
while loop_again == 'y':                    #start of loop
    print('''Welcome to Yummy Cupcake (YC)
    ==============================
    Magic Cupcake (M or m)
    Delicious Chocolate Cupcake (D or d)   
    Strawberry Walnut Cupcake (S or s)''')                  #welcome statement
    cupType = input("Please enter your preferred cupcake: ")
    if cupType == 'M' or cupType == 'm':                    #beginning of magic cupcake order process
        magNum = int(input('How many Magic cupcakes would you like? '))
        if magNum > 0 and magNum < 5:
            order = magNum * MAGPRICE * (1+TAX)         #condition for valid order
            print('The total price for ', magNum, ' Magic cupcake(s) is $', format(order,'.2f'), sep='')
        elif magNum >= 5:
            print('You cannot order more than four Magic cupcakes.')        #condition for too many magic
        else:
            print('You have entered a negative number or zero, no transaction will be conducted.')      #condition for zero or negative magic
            
    elif cupType == 'D' or cupType == 'd':      #beginning of delicious cupcake order process
        delNum = int(input('How many Delicious cupcakes would you like? '))
        if delNum > 0 and delNum < 5:
            order = delNum * DELPRICE * (1+TAX)         #condition for valid order
            print('The total price for ', delNum, ' Delicious cupcake(s) is $', format(order,'.2f'), sep='')
        elif magNum >= 5:
            print('You cannot order more than four Delicious cupcakes.')        #condition for too many delicious
        else:
            print('You have entered a negative number or zero, no transaction will be conducted.')     #condition for zero/negative delicious

    elif cupType == 'S' or cupType == 's':      #beginning of strawberry order process
        strawNum = int(input('How many Strawberry Walnut cupcakes would you like? '))
        if strawNum > 0 and strawNum < 4:
            order = strawNum * STRAWPRICE * (1+TAX)
            print('The total price for ', strawNum, ' Strawberry cupcake(s) is $', format(order,'.2f'), sep='') #condition for valid order less than four
            print('The number of cupcakes is less than four, so no discount will be applied.')
        elif strawNum >=4 and strawNum < 21:
            preorder = strawNum * STRAWPRICE * (1+TAX)          #condition for valid order greater than or equal to four
            print('The total price for ', strawNum, ' Strawberry cupcake(s) is $', format(preorder,'.2f'), sep='')
            discount = (strawNum * STRAWPRICE) * DISCRATE           #calculating discount value
            print('The discount amount is $', format(discount,'.2f'), sep='') 
            order = ((strawNum * STRAWPRICE) - discount) * (1+TAX)      #calculating order after discount is applied
            print('The total price after discount is $', format(order,'.2f'), sep='')
        elif strawNum >= 21:
            print('You cannot order more than 20 Strawberry walnut cupcakes')       #condition for too many strawberry cupcakes
        else:
            print('You have entered a negative number or zero, no transaction will be conducted.')  #condition for zero/negative strawberry cupcakes
        
    else:
        print('You have entered an invalid cupcake type. Try again')    #condition for invalid cupcake choice


    loop_again = input ("\nDo you want to loop again? (y to loop again): ")     #prompt to restart the loop
    
