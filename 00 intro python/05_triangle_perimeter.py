def main():
    side1 = float(input("\033[1;3m Enter the length of side 01:\033m "))
    side2 = float(input("\033[1;3m Enter the length of side 02:\033m "))
    side3 = float(input("\033[1;3m Enter the length of side 03:\033m "))

    perimeter = side1 + side2 + side3

    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()
