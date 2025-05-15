def greet(name):
    # Return a greeting message with the user's name
    return "Greetings " + name + "!"

def main():
    # Ask the user for their name
    name = input("What's your name? ")
    # Call the greet function and print the returned greeting
    print(greet(name))

if __name__ == '__main__':
    main()
