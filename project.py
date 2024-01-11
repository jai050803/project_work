from tkinter import messagebox
import tkinter as tk
import mysql.connector


# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'jai',
    'password': 'jai@2301420045',
    'database': 'user_Credentials',
}

def create_user_table():
    # Function to create the user table if not exists
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE,
                password VARCHAR(50)
            )
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def insert_user(username, password):
    # Function to insert a new user into the database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error", "Failed to register user.")
    finally:
        cursor.close()
        conn.close()

def signup():
    # Function to handle signup button click
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        insert_user(username, password)
    else:
        messagebox.showwarning("Warning", "Please enter both username and password.")

# Create the main window
root = tk.Tk()
root.title("Signup Form")

# Set the window size and position
root.geometry("800x400")

# Create frames
left_frame = tk.Frame(root, width=480)
right_frame = tk.Frame(root, width=320)

# Pack frames in 60:40 ratio
left_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Load and display an image on the left frame
photo = tk.PhotoImage(file="./images.png")
image_label = tk.Label(left_frame, image=photo)
image_label.photo = photo
image_label.pack(expand=True, fill=tk.BOTH)

# Create and pack widgets for the signup form on the right frame
create_user_table()

tk.Label(right_frame, text="Signup Form", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(right_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(right_frame)
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(right_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(right_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

signup_button = tk.Button(right_frame, text="Signup", command=signup)
signup_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()