#Katie Meuer, Miles-per-Gallon, 1/19/2023
#Ast user miles traveled and gallons used
#Create equation
#Print results

Miles = float(input(f'How many miles did you drive?'))
Gallons = float(input('How many gallons of gas did you use?'))
MPG = Miles / Gallons
print(f'Traveling {Miles} miles with {Gallons} gallons')
print(f'means that your MPG are {MPG:,.2f}.')