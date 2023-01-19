#Katie Meuer, Male and Female Percentages, 1/19/2023
#write input variables for number of males and females in class
#Create variable for total number of students
#Create percentage of male by multiplying males * total
#Create percentage of females by multipyling females * total
#Print

#write input variables for number of males and females in class
Males = int(input('How many males are in the class? '))
Females = int(input('How many females are in the class? '))


#Create variable for total number of students
Total = Males + Females

#Create percentage of male by multiplying males * total

Male_Percent = Males/Total
#Create percentage of females by multipyling females * total
Female_Percent = Females/Total

#Print
print(f'For a class with {Total} people, comprised of {Males} males,')
print(f'and {Females} females,')
print(f'the class is {Male_Percent:.2f} percent male and {Female_Percent:,.2f} percent female.')