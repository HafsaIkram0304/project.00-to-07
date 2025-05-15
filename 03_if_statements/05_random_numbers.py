import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")
    print()  # for a clean newline at the end

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()

