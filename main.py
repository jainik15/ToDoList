import sys 
def addTask():
    t= input("Enter task desciption: ")
    todo_list.append(t)
    print("Task added successfully")
    main()

def removeTask():
    if len(todo_list)==0:
        print("List is empty")
        
    else:
        i=1
        for tasks in todo_list:
            print(i, tasks)
            i+=1
        try:
            removeTask = int(input("Enter number to remove: "))
            todo_list.remove(todo_list[removeTask])
            print("Task removed successfuly")
        except:
            print("Invalid arguements")
        main()

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
    main()


todo_list = [] #creating list

#Displaying actions menu
def main():
    print("--TO DO LIST--")
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    while True:
        try:
            user_choice = int(input("Enter your choice: ")) 
            if 0< user_choice <5:
                choice=user_choice
                break
            else:
                print("Invalid choice! Enter between range 1-4")
        except ValueError:
            print("Invalid choice!")

    if choice==1:
        addTask()
    elif choice==2:
        removeTask()
    elif choice==3:
        view_list()
    elif choice==4:
        sys.exit()

if __name__=="__main__":
    main()