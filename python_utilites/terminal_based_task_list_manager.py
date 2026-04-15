import os 
TASK_FILE = 'tasks.txt'

def load_tasks():
    tasks=[]
    if (os.path.exists(TASK_FILE)) :
        with open (TASK_FILE,'r',encoding='UTF-8') as f :
            for line in f :
                text,status = line.strip().rsplit("||",1)
                tasks.append({"text":text,"done":status=='done'})
    return tasks 
            
    
    
def save_tasks(tasks):
    # pass
    with open (TASK_FILE,'w',encoding='UTF-8') as f :
        for task in tasks :
            status = 'done' if task['done'] else 'not_done'
            f.write(f"{task['text']} || {status} \n ")
        
def display_tasks(tasks):
    # pass
    if not tasks :
        print (f"No tasks found!!!")
    else :
        for i , task in enumerate( tasks , 1) :
            checkbox = '☑️' if task['done'] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()
           

def task_manager():
    tasks = load_tasks()
    
    while True:
        print('\n------ Task List Manager  -------')
        print('1. Add task')
        print('2. Display tasks')
        print('3. Mark task as completed')
        print('4. Delete a task')
        print('5. Exit')
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            text = input("Enter your task: ").strip()
            if text:
                tasks.append({'text': text, 'done': False})
                save_tasks(tasks)
            else:
                print("Enter a valid task")
            
        elif choice == "2":
            display_tasks(tasks)
                
        elif choice == "3":
            display_tasks(tasks)
            try:
                num = int(input('Enter task number: '))
                if 1 <= num <= len(tasks):
                    tasks[num-1]['done'] = True
                    save_tasks(tasks)
                    print("Task marked as done ✅")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")
                    
        elif choice == "4":
            display_tasks(tasks)
            try:
                num = int(input('Enter task number: '))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed['text']}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")
            
        elif choice == "5":
            print("Exiting task manager 👋")
            break
        
        else:
            print("Please enter correct value")

task_manager()