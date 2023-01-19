#Katie Meuer, Tip, Tax, and Total, 1/19/2023
#Create variable for how much user spent
#Create variable for tax with 18% times spending
#Create variable for 7% sales times total
#Create variable for total plus tax and tip
#print it all

#Create variable for how much user spent
Meal_Cost = float(input(f'How much did your meal cost? '))
#Create variable for tip with 18% times spending
Tip = Meal_Cost * 0.18
#Create variable for 7% sales times spending
Tax = Meal_Cost * 0.07
#Create variable for total plus tax and tip
Total = Meal_Cost + Tip + Tax
#print it all
print(f'Meal cost: {Meal_Cost}.')
print(f'Tip: {Tip:,.2f}.')
print(f'Tax: {Tax:,.2f}.')
print(f'Total: {Total:,.2f}.')