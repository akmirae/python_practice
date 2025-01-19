def display_numbers_from_file():
    try:
        with open("numbers.txt", 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' does not exist.")
    except ValueError:
        print("Error: The file contains invalid data.")
        
display_numbers_from_file()
