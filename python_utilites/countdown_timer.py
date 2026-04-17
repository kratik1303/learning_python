import time 
import winsound

while True :
    try:
        seconds = int (input("⏱️ Please enter a time you want me to take a countdown....."))
        if(seconds<1):
            print("Pls enter a number greater than 1 .....")
            continue
        break
    except ValueError :
        print("Pls enter a whole number!!...")
        
print("\n ⏳ Timer Started...!!!!...")

for remaining in range(seconds,-1,-1) :
    mins,secs = divmod(remaining,60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"Time left:{time_format}",end="\r")
    time.sleep(1)

print("\n Time's up little buddy !!!! Do what u enjoyy ")
# print(\a)
#             frequency,time
winsound.Beep(1000, 2000)