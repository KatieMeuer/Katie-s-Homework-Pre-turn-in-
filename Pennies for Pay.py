#Katie Meuer, Pennies for Pay, 1/23/2023
#ask customer for number of days they want to calculate
#write for loop that doubles the amount of pennies on each line
#create variable for total pay


#User input
NumofPen = int(input('How many days of pay would you like to calculate? '))


#For loop
for pennies in range (NumofPen + 1):
    daily = 2**pennies
    total = daily + 0
    print(daily)




print(total)