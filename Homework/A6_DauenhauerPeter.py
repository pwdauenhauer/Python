#Name: Peter Dauenhauer
#Assignment #6
#Date: 11/1/19
#Section: MW 9:30-11
#This is a program to read from a file of product information and organize it
#into both one and two dimensional lists for processing and reporting

NUMFIELD = 5    #global constant variable used for several functions

def prodReport(oneDim):     #defining report function with one dimensional list as argument
    count = 0
    for item in oneDim:     #for loop to report each list item
        print(oneDim[count])
        count = count + 1
    revenue = oneDim[2] * oneDim[4] #calculating revenue and profit
    profit = revenue * oneDim[3]
    print('Revenue: $', format(revenue,'.2f'), sep='') #reporting revenue and profit
    print('Profit Amount: $', format(profit,'.2f'), sep='')
    print()

def printTwoDim(list2, rows): #defining print function with two dimensional list and row amount as arguments
    for row in range(rows):
        for col in range(NUMFIELD): #double for loops - using NUMFIELD as range 
            print(list2[row][col])
        print()
    

def main():  #defining main()
    
    productID = ''
    name = ''
    price = 0       #initializing all variables within main()
    profitMargin = 0
    quantity = 0
    try:            #try suite for opening file
        prodFile = open('HW6_FILE.txt', 'r')
    except IOError:             #handling IOError if file can't be opened/read
        print('Sorry, an error occurred while trying to read this file')
    productID = prodFile.readline().rstrip('\n')
    twoDim = []             #declaring two dimensional empty list

    while productID != '':          #beginning while loop
        prodList = []               #declaring one dimensional empty list
        prodList.append(productID)
        name = str(prodFile.readline().rstrip('\n'))
        prodList.append(name)
        price = float(prodFile.readline())          #reading and appending each value of the file to one dimenisonal list
        prodList.append(price)
        profitMargin = float(prodFile.readline())
        prodList.append(profitMargin)
        quantity = int(prodFile.readline())
        prodList.append(quantity)
        productID = str(prodFile.readline().rstrip('\n'))
        twoDim.append(prodList)
        maxRow = len(twoDim)        #defining maxRow for # of rows in two dimensional list
        prodReport(prodList)        #calling report function using prodList as the argument

    print('Content of two dimensional list:')
    printTwoDim(twoDim, maxRow)         # calling the print function using twoDim and maxRow as the arguments
    
        
main()      #call main()
