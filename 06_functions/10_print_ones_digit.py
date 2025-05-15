def print_ones_digit(num):
    # Print the ones digit of the number
    print("The ones digit is", num % 10)

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

if __name__ == '__main__':
    main()
