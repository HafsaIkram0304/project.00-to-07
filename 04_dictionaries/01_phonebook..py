def read_phone_numbers():
    """
    Asks the user for names and numbers to store in a phonebook (dictionary).
    Returns the completed phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names and numbers in the phonebook.
    """
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allows the user to lookup phone numbers by name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
