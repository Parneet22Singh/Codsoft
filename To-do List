import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error",'Please enter the task!')

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Error","Please select the task you want to delete!")

# Set up the main window
window = tk.Tk()
window.title("My To-Do List")
window.configure(bg="light green")

# To-Do List Heading
heading = tk.Label(window, text="To-Do List", font=("Times New Roman", 20))
heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Task Entry
task_entry = tk.Entry(window, width=40)
task_entry.grid(row=1, column=0, padx=10, pady=10)

# Add Task Button
add_button = tk.Button(window, text="Add Task", width=10, command=add_task)
add_button.grid(row=1, column=1, padx=10, pady=10)

# Task Listbox
task_listbox = tk.Listbox(window, width=60, height=10)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Delete Task Button
delete = tk.Button(window, text="Delete Task", width=10, command=delete_task)
delete.grid(row=3, column=0, padx=10, pady=10)

# Exit Button
exit = tk.Button(window, text="Exit", width=10, command=window.quit)
exit.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()
