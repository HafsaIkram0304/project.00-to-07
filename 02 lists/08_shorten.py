MAX_LENGTH : int = 3  # This is the maximum length we want the list to have

def shorten(lst):
    """
    Removes elements from the end of lst, printing each item it removes
    until lst is MAX_LENGTH items long.
    If lst is already shorter than or equal to MAX_LENGTH, it leaves it unchanged.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove and get the last element
        print(last_elem)  # Print the element removed

# There is no need to edit code past this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list of elements from the user
    shorten(lst)  # Call the shorten function to print and modify the list

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
