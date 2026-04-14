import datetime

entry = input ("What did you learn today? ").strip()
rating = input("rate your productivity today (1-5,optional)...").strip()

now = datetime.datetime.now()
# print(now)
date_str = now.strftime("%Y-%m-%d -%I:%M %p")
# print(date_str)

journal_entry = f'\n 📆{date_str}\n {entry}'

if rating :
    journal_entry += f"\n ⭐Productive rating : {rating}"

journal_entry += "\n"+"--"*50

# print(journal_entry)

with open ("learning_journal.txt","a",encoding="UTF-8") as f:
    f.write(journal_entry)

print(f"\n Your journal entry has been saved to 'learning_journal.txt' file ")
