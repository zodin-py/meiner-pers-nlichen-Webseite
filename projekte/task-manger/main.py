tasks_list = []
def add_taske_to_list():
  task = input("Enter task: ")
  task_date_str = input("Enter task date (yyyy.mm.dd): ")
  task_year, task_month, task_day = map(int, task_date_str.split('.'))
  if task_year < 2024 or task_month > 12 or task_day > 31:
     print("Invald format please. Enter a (yyyy.mm.dd)")
     return
  tasks = {"Task":task, "Task Date":task_date_str, "completed":False}
  tasks_list.append(tasks)
  print("task added to list")

def mark_task_complete(tasks):
  for i, task in enumerate(tasks):
    print(f"{i + 1}. {task['Task']} ")
  complet = int(input("Enter the number of the task to mark as complete: "))
  if 1 <= complet <= len(tasks):
    tasks[complet - 1]["completed"] = True
  else:
    print("Invalid task number.")
    
def view_tasks(tasks):
  for i, task in enumerate(tasks):
    if task["completed"]:
      emoge = "✅"
    else:
      emoge = "❌" 
  
    print(f"{i + 1}. {task['Task']} ({task['Task Date']}) {emoge}")


def mein():
  massege = '''1. Add task to list
2. Mark task as complete
3. View tasks
4. Quit
'''
  while True:
    print(massege)
    choice = input("Enter your choice: ")
    if choice == "1":
      add_taske_to_list()

    elif choice == "2":
      mark_task_complete(tasks_list)

    elif choice == "3":
      view_tasks(tasks_list)

    elif choice == "4":
      print("see you agen")
      break

    else:
      print("Invalid chice please enter a number between 1 and 4")


mein()



