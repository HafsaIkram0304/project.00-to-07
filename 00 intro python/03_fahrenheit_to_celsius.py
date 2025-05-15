def main():
    
    fahrenheit = float(input("\033[1;3m Enter the temperature in fahrenheit \033m"))
    
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    print(f"temperature : {fahrenheit}F = {celsius}C")

if  __name__ == "__main__": main()
