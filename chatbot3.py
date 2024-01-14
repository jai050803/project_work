import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar
import pandas as pd
import spacy

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Create a label for the chatbot title
        chatbot_label = tk.Label(root, text="AI Chatbot", font=("Arial", 14), bg="deep sky blue", fg="black")
        chatbot_label.pack(padx=10, pady=5, fill=tk.X)

        # Create a Text widget for file path display
        self.file_path_display = tk.Text(root, height=1, width=50, state=tk.DISABLED)
        self.file_path_display.pack(padx=10, pady=5)

        # Create a button to upload a file
        upload_button = tk.Button(root, text="Upload Your File", command=self.upload_file, bg="light blue", fg="black")
        upload_button.pack(pady=5)

        # Create a Text widget for chat display
        self.chat_display = tk.Text(root, height=10, width=50, state=tk.DISABLED)
        self.chat_display.pack(padx=10, pady=10)

        # Create an Entry widget for user input
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)

        # Create a button to send the message
        send_button = tk.Button(root, text="Send", command=self.send_message, bg="light blue", fg="black", width=10)
        send_button.pack(pady=10)

        # Load spaCy language model
        self.nlp = spacy.load("en_core_web_sm")

        # DataFrame to store the uploaded data
        self.uploaded_data = None

        # List to store the changes made by the user
        self.changes = []

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

            # Read the uploaded data into a DataFrame
            self.uploaded_data = pd.read_csv(file_path)

            # Display a dummy message for now
            self.display_message(f"Number of rows in the file: {len(self.uploaded_data)}")

    def send_message(self):
        user_input_text = self.user_input.get()
        if user_input_text:
            # Display user message in the chat display
            self.display_message("You: " + user_input_text)

            # Generate a response using spaCy
            response = self.generate_response(user_input_text)
            
            # Display the bot's response in the chat display
            self.display_message(f"Bot: {response}")

            # Clear the user input
            self.user_input.delete(0, tk.END)

    def generate_response(self, input_text):
        # Use spaCy for basic response generation
        doc = self.nlp(input_text)

        # Check if the user is asking about the data description
        if any(token.text.lower() in ["data", "description", "describe"] for token in doc):
            if self.uploaded_data is not None:
                # Generate statistical information using pd.describe()
                description = self.uploaded_data.describe()
                return f"Here is the statistical information of the data:\n\n{description}"
            else:
                return "Please upload a file first."

        # Check if the user wants to clean the data
        if any(token.text.lower() in ["clean", "remove", "null", "duplicate"] for token in doc):
            response = self.clean_data(input_text)
            return response

        # If no specific query is detected, return a default response
        return "I'm a simple chatbot. Ask me anything!"

    def clean_data(self, input_text):
        # Perform data cleaning operations based on user input
        if "remove duplicate data" in input_text.lower():
            self.uploaded_data.drop_duplicates(inplace=True)
            self.changes.append("Removed duplicate data.")
            return "Duplicate data removed."

        elif "show me duplicate data" in input_text.lower():
            duplicate_rows = self.uploaded_data[self.uploaded_data.duplicated()]
            return f"Duplicate data:\n\n{duplicate_rows}"

        elif "remove null values from this column" in input_text.lower():
            # Extract column name from the input
            column_name = input_text.split("from this column")[1].strip()
            self.uploaded_data.dropna(subset=[column_name], inplace=True)
            self.changes.append(f"Removed null values from column '{column_name}'.")
            return f"Null values removed from column '{column_name}'."

        elif "remove null values from the data" in input_text.lower():
            self.uploaded_data.dropna(inplace=True)
            self.changes.append("Removed null values from the entire dataset.")
            return "Null values removed from the entire dataset."

        else:
            return "I'm not sure how to clean the data based on your input."

    def display_message(self, message):
        # Enable the Text widget to modify its content
        self.chat_display.config(state=tk.NORMAL)
        # Insert the message into the Text widget
        self.chat_display.insert(tk.END, message + "\n")
        # Disable the Text widget to prevent further modification
        self.chat_display.config(state=tk.DISABLED)
        # Autoscroll to the bottom
        self.chat_display.yview(tk.END)

    def on_enter(self, event, widget):
        widget.config(bg="powder blue")

    def on_leave(self, event, widget):
        widget.config(bg="light blue")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
