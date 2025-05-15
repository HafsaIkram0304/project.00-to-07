def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")
    
    # Call num_in_stock to check how many of that fruit are in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print the corresponding message
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This function returns the number of fruit Sophia has in stock
def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # If the fruit is not in stock, return 0
        return 0

# Entry point of the program
if __name__ == '__main__':
    main()
