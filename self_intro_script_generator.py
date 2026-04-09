import datetime

name = input ("What is your name ? ").strip()
age = input ("How old are you ? ").strip()
city = input ("Which city do you live in ? ").strip()
profession = input ("What is your profession ? ").strip()
# hobby = input ("What is your favourite hobby ? ").strip()
hobbies=[]
while True:
    hobby = input("What is your fav hobby ?").strip()
    if hobby.lower() == "done":
        break
    hobbies.append(hobby)

intro_msg = ( 
            f"Hello my name is {name}, I am {age} years old and live in {city}. "
            f"I work as a {profession} and I absolutely enjoy {', '.join(hobbies)} in my free time. "
            f"Nice to meet you\n"
            )
current_date = datetime.date.today().isoformat()
intro_msg += f"Logged on : {current_date} "
border = "*" * 80
final_output = f"{border}\n {intro_msg}\n {border}"
print(f"\n"+final_output)