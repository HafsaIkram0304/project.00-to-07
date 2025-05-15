def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Continue doubling the number until it's 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# This is required to execute the program.
if __name__ == '__main__':
    main()
