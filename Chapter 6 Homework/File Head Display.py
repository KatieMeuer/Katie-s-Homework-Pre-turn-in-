#Katie Meuer, File Head Display, 2/9/2023
#User input to name the file they want
file_name = str(input('Enter the name of a file: '))
#Open user file
file_open = open(file_name, 'r')

#Read and print the lines of code
line = file_open.readline()
print(line)
line = file_open.readline()
print(line)
line = file_open.readline()
print(line)
line = file_open.readline()
print(line)
line = file_open.readline()
print(line)