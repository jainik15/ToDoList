import json
from datetime import datetime

todo_list = [] 

def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(todo_list, file , indent=4)

def loadTasks():
    global todo_list
    try:
        with open("tasks.json", "r") as file:
            todo_list= json.load(file)
    except FileNotFoundError:
        todo_list=[]

def addTask():
    print()
    tname= input("Enter task desciption: ")
    due_date= input("Enter due date: [yyyy-mm-dd]").strip()
    if due_date=="":
        due_date=None
    else:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date, saving due date as none")
            due_date=None
    while True:
        pr= ["high", "mid", "low"]
        priority = input("Choose (High|Mid|Low): ") .strip().lower()
        if priority in pr:
            break
        else:
            print("Enter valid priority")

    task = {"description" : tname.capitalize() , 
            "completed" : False, 
            "due" : due_date, 
            "priority" : priority.capitalize()
            }
    todo_list.append(task)
    saveTasks()
    print("\n Task added successfully")
    

def removeTask():
    if len(todo_list)==0:
        print("List is empty")
        return
    else:
        view_list()
        try:
            task_num = int(input("\n Enter task number to remove: "))
            idx= task_num-1
            if 0<=idx<len(todo_list):
                removed_task = todo_list.pop(idx)
                print("\n '",removed_task["description"],"'", " task removed successfully")
                saveTasks()
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid arguments")

def markTasks():
    if(len(todo_list) ==0 ):
        print("List is empty")
        return
    else:
        view_list()
        try:
            print()
            task_num=int(input("Enter task number to mark: "))
            idx=task_num-1
            if 0<=idx<len(todo_list):
                todo_list[idx]["completed"]=True
                saveTasks()
                print(" \n'",todo_list[idx]["description"],"'", "marked completed successfully")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid arguments")

def editTasks():
    if len(todo_list)==0:
        print("\n List is empty")
        return
    else:
        view_list()
        try:
            editTaskNum= int(input("Enter task number to edit"))
            idx = editTaskNum-1
            if 0<=idx< len(todo_list):
                nDes = input("Enter new description: ").strip()
                if nDes != "":
                    todo_list[idx]["description"]=nDes.capitalize()
                
                nDue = input("Enter new due date: ").strip()
                if nDue == "":
                    pass
                else:
                    try:
                        datetime.strptime(nDue, "%Y-%m-%d")
                        todo_list[idx]["due"]=nDue
                    except ValueError:
                        print("Invalid date! (setting due date as none)")
                        todo_list[idx]["due"]=None
                
                pr =["high","mid","low"]
                npr = input("Enter new priority (high|mid|low): ").strip().lower()
                if npr in pr:
                    todo_list[idx]["priority"]=npr.capitalize()
                else:
                    print("Invalid priority, Not changed!")
                saveTasks()
                print("Task updated successfully")
            else:
                print("\n Invalid task number")
        except ValueError:
                print("Invalid arguments")
    
def view_list():
    if len(todo_list)==0:
        print("\n List is empty")
        return
    else:
        print("-----To Do List-----")
        priority_levels = ["High", "Mid", "Low"]
        task_counter=1
        def sort_date(task):
            if task["due"] == None:
                return datetime.max
            try: 
                return datetime.strptime(task["due"], "%Y-%m-%d")
            except ValueError:
                return datetime.max
        for priority in priority_levels:
            group=[]
            for task in todo_list:
                if priority==task["priority"]:
                    group.append(task)
            if len(group)>0:
                print(f"\n --- {priority.capitalize()} Level---")
                group.sort(key=sort_date)
                for task in group:
                    status = "[x]" if task["completed"]==True else "[ ]"
                    due_date = f'(Due: {task["due"]})' if task["due"] != None else ""
                    print (f'{status} || {task_counter} || {task["description"]} || {due_date} || {task["priority"]}')
                    task_counter+=1
            else:
                print(f"\n --- {priority.capitalize()} Level---")
                print("\n No tasks")
        print("\n-----End of List-----")

def main():
    while True:
        print()
        print("-----TO DO LIST-----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task")
        print("4. Edit Task")
        print("5. View Task")
        print("6. Exit ")
        print()
        try:
            choice = int(input("Enter your choice: ")) 

            if choice==1:
                addTask()
            elif choice==2:
                removeTask()
            elif choice==3:
                markTasks()
            elif choice==4:
                editTasks()
            elif choice==5:
                view_list()
            elif choice==6:
                print("--Program Terminated--")
                break
            else:
                print("Invalid choice! (Enter between range 1-5)")
       
        except ValueError:
            print("Invalid choice!")

if __name__=="__main__":
    loadTasks()
    main()