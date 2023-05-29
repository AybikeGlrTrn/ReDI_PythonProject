class Todo:
# define attributes of Todo class
  def __init__(self, todo_desc, todo_type, todo_priority, todo_deadline):
    self.todo_desc = todo_desc
    self.todo_type = todo_type
    self.todo_priority = todo_priority
    self.todo_deadline = todo_deadline

  def show(self):
    print ("Description:", self.todo_desc, "Type:", self.todo_type, "Priority:", self.todo_priority, "Deadline: ", self.todo_deadline)

todo_list = []

# get and store text in the todo list of strings
def new_task_entry():
  todo_desc = input ("Enter your new to do: ")
#Define type of todo after enterinhg the task 
  todo_type = input("Please select the to do type: \n1-Personal task \n2-Work task\n")
#Define priority of todo after enterinhg the task 
  todo_priority = input("Please select the to do priority: \n1-High importance \n2-Medium importance \n3-Low importance\n")
#Enter deadline of todo
  todo_deadline = input ("Please enter your to do deadline in MM/DD/YYYY forma: \n")  
  
# create a new todo instance from the parameters given above
# insert tne new instance into the list
  New_todo = Todo (todo_desc, todo_type, todo_priority, todo_deadline)
  todo_list.append(New_todo) 


# print out the todo list of strings
def review_todo():
  print("todo_list: ")
  for todo in todo_list:
      todo.show()

#Selection of operations
greeting = "Welcome to your to do list"
print (greeting)

while True:
  operation=input("Please select the operation: \n1- Enter a new to do \n2- Review your current to do list \n3- Exit to do list\n")
  
  if operation == "1": 
    new_task_entry()

  elif operation == "2":
    review_todo()
  
  elif operation == "3":
    print("Your to do list will be closed") 
    break
  
  else:
    print("Select a valid operation")



