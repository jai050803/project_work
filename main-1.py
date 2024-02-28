import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from docx import Document
import pandas as pd
import os

opened_files = []
def open_file(file_type, display_area):
    file_extensions = {
        "Excel": "xlsx",
        "CSV": "csv",
        "Word": "docx",
        "TXT": "txt",
        "MySQL": "sql",
        "JSON": "json",
        "Others": "*"
    }
    file_extension = file_extensions.get(file_type, "*")
    file_path = filedialog.askopenfilename(title=f"Select {file_type} File", filetypes=[(f"{file_type} files", f"*.{file_extension}")])
    if file_path:
        opened_files.append({"path": file_path, "type": file_type})  # Ensure this line is correct
        display_file_name(os.path.basename(file_path), display_area)


def merge_files():
    if not opened_files:
        messagebox.showinfo("Merge Error", "No files have been opened for merging.")
        return

    # Initialize an empty DataFrame for the merge result
    merged_df = pd.DataFrame()

    # Attempt to merge files based on common columns
    for file_info in opened_files:
        file_path = file_info['path']
        file_type = file_info['type']

        # Load the file into a DataFrame
        if file_type == 'Excel':
            df = pd.read_excel(file_path)
        elif file_type == 'CSV':
            df = pd.read_csv(file_path)
        else:
            messagebox.showinfo("Merge Error", f"File type '{file_type}' is not supported for merging.")
            return

        # If it's the first file, initialize merged_df
        if merged_df.empty:
            merged_df = df
        else:
            # Attempt to find common columns and merge
            common_columns = list(set(merged_df.columns) & set(df.columns))
            if common_columns:
                merged_df = pd.merge(merged_df, df, on=common_columns, how='outer')
            else:
                messagebox.showinfo("Merge Error", "No common columns found between files for merging.")
                return

    # After merging, offer to save the merged DataFrame
    if not merged_df.empty:
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if save_path:
            if save_path.endswith('.csv'):
                merged_df.to_csv(save_path, index=False)
            elif save_path.endswith('.xlsx'):
                merged_df.to_excel(save_path, index=False)
            messagebox.showinfo("Merge Successful", f"Files have been merged and saved to {save_path}")

def display_file_name(filename, display_area):
    # Function to display the filename in the specified area
    global opened_files
    opened_files.append(filename)  # Add filename to the list of opened files
    
    for i, name in enumerate(opened_files):
        tk.Label(display_area, text=name, bg='#ffffff', font=('Arial', 12, 'bold')).grid(row=i, column=0, sticky='w', padx=10, pady=5)

def show_secondary_page():
    window = tk.Tk()
    window.title("Dashboard")
    window.state("zoomed")
    window.title('EMS - A Business Intelligence tool')
    window.configure(bg="#eff5f6")
    image_icon = PhotoImage(file="logo.png")
    window.iconphoto(False,image_icon)
    
    header = Frame(window, bg="#009df4", width=1366, height=60)
    header.place(x=200, y=0)
        
    logout_text = Button(header, text="Logout",border = 0, font="arial 12 bold", bg="#009df4", fg="white", cursor="hand2")
    logout_text.place(x=1090,y=15)
        
    #sidebar
    sidebar = Frame(window, bg="#ffffff")
    sidebar.place(x=0,y=0,width=200,height=700)
        
# Replace PhotoImage with ImageTk.PhotoImage
    original_img = Image.open('avatar.png')
    resized_img = original_img.resize((150, 150), Image.Resampling.LANCZOS) 
    img = ImageTk.PhotoImage(resized_img)
    sidebar.img = img
    # Create a label to display the image and place it on the sidebar
    avatar_label = Label(sidebar, image=img, bg='#ffffff')
    avatar_label.place(x=20, y=80)
    
    username_label = Label(sidebar, text=f"Hello", font="arial 12 bold", bg="#ffffff")
    username_label.place(x=50,y=240)
        
    #body
    heading = Label(window, text = "User Dashboard", font="arial 20 bold", fg="#009df4")
    heading.place(x=700, y=70)
    
    #frames
    bodyframe1 = Frame(window, bg='#ffffff')
    bodyframe1.place(x=240, y= 110, width=1100, height=320)
    
    merge_button = Button(bodyframe1, text="Merge Files", command=merge_files, border=0, font="arial 10 bold", bg="green", fg="white")
    merge_button.place(x=400, y=280)  # Adjust x, y coordinates as needed

    
    file_types = ["Excel", "CSV", "Word", "TXT", "MySQL", "JSON", "Others"]
    
    for i, file_type in enumerate(file_types):
        Button(sidebar, text=file_type, command=lambda ft=file_type, bf=bodyframe1: open_file(ft, bf),
               border=0, font="arial 10 bold", bg="black", fg="white").place(x=20, y=300 + (i * 50), width=160, height=30)
    
    bodyframe2 = Frame(window, bg='#009aa5')
    bodyframe2.place(x=240, y= 455, width=310, height=220)
    
    bodyframe3 = Frame(window, bg='#e21f26')
    bodyframe3.place(x=640, y= 455, width=310, height=220)
    
    bodyframe4 = Frame(window, bg='#ffcb1f')
    bodyframe4.place(x=1030, y= 455, width=310, height=220)
    
    
    window.mainloop()
    
show_secondary_page()