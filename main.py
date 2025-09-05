import tkinter as tk  # Import tkinter

# Main window setup
root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x300")
root.configure(bg="lightblue")

# Title
title_label = tk.Label(root, text="Welcome to the Simple GUI", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=20)

# Name input
name_label = tk.Label(root, text="Enter your name:", font=("Helvetica", 12), bg="lightblue")
name_label.pack()
name_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
name_entry.pack(pady=10)

# Functions
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name.", fg="red")

def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="", fg="black")

# Buttons
greet_user_button = tk.Button(root, text="Greet Me", font=("Helvetica", 12), command=greet_user)
greet_user_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset)
reset_button.pack(pady=10)

# Greeting label
greeting_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightblue")
greeting_label.pack(pady=20)

# Run app
root.mainloop()
