📝 Terminal-Based To-Do List App
A Python-based terminal application that helps users manage tasks efficiently. This app supports features like task prioritization, due dates, search, edit, and persistent storage — all from the command line.

🚀 Features
1️⃣ Add Tasks – Add tasks with a description, due date (optional), and priority (High, Mid, Low).
2️⃣ View Tasks – View tasks grouped by priority and sorted by due date.
3️⃣ Mark Tasks – Mark tasks as completed.
4️⃣ Remove Tasks – Delete a task by its task number.
5️⃣ Edit Tasks – Modify a task's description, due date, and priority.
6️⃣ Search Tasks – Search tasks by keyword (case-insensitive, partial match).
7️⃣ Save & Load – Tasks are automatically saved to a JSON file and reloaded on startup.

📁 File Structure

todo_app/
├── tasks.json           # Auto-generated file to store tasks
└── todo.py              # Main application script

🛠️ Technologies Used
Python 3
JSON for file-based storage
datetime for due date handling

💡 Possible Future Enhancements

🔎 Filter tasks by date (e.g., show only today's or pending tasks)

📤 Export tasks to CSV or PDF

🖥️ Create GUI version using Tkinter or a Web version using Flask