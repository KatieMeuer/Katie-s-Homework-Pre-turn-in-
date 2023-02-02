#Katie Meuer, Stadium Seating, 2/2/2023
#Create variables for three types of seating
#creat total variable and print it

#Variables
Class_A = int(input('How many tickets for class A seats were sold?')) * 20
Class_B = int(input('How many tickets for class B seats were sold?')) * 15
Class_C = int(input('How many tickets for class C seats were sold?')) * 10

#Total variable
ticket_total = Class_A + Class_B + Class_C
print(f'The total amount sold in tickets is ${ticket_total}')


#So that user can keep viewing code until clicking enter
input()