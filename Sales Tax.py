#Katie Meuer, Sales Tax, 1/19/2023
#Create input for users to type total
#Creat varaibles for sales tax and country tax
#Calculate sales and country tax on total
#Print tax
#Add tax to total
#Print total with tax

#Subtotal variable
SubTotal = float(input("What is the total of your purchase?"))
#STate and Country tax
StateT = SubTotal * 0.05
CountryT = SubTotal * 0.025
#Total Tax
TotalT = StateT + CountryT
#Print commands
print(f'Subtotal: {SubTotal}.')
print(f'State tax: {StateT:,.2f}')
print(f'Country tax: {CountryT:,.2f}')
print(f'Total tax: {TotalT:,.2f}.')
#Total with subtotal and tax
Total = SubTotal + TotalT
print(f'Your total is {Total:,.2f}.')
