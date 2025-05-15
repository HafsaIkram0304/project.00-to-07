def add_three_copies(my_list, data):
    """
    Adds three copies of `data` to `my_list`.
    Notice: We do not return anything because lists are mutable!
    """
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
