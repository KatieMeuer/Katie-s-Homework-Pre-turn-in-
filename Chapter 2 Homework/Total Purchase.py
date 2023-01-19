#Katie Meuer, Total Purchase, 1/19/2023
#Create input asking customer how much each item was
#Creat variable that adds all the item prices
#Create variable that calculates tax
#Create variable that adds tax to total
#print

ItemPrice1 = float(input("How much money did your first item cost?" ))
ItemPrice2 = float(input("How much money did your second item cost?" ))
ItemPrice3 = float(input("How much money did your third item cost?" ))
ItemPrice4 = float(input("How much money did your fourth item cost?" ))
ItemPrice5 = float(input("How much money did your fifth item cost?" ))

Subtotal = ItemPrice1 + ItemPrice2 + ItemPrice3 + ItemPrice4 + ItemPrice5
print(f'The subtotal of your order is {Subtotal}')
Tax = 0.07 * Subtotal
print(f'Your tax is {Tax:,.2f}')
Total = Subtotal + Tax
print(f'Your total is {Total}')
