def get_float(prompt):
    while True:
        try:            
            return float(input(prompt))
        except ValueError:
            print("❌❌Pls enter the correct value: \n")
    

num_people= int(input("How many people are there in the group?"))
names = [ ]

for i in range (num_people):
    name = input(f"Enter the name of person #{i+1}").strip()
    names.append(name)
    
total_bill=get_float("What is the total amount of the bill?? ")

share = round(total_bill/num_people,2)

print ("\n"+"**"*40+"\n")
print(f"The total bill amount is {total_bill}\n")
print(f"Each person owes a bill of :{share}\n")

for name in names :
    print(f"Hey, {name} owes a bill of {share}\n" )
    
print ("\n"+"**"*40+"\n")


