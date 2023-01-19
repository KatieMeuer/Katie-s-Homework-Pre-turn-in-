#Katie Meuer, Compound Interest, 1/19/2023
#Create unput variables for amount deposited, interest rate,
 #of times per year interest is compouned, and number of years
#Put variables into equation
#Print

#Amount originally deposited
Amount1 = float(input(f'How much money did you deposit into the account? $'))
#INterest rate
Interest_Rate = float(input(f'What is the annual iterest rate of your bank? '))
#Number of times per year compounded
Number_Compounded = float(input(f'How many times per year is the interest compounded '))
#Number of years left in bank
Years = float(input(f'How many years will the account be left in the bank? '))

Amount2 = Amount1 * (1 + Interest_Rate/Number_Compounded)**(Number_Compounded * Years)
print(f'Once your money has been in the bank for {Years} years,')
print(f'you will have ${Amount2:,.2f}.')
