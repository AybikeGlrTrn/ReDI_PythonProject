import tkinter 
import tkinter.messagebox

root= tkinter.Tk()
root.title ("To-Do List")

def add_task():
    task = entry_task.get()
    listbox_tasks.insert(tkinter.END, task)

def delete_task():
    task_index=listbox_tasks.curselection()[0]
    listbox_tasks.delete(task_index)

def load_task():
    pass

def save_task():
    pass
  
#Create te GUI
listbox_tasks = tkinter.Listbox(root, height=20, width=50)
listbox_tasks.pack()

entry_task=tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task=tkinter.Button(root, text="Add a new task", width=48, command=add_task)
button_add_task.pack()

button_delete_task=tkinter.Button(root, text="Delete a new task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task=tkinter.Button(root, text="Load tasks", width=48, command=load_task)
button_load_task.pack()

button_save_task=tkinter.Button(root, text="Save tasks", width=48, command=save_task)
button_save_task.pack()

root.mainloop()
