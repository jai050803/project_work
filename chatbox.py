import tkinter as tk
from tkinter import Scrollbar

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Create a Text widget for chat display
        self.chat_display = tk.Text(root, height=20, width=50, state=tk.DISABLED)
        self.chat_display.pack(padx=10, pady=10)

        # Create a Scrollbar for the Text widget
        scrollbar = Scrollbar(root, command=self.chat_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.config(yscrollcommand=scrollbar.set)

        # Create an Entry widget for user input
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(padx=10, pady=10)

        # Create a button to send the message
        send_button = tk.Button(root, text="Send", command=self.send_message)
        send_button.pack(pady=10)

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
        self.chat_display.config(state=tk.NORMAL)
        # Insert the message into the Text widget
        self.chat_display.insert(tk.END, message + "\n")
        # Disable the Text widget to prevent further modification
        self.chat_display.config(state=tk.DISABLED)
        # Autoscroll to the bottom
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
