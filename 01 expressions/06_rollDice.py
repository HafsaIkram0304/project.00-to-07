"""
Simulate rolling two dice, and print results of each
roll as well as the total.
"""

# Import the random library to simulate dice rolls
import random

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)

    # Roll the dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate total
    total: int = die1 + die2

    # Print the results
    print(f"Each die has {NUM_SIDES} sides.")
    print(f"First die roll: {die1}")
    print(f"Second die roll: {die2}")
    print(f"Total of two dice: {total}")

# This provided line is required at the end of the file
if __name__ == '__main__':
    main()
