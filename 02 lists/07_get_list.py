def main():
    lst = []  # Make an empty list to store the values

    val = input("Enter a value: ")  # Get the first value
    while val:  # Keep asking as long as user doesn't press enter
        lst.append(val)  # Add value to the list
        val = input("Enter a value: ")  # Ask again

    print("Here's the list:", lst)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
