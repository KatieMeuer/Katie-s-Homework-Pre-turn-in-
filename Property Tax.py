#Katie Meuer, Property Tax, 2/2/2023
#Three functions
#1 - get input for value of property
#2 - assess assessment value and return that value, print value
#3 - assess tax, return value, print value
#call main function

#Main - calls assessment_value and tax
def main():
    assessment_value()
    tax()

#Prints assessment
def assessment_value():
    print(f'Your assessment value is ${assessment}.')

#calculates tax and prints it
def tax():
    property_tax1 = 0.72 * assessment
    property_tax2 = property_tax1 / 100
    print(f'Your property tax is ${property_tax2:,.2f}.')

#Variables for property value and assessment value
property_value = int(input('Enter the value of your property: '))
assessment = property_value * 0.60

main()

#Allows program to remain running until user presses enter
input()