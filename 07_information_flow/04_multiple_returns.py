def get_user_info():
    # Asking user for their first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Returning the data as a tuple
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    # Call the get_user_info function to collect data
    user_data = get_user_info()
    
    # Print the returned data in a readable format
    print("Received the following user data:", user_data)

# This is the entry point of the program
if __name__ == "__main__":
    main()
