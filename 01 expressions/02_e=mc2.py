C: int = 299792458  # The speed of light in m/s

def main():
    while True:
        try:
            mass_in_kg: float = float(input("Enter kilos of mass (or type -1 to quit): "))
            
            if mass_in_kg == -1:
                print("Goodbye!")
                break

            # Calculate energy
            energy_in_joules: float = mass_in_kg * (C ** 2)

            # Display work to the user
            print("e = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(str(energy_in_joules) + " joules of energy!\n")

        except ValueError:
            print("Please enter a valid number!\n")


# This provided line is required at the end of the Python file to call main()
if __name__ == '__main__':
    main()
