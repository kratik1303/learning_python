import textwrap

name = input("What is your name? ").strip()
profession = input("What is your profession? ").strip()
passion = input("What is your passion? ").strip()
emoji = input("What is your favorite emoji? ").strip() or "👍"
website = input("What is your website or portfolio link? ").strip() or "N/A"

print ("\n Choose your preferred style for the bio:")
print("1. Simple lines")
print("2. Verical flairs")
print ("3. Emoji Sandwich")


style = input("Enter the number corresponding to your preferred style: ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession}\n 🔥{passion}\n 🔥{website}\n"
    if style == "2":
        return f"{emoji} {name}\n {profession}\n 🔥{passion}\n 🔥{website}\n"
    if style == "3":
        return f"{emoji*3} {name}\n {profession}\n 🔥{passion}\n 🔥{website}\n {emoji*3} 🔥"
    
bio = generate_bio(style)
print("Your stylish bio : \n")
print("*"*30)
print(textwrap.dedent(bio))
print("*"*30)

save = input("Do u want to save this bio into a txt file ? (y/n)").strip().lower()

if save =='y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open (filename,'w',encoding = 'utf-8') as f:
        f.write(bio)
    print("Bio saved successfully as " + filename)
    
    