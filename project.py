from tkinter import messagebox
import tkinter as tk
import customtkinter as ctk
import mysql.connector
import customtkinter as ctk

class frame(ctk.CTkFrame):
    def __init__(self, *args, header_name="Login", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)
        
        self.fullname = ctk.CTkLabel(self, text="Enter your full name", font=("Helvetica", 16))
        self.fullname.grid(row=2, column=0, columnspan=10, pady=10)
        
        self.entry = ctk.CTkEntry(self, placeholder_text="full name")
        self.entry.grid(row=3, column=0, columnspan=10, pady=8, padx=10)
        
        self.username = ctk.CTkLabel(self, text="Username", font=("Helvetica", 16))
        self.username.grid(row=4, column=0, columnspan=10, pady=10)

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
                fullname VARCHAR(50),
                emailaddress varchar(50),
                username VARCHAR(50) UNIQUE,
                password VARCHAR(50),
            )
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def insert_user(name, username, password):
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
ctk.set_appearance_mode("System")        


# Set the window size and position
ctk.set_default_color_theme("green")    

# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("EMS App")    
        self.geometry("800x800")
        
        self.frame1 = frame(self, header_name="Login Here")
        self.frame1.grid(row=10, column=10, padx=100, pady=100)
        
        
        
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()  