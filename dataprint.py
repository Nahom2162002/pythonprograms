def userfile(filename): 
    file_choice = open(filename)
    print(file_choice.read())
    file_choice.close()

def main():
    filename = input("Which file would you like to print?")
    userfile(filename)

if __name__ == '__main__':
    main()