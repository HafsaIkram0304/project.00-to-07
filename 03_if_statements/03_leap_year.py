def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check the conditions for a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
