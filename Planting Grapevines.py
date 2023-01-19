#Katie Meuer, Planting Grapevines, 1/19/2023
#Create input variables for different lengths and amounts of space
#Input variables into equation
#Print

#Input Variables
Length = float(input(f'How long is your row in feet? '))
End_Post = float(input(f'How much space does your end-post assembly occupy? '))
BTVine_Space = float(input(f'How much space in feetdo you want between grapevines? '))

#Equation
V_Number = (Length - 2 * End_Post)/BTVine_Space

#Print
print(f'You will be able to fit {V_Number:,.2f} grapevines in each row. ')