import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar
import pandas as pd
import spacy
import openai

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")
        
        openai.api_key = "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"

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

            # Generate a response using OpenAI's GPT-3
            response = self.generate_response_openai(user_input_text)

            # Display the bot's response in the chat display
            self.display_message(f"Bot: {response}")

            # Clear the user input
            self.user_input.delete(0, tk.END)

    def generate_response_openai(self, input_text):
        # Add information from the uploaded data to the input prompt
        prompt = f"You: {input_text}\nBot: Data Info - {self.get_data_info()}\n"
        
        # Make a request to OpenAI's API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can experiment with different engines
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )

        return response['choices'][0]['text'].strip()

    def get_data_info(self):
        if self.uploaded_data is not None:
            # Provide some information about the uploaded data
            num_rows, num_columns = self.uploaded_data.shape
            column_names = ", ".join(self.uploaded_data.columns)

            return f"The dataset contains {num_rows} rows and {num_columns} columns. Columns: {column_names}"
        else:
            return "No data has been uploaded."

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
