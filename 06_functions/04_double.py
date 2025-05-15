def double(num: int):
    # This function doubles the input number
    return num * 2

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    
    # Call double function and store the result
    num_times_2 = double(num)
    
    # Output the result
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
