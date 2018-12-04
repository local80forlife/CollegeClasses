#Andrew Barton: CSC 110 Wk 5 Homework - 10/25/18
#Pete's pizza palace program takes user input form the size of the pizza and how
#many pizza's wanted. The program will calculate the total price with current
#deal going on and sales tax at 10.1%

#Global Constants
SALESTAX = .101
DISCOUNT = .10
SMALL = 8.99
MEDIUM = 14.99
MED_SECOND = 7.99
LARGE = 24.99

#Ask user for Size of the pizza and how many, based on size send to appropriate
#function to perform calculations. Functions will return price and send to Taxes
def main():
    print("Welcome to Pete's Pizza Palace")
    print("Please enter the size you would like")
    
    size = input("'s' for Small, 'm' for Medium, or 'l' for Large: ")
    size = size.upper()
    
    #test for correct pizza size
    if size == 'S' or size == 'M' or size == 'L':
        
        quantity = int(input("How many Pizza(s) would you like to order: "))

        #this case will prevent a invalid number from being calculated 
        if quantity < 1:
            print("You have entered an invalid number. Please try again")
        
        elif size == 'L':
            pizzaCost = large(quantity)
            taxCost = tax(pizzaCost)
            total = pizzaCost + taxCost
            return printOutput("Large", quantity, pizzaCost, taxCost, total)

        elif size == 'M':
            pizzaCost = medium(quantity)
            taxCost = tax(pizzaCost)
            total = pizzaCost + taxCost
            return printOutput("Medium", quantity, pizzaCost, taxCost, total)

        elif size == 'S':
            pizzaCost = large(quantity)
            taxCost = tax(pizzaCost)
            total = pizzaCost + taxCost
            return printOutput("Small", quantity, pizzaCost, taxCost, total)

    else:
        print("You entered an invalid size, please restart and try again")

#This function will take in how many Large pizza's the user wants and calculates
#the price without tax. If user wants more then 3 pizza's apply a 10% discount
def large(amount):
    sub_total = amount * LARGE
    if amount >= 3:
        discount = sub_total * DISCOUNT
        total = sub_total - discount
        return total
    else:
        return sub_total

#calculate the price for medium size pizzas with a 'buy 1 get 2nd half off' deal
def medium(amount):
    twoPizzaCal = amount // 2
    fullPricePizza = twoPizzaCal * MEDIUM
    halfPricePizza = twoPizzaCal * MED_SECOND
    #if there is an odd number of pizza's we will calculate the extra here
    extraPizzaCal = amount % 2
    extraPizzaPrice = extraPizzaCal * MEDIUM
    sub_total = fullPricePizza + halfPricePizza + extraPizzaPrice
    return sub_total
    
#small pizza's don't have a deal going on, just calculate and return
def small(amount):
    sub_total = amount * SMALL
    return sub_total

#This calculate the sales tax but doesn't add it to the price
def tax(price):
    return price * SALESTAX

#This funtion deals only with output
def printOutput(size, amount, price, taxes, total):
    price = '{:.2f}'.format(price)
    taxes = '{:.2f}'.format(taxes)
    total = '{:.2f}'.format(total)
    print("You asked for " + str(amount) + " " + size + " Pizza(s)")
    print("Sub Total: $" + str(price))
    print("Taxes: $" + str(taxes))
    print("Total: $" + str(total))

main()

#TEST 1: Size 'l'; Quantity 5; subtotal 112.45; taxes 11.36; total 123.81
#TEST 2: Size 'M'; Quantity 7; subtotal 83.93; taxes 8.48; total 92.41
#TEST 3: Size 'S'; Quantity -4; Error message
#TEST 4: Size 'w'; Error message

#started this assignment writing the function names first, then started to
#define main() with input for a large pizza, then wrote the function to handle
#the large pizza calculations. Once large was good i copied the format for the
#next two sizes.For a short while I got stuck with the 'else' statement always
#printing at the end with an 'if' statement but I read up on the 'elif' and went
#with that and it worked out great.

#I tested the cases above on paper then sent them through the program to make
#sure my algorithm was correct. Everything worked out well, I think the next
#step I should fix is testing for 'null' in case the user doesn't enter anything

#I learned that the 'elif' is very important for the correct flow of the program
#when dealing with mulitple logic cases. I think next time I would also print
#the amount you saved from the deals going on like "You saved: $xx.xx"
