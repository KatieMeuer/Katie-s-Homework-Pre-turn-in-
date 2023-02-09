#Katie Meuer, Item Counter, 2/9/2023
def main():
    #Open names.txt
    open_file = open('names.txt', 'r')
    #Create object counter
    counter = open_file.readline()
    #variable to keep track of # of lines
    count = 0

    #Count lines
    while counter != '':
        counter = open_file.readline()
        count += 1


    print(f' There are {count} names in this file.')

    open_file.close()

if __name__ == '__main__':
    main()

