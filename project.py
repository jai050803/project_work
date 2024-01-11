import customtkinter as ctk 
import mysql.connector

# MySQL database connection details
db_config = {
    'host': 'your_host',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_database',
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


ctk.set_appearance_mode("System")

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("EMS App")  
        self.geometry("800x800")  


if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop() 