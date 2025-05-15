DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINT_PER_HOUR = 60
SEC_PER_MINT =  60

def main():
    
    total_seconds = DAYS_IN_YEAR * HOURS_IN_DAY * MINT_PER_HOUR *SEC_PER_MINT
    print(f"there are {total_seconds} in a year")
    
if __name__ == '__main__':
    main()
    
