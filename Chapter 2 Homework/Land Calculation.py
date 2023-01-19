#Katie Meuer, Land Calculation, 1/19/2023
#Creat input variable for square feet
#Creat variable for # of feet / 43,560
#PRINT

#Creat variable for sf
Their_Land = float(input("How many square feet of land do you have? "))
Acres = Their_Land / 43560
print(f'You have {Acres:,.2f} acres of land')
