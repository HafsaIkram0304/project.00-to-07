def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers

    # Loop through each index and double the element
    for i in range(len(numbers)):
        numbers[i] *= 2  # Multiply each element by 2

    print(numbers)  # Print the updated list

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
