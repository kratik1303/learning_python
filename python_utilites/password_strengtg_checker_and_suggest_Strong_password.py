import string
import random
import getpass

def check_password_strength(password) :
    issues = [ ]
    
    if (len(password) < 8 ) :
        issues.append("Min length of a password is 8 ")
    if not any (c.islower() for c in password):
        issues.append("Atleast one lowercase letter!!! ")
    if not any (c.isupper() for c in password):
        issues.append("Atleast one upperCase letter ")
    if not any (c.isdigit() for c in password):
        issues.append("Atleast one digit ")
    if not any(c in string.punctuation for c in password) :
        issues.append("Missing a special character ")
    return issues 

def generate_strong_password(length = 12 ) :
    chars = string.ascii_letters + string.digits + string.punctuation 
    return ''.join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter a password pls !!")
issues = check_password_strength(password)
suggestion = generate_strong_password()

if not issues :
    print("Your password is pretty strong \n")
else :
    print("Your password is weak \n")
    for issue in issues :
        print(f"-{issue}")
    print (" \nSuggesting a strong password\n ")
    print (suggestion)