import tkinter as tk
from tkinter import Scrollbar
from tkinter import filedialog
import customtkinter as ctk
import pandas as pd

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Create a label for the chatbot title
        chatbot_label = tk.Label(root, text="AI Chatbot", font=("Arial", 14), bg="deep sky blue" , fg="white")
        chatbot_label.pack(padx=10, pady=5, fill=tk.X)
        
        # Create a Text widget for file path display
        self.file_path_display = tk.Text(root, height=1, width=50, state=tk.DISABLED)
        self.file_path_display.pack(padx=10, pady=5)

        # Create a button to upload a file
        upload_button = tk.Button(root, text="Upload Your File", command=self.upload_file, bg="light blue", fg="black")
        upload_button.pack(pady=5)

        # Create a Text widget for chat display
        self.chat_display = ctk.CTkTextbox(root, height=200, width=500, state=tk.DISABLED)
        self.chat_display.pack(padx=10, pady=10)

        # Create a Scrollbar for the Text widget
        scrollbar = Scrollbar(root, command=self.chat_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.configure(yscrollcommand=scrollbar.set)

        # Create an Entry widget for user input
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)

        # Create a button to send the message
        send_button = ctk.CTkButton(root, text="Send", command=self.send_message, width=40)
        send_button.pack(pady=20)

        # Change the mouse hover effect for the button
        send_button.bind("<Enter>", lambda event, button=send_button: self.on_enter(event, button))
        send_button.bind("<Leave>", lambda event, button=send_button: self.on_leave(event, button))
        
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.display_message(f"File uploaded: {file_path}")
            self.file_path_display.config(state=tk.NORMAL)
            self.file_path_display.delete(1.0, tk.END)
            self.file_path_display.insert(tk.END, file_path)
            self.file_path_display.config(state=tk.DISABLED)

            # You can add your pandas logic here to process the uploaded file
            # For now, let's just display a dummy message
            df = pd.read_csv(file_path)
            self.display_message(f"Number of rows in the file: {len(df)}")
            
    def send_message(self):
        user_input_text = self.user_input.get()
        if user_input_text:
            # Display user message in the chat display
            self.display_message("You: " + user_input_text)

            # You can add your logic here to process user input and generate a response
            # For now, let's just display a dummy response
            response = "Bot: Your message was received!"

            # Display the bot's response in the chat display
            self.display_message(response)

            # Clear the user input
            self.user_input.delete(0, tk.END)

    def display_message(self, message):
        # Enable the Text widget to modify its content
        self.chat_display.configure(state=tk.NORMAL)
        # Insert the message into the Text widget
        self.chat_display.insert(tk.END, message + "\n")
        # Disable the Text widget to prevent further modification
        self.chat_display.configure(state=tk.DISABLED)
        # Autoscroll to the bottom
        self.chat_display.yview(tk.END)

    def on_enter(self, event, widget):
        widget.configure()

    def on_leave(self, event, widget):
        widget.configure()


if __name__ == "__main__":
    root = ctk.CTk()
    app = ChatApp(root)
    root.mainloop()

