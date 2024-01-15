import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk

def submit_form():
    # Implement form submission logic here
    print("Form submitted")

def show_login():
    # Implement logic to switch to login frame
    print("Switching to login frame")

# Create the main window
root = ctk.CTk()
root.title("Signup Window")
root.geometry("700x700")

# Left Frame with an image
left_frame = ttk.Frame(root, width=700, height=700)
left_frame.grid(row=0, column=0)

# Load and display an image on the left frame
image_path = "./images.png"  # Replace with the actual image path
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

image_label = ttk.Label(left_frame, image=photo)
image_label.image = photo  # Keep a reference to the image to prevent garbage collection
image_label.pack()

# Right Frame with signup form
right_frame = ttk.Frame(root, width=350, height=700)
right_frame.grid(row=0, column=1)

# Signup form elements
name_label = ttk.Label(right_frame, text="Name:")
name_entry = ttk.Entry(right_frame)

email_label = ttk.Label(right_frame, text="Email:")
email_entry = ttk.Entry(right_frame)

password_label = ttk.Label(right_frame, text="Password:")
password_entry = ttk.Entry(right_frame, show="*")

confirm_password_label = ttk.Label(right_frame, text="Confirm Password:")
confirm_password_entry = ttk.Entry(right_frame, show="*")

submit_button = ttk.Button(right_frame, text="Submit", command=submit_form, style="Green.TButton")

login_link = ttk.Label(right_frame, text="Already a member? Login here..", cursor="hand2")
login_link.bind("<Button-1>", lambda event: show_login())

# Styling for the submit button
style = ttk.Style()
style.configure("Green.TButton", foreground="white", background="green", borderwidth=1, relief="solid", padding=(10, 5), borderradius=5)

# Layout the signup form elements
name_label.grid(row=0, column=0, pady=10, sticky="w")
name_entry.grid(row=0, column=1, pady=10, sticky="w")

email_label.grid(row=1, column=0, pady=10, sticky="w")
email_entry.grid(row=1, column=1, pady=10, sticky="w")

password_label.grid(row=2, column=0, pady=10, sticky="w")
password_entry.grid(row=2, column=1, pady=10, stickSy="w")

confirm_password_label.grid(row=3, column=0, pady=10, sticky="w")
confirm_password_entry.grid(row=3, column=1, pady=10, sticky="w")

submit_button.grid(row=4, column=1, pady=20, sticky="e")

login_link.grid(row=5, column=1, pady=10, sticky="e")

# Run the Tkinter main loop
root.mainloop()
