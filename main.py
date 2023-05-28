class Todo:
  pass 

todo_list= []

# get text
# store text in the todo list of strings
def new_task_entry():
  task = input ("Enter your new task: ")
  todo_list.append(task)
  print ("Task added successfully")

# print out the todo list of strings
def review_task():
  print("todo_list: ")
  for task in todo_list:
    print (task)

#Selection of operations
greeting = "Welcome to your to do list"
print (greeting)

while True:
  operation=input("Please select the operation: \n1- Enter a new to do task \n2- Review your current to do list \n3- Exit to do list\n")
  
  if operation == "1": 
    new_task_entry()
  
  elif operation == "2":
    review_task()
  
  elif operation == "3":
    print("Your to do list will be closed") 
    break
  
  else:
    print("Select a valid operation")