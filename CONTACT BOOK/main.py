import tkinter as tk
from tkinter import messagebox

# Contact book dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contacts[name] = phone
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Function to remove a contact
def remove_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    
    if selected_contact:
        name = selected_contact.split(":")[0].strip()
        if name in contacts:
            del contacts[name]
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' removed!")
        else:
            messagebox.showwarning("Error", "Contact not found.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to remove.")

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {phone}")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=10)

# Entry widgets for name and phone
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)
phone_entry = tk.Entry(root, font=("Arial", 14))
phone_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons to add and remove contacts
add_button = tk.Button(root, text="Add Contact", font=("Arial", 12), command=add_contact)
add_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Contact", font=("Arial", 12), command=remove_contact)
remove_button.grid(row=2, column=1, padx=10, pady=10)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, font=("Arial", 14), height=10, width=30)
contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
