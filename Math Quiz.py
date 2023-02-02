#Katie Meuer, Math Quiz, 2/2/2023

#Random
import random

#Number 1 and 2 randoms
number_1 = random.randint(10, 1000)
number_2 = random.randint(10, 1000)

#calculate Total variables
total = number_1 + number_2

def main():
    Formatting()
    User_Input()

#Print numbers and instructions with if formatting so that the numbers will align correctly
def Formatting():
    print('Add the two numbers')

    if number_1 <= 99:
        print(f'      {number_1}')
    else:
        print(f'     {number_1}')

    if number_2 <= 99:
        print(f'     +{number_2}')
    else:
        print(f'    +{number_2}')


#User input and message whether correct or incorrect
def User_Input():
    total_input = int(input('     '))
    if total_input == total:
        print('Yay!')
    else:
        print('Nope')

main()
input()