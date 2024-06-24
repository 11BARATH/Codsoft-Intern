
# INTERN To Do List
from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def mark_complete():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(END, f"{task} (Completed)")
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_entry.get()
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, task)
        task_entry.delete(0, END)
    except:
        messagebox.showwarning("Warning", "You must select a task and enter new details.")

root = Tk()
root.title("To-Do List")

input_frame = Frame(root)
input_frame.pack(pady=10)

task_listbox_frame = Frame(root)
task_listbox_frame.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

task_label = Label(input_frame, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = Entry(input_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

task_listbox = Listbox(task_listbox_frame, width=50, height=10, selectmode=SINGLE)
task_listbox.pack(side=LEFT, fill=BOTH)

task_scrollbar = Scrollbar(task_listbox_frame)
task_scrollbar.pack(side=RIGHT, fill=BOTH)

task_listbox.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=task_listbox.yview)

add_button = Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5, pady=5)

complete_button = Button(button_frame, text="Mark Complete", command=mark_complete)
complete_button.grid(row=0, column=2, padx=5, pady=5)

update_button = Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()





