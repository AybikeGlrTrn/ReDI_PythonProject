# validation of date input by datetime module
# getting todays` date by date module
from datetime import datetime, date

class Todo:
# define attributes of Todo class
  def __init__(self, todo_desc, todo_type , todo_priority, todo_date):
    self.todo_desc = todo_desc
    self.todo_type = todo_type
    self.todo_priority = todo_priority
    self.todo_date = todo_date

  def show(self):
    if self.todo_type=="1":
      type = "personal"
    elif self.todo_type=="2":
      type = "work"
    else:
      print("Select a valid operation")
        
    if self.todo_priority=="1":
      priority = "high"
    elif self.todo_priority=="2":
      priority = "medium"
    elif self.todo_priority=="3":
      priority = "low"
    else:
      print("Select a valid operation")
      
    print ("")  
    print ("to do:", self.todo_desc, ",", "type:", type, ",", "priority:", priority, ",", "deadline: ", self.todo_date)

todo_list = []

# get and store text in the todo list of strings
def new_task_entry():
  todo_desc = input ("Enter your new to do: ")
  print ("")
  
  while True:
    #Define type of todo after entering the task 
    todo_type = input("Please select to do type: \n Enter 1 for personal to do \n Enter 2 for work to do \n")
    #Check user input (type) of todo 
    if todo_type == "1" or todo_type == "2":
      break 
    else:
      print ("Invalid operation. Please enter 1 or 2")
  print ("")

  while True:
    #Define priority of todo 
    todo_priority = input("Please select to do priority: \n enter 1 for high priority \n enter 2 for medium priority \n enter 3 for low priority\n")
    #Check user input (priority) of todo 
    if todo_priority == "1" or todo_priority == "2" or todo_priority == "3":
      break 
    else:
      print ("Invalid operation. Please enter 1, 2 or 3") 
  print ("")
  
  #Enter deadline of todo # consider the date in string format DD/MM/YY
  #Check user input (date) of todo 
  while True:
    try:
      todo_date = input ("Please enter your to do deadline in MM/DD/YY format: \n")  
      date_object = datetime.strptime(todo_date, "%m/%d/%y").date()
      today = date.today()
      if date_object >= today:
        break
      else:
        print("Please enter a date in today or in the future")
    except ValueError as err:
      print(err)
  print ("")
  print("To do date added successfully")

  # create a new todo instance from the parameters given above
  # insert the new instance into the list
  new_todo = Todo (todo_desc, todo_type, todo_priority, date_object)
  todo_list.append(new_todo) 

# print out the todo list of strings
def review_todo():
  review_todo_type = input("Please select to do type: \n Enter 1 for Personal to do \n Enter 2 for Work to do \n")
  # sort by priority and date (Ascending order)
  todo_list.sort (key=lambda x: (x.todo_date, x.todo_priority))

  # print selected todo_type
  for todo in todo_list:
    if todo.todo_type==review_todo_type:
      todo.show()  

#Selection of operations
greeting = "Welcome to your to do list"
print (greeting)

while True:
  print ("")
  operation=input("Please select the operation: \n 1 for entering a new to do \n 2 for reviewing your current to do list \n 3 for exiting to do list\n")

  print ("")
  if operation == "1": 
    new_task_entry()
  elif operation == "2":
    review_todo()
  elif operation == "3":
    print("Your to do list will be closed") 
    break
  else:
    print("Select a valid operation")



