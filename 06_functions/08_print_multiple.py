def print_multiple(message: str, repeats: int):
    for i in range(repeats):  # Loop repeats times
        print(message)  # Print the message in each iteration

def main():
    message = input("Please type a message: ")  # Prompt user for a message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt user for number of repeats
    print_multiple(message, repeats)  # Call function to print the message the specified number of times

if __name__ == '__main__':
    main()
