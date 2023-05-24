class todolist:
  pass 

def new_task_entry():
  pass

def review_task():
  pass

#Selection of operations
greeting = "Welcome to your to do list"
print (greeting)

operation=input("Please select the operation: \n1- Enter a new to do \n2- Review your current to do list \n3- Exit to do list\n")

if operation == "1": 
  print("Enter a new task")
  new_task_entry()

elif operation == "2":
  print("Review your to do list") 
  review_task()
  
elif operation == "3":
  print("Your to do list will be closed") 

else:
  print("Select a valid operation")