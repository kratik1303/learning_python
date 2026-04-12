def calculate_mins(age_in_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINS_IN_HOUR = 60
    
    total_days = age_in_years * DAYS_IN_YEAR
    total_hrs = HOURS_IN_DAY * total_days
    total_mns = MINS_IN_HOUR * total_hrs
    
    return round(total_days), round(total_hrs) , round(total_mns)

while True:
    try:
        age = float(input("Enter your age in years->"))
        days,hours,mins = calculate_mins(age)
        
        print("\n You are apporximately : ")
        print(f"--{days:,} days old")
        print(f"--{hours:,} hours old")
        print(f"--{mins:,} mins old")

        again = input ("WOuld you like to try it again (y/n)??").strip().lower()
        
        if again !='y':
            print("Saionara!!")
            break
        
    except:
        print("Pls eneter a correct age !!!")    
    
    