todo_list = [] #creating list

#Displaying actions menu
print("--TO DO LIST--")
print("1. Add")
print("2. Remove")
print("3. View")
print("4. Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))
        break
    except:
        print("Invalid choice!")

