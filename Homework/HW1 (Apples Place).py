MAC_PRICE = 2           #named constants
RED_PRICE = 2.5         #Prices, red is Red Delicious, mac is macintosh
FUJI_PRICE = 2.8
PROFIT_MARGIN = 0.38
TAX = 0.08              #sales tax rate

mac_order = 0           #initializing variables
red_order = 0           #order variables represent number of apples requested by customer
fuji_order = 0
total_apples = 0
mac_charge = 0
red_charge = 0          #all the charges for individual apple types
fuji_charge = 0
revenue = 0
order_charge = 0        #charge for full order 
profit = 0

print("Welcome to Apples Place! What can we get for you today?") #welcome message
print("############################################################")
print('''Macintosh -- $2.00
Red Delicious -- $2.50                         
Fuji -- $2.80''')               #menu items
print()
customer = input("What is the customer's name?: ")            #beginning of prompts
mac_order = int(input("How many Macintosh apples would you like?: "))
red_order = int(input("How many Red Delicious apples would you like?: "))
fuji_order = int(input("How many Fuji apples would you like?: "))
total_apples = mac_order + red_order + fuji_order       #defining total_apples
mac_charge = mac_order*MAC_PRICE
red_charge = red_order*RED_PRICE        #defining charge variables
fuji_charge = fuji_order*FUJI_PRICE
print()             #blank line
print('''Transaction Report
*****************''')           #report heading
print('Coustomer name:', customer)
print('Macintosh:', mac_order)              #types of apples ordered
print('Red Delicious:', red_order)
print('Fuji:', fuji_order)
print('The charge for Macintosh apples is $', format(mac_charge,'.2f'), sep='')     #charge statements
print('The charge for Red Delicious apples is $', format(red_charge,'.2f'), sep='')
print('The charge for Fuji apples is $', format(fuji_charge,'.2f'), sep='')
print('The total apples ordered is', total_apples)      #stating apple total
revenue = mac_charge + red_charge + fuji_charge         #defining revenue and order_charge variables
order_charge = revenue * (1 + TAX)
print('The total charge for all apples is $', format(order_charge,'.2f'), sep='') #total order charge including tax
print('The total revenue for the order is $', format(revenue,'.2f'), sep='')
profit = revenue * PROFIT_MARGIN        #defining profit
print('The total profit for the order is $', format(profit,'.2f'), sep='')




                                                     
      
