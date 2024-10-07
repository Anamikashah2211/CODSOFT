# Simple Calculator Program

import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to handle button press
def button_press(symbol):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(symbol))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a display widget
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="raised", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Buttons for calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 18), command=evaluate_expression)
        root.bind('<Return>', evaluate_expression)  # Enter key for "="
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: button_press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make columns and rows scalable
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
