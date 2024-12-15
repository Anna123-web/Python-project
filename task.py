import tkinter as tk
from tkinter import messagebox

# Callback functions
def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

def update_label():
    text = entry.get()
    if text.strip():
        center_label.config(text=text)
    else:
        center_label.config(text="Center")

# Create the main window
root = tk.Tk()
root.title("Enhanced GUI Example")
root.geometry("500x400")

# Centered Label
center_label = tk.Label(root, text="Center", bg="blue", fg="white", font=("Arial", 14))
center_label.place(relx=0.5, rely=0.5, anchor="center")

# Top-Right Label
top_right_label = tk.Label(root, text="Top-Right", bg="green", fg="white", font=("Arial", 12))
top_right_label.place(relx=1.0, rely=0.0, anchor="ne")

# Label with Relative Dimensions
rel_size_label = tk.Label(root, text="Relwidth & Relheight", bg="red", fg="white", font=("Arial", 12))
rel_size_label.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.2)

# Button to Show Message Box
button = tk.Button(root, text="Click Me", command=on_button_click, bg="yellow", font=("Arial", 12))
button.place(relx=0.5, rely=0.8, anchor="center")

# Entry Widget to Update Label
entry = tk.Entry(root, font=("Arial", 12))
entry.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.4)

# Button to Update Label Text
update_button = tk.Button(root, text="Update Label", command=update_label, bg="lightblue", font=("Arial", 10))
update_button.place(relx=0.5, rely=0.9, anchor="center")

# Run the Tkinter event loop
root.mainloop()