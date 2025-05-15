def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b.
    """
    sum = a + b
    return sum / 2

def main():
    # Example averages
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Final average of the two averages
    final = average(avg_1, avg_2)
    
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This is required to execute the program.
if __name__ == '__main__':
    main()
