def addTask():
    t= input("Enter task desciption: ")
    todo_list.append(t)
    print("Task added successfully")


def removeTask():
    if len(todo_list)==0:
        print("List is empty")
        
    else:
        view_list()
        try:
            task_num = int(input("Enter task number: "))
            idx= task_num-1
            if 0<=idx<len(todo_list):
                removed_task = todo_list.pop(idx)
                print(removed_task, " task removed successfully")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid arguments")

def view_list():
    if len(todo_list)==0:
        print("List is empty")
    else:
        i=1
        print("-To Do List-")
        for tasks in todo_list:
            print(" ",i, tasks)
            i+=1
        print()
        print("END OF LIST")

todo_list = [] #creating list

#Displaying actions menu
def main():
    while True:
        print("--TO DO LIST--")
        print("1. Add")
        print("2. Remove")
        print("3. View")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: ")) 

            if choice==1:
                addTask()
            elif choice==2:
                removeTask()
            elif choice==3:
                view_list()
            elif choice==4:
                print("--Program Ended--")
                break
            else:
                print("Invalid choice! (Enter between range 1-4)")
       
        except ValueError:
            print("Invalid choice!")

if __name__=="__main__":
    main()