ADULT_AGE = 18  # U.S. legal adult age

def is_adult(age: int):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    return False

########## No need to edit code beyond this point :) ##########

def main():
    # Prompt the user for the person's age
    age = int(input("How old is this person?: "))
    # Call the is_adult function and print the result
    print(is_adult(age))

if __name__ == "__main__":
    main()
