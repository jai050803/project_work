import customtkinter as ctk

class frame(ctk.CTKFrame):
    def __init__(self, *args, header_name="Login", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        self.header = ctk.CTkLabel(self, text=self.header_name, background="green")
        self.header.grid(row=0, column=0, padx=10, pady=10)