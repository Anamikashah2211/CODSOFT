# todo_list.py

import tkinter as tk
from tkinter import messagebox

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks from the listbox
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a frame to hold the task entry field and buttons
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create a task entry field
task_entry = tk.Entry(input_frame, width=35)
task_entry.pack(side=tk.LEFT, padx=10)

# Create a button to add the task
add_button = tk.Button(input_frame, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT)

# Create a listbox to display tasks
task_listbox = tk.Listbox(window, height=10, width=50, bd=3)
task_listbox.pack(pady=10)

# Create a frame for delete and clear buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create a delete button
delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear All", width=12, command=clear_tasks)
clear_button.pack(side=tk.LEFT)

# Start the main event loop
window.mainloop()
