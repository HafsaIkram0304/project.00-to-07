MAX_TERM_VALUE = 10000  # The maximum value for the Fibonacci terms

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term with a space between each
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
