import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from PIL import Image, ImageTk
from open_file import open_file

def display_data():
    pass
def display_in_treeview():
    pass

def show_data_info():
    pass

def perform_operation():
    pass

def download_data():
    pass
theme = "light" 
file_path = None
current_data = None
def data_open():
    root = tk.Tk()
    root.state("zoomed")

    # Header Frame
    header_frame = tk.Frame(root, bg="#273746", height=70, bd=1, relief=tk.SOLID)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(header_frame, text="EMS - A Business Intelligence Tool", font=("Arial", 20, "bold"), bg="#273746", fg="white")
    header_label.pack(pady=15)

    # Main Part Frame
    main_frame = tk.Frame(root, bg="#ecf0f1", height=250, bd=1, relief=tk.SOLID)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Skyblue Left Frame
    menu_frame = tk.Frame(main_frame, bg="darkgrey", width=150, bd=1, relief=tk.SOLID)
    menu_frame.pack(fill=tk.Y, side=tk.LEFT)

    # Bottom Frame
    bottom_frame = tk.Frame(main_frame, bg="#ecf0f1", bd=1, relief=tk.SOLID)
    bottom_frame.pack(fill=tk.X)

    # Buttons for Data Operations
    data_operations = ["DATA CLEANING", "DATA INFORMATION", "DATA VISUALIZATION", "STATISTIC OF DATA"]
    for operation in data_operations:
        if operation == "DATA INFORMATION":
            operation_button = tk.Button(bottom_frame, text=operation, command=show_data_info, bg="#273746", fg="#ecf0f1", width=17, bd=1, relief=tk.RAISED)
        else:
            operation_button = tk.Button(bottom_frame, text=operation, command=lambda op=operation: perform_operation(),
                                        bg="#273746", fg="#ecf0f1", width=17, bd=1, relief=tk.RAISED)
        operation_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Download Button
    download_button = tk.Button(bottom_frame, text="Download Data", command=download_data, bg="#273746", fg="#ecf0f1", width=15, bd=1, relief=tk.RAISED)
    download_button.pack(side=tk.RIGHT, padx=10, pady=5)

    # Heading for File Upload
    file_heading = tk.Label(menu_frame, text="Upload File", font=("Arial", 14, "bold"), bg="darkgrey", fg="white")
    file_heading.pack(pady=10)

    # Buttons for Different File Types
    file_types = ["CSV", "Text", "Excel", "Word"]
    for file_type in file_types:
        button = tk.Button(menu_frame, text=f"Open {file_type}", command=lambda ft=file_type: open_file(ft),
                            bg="#273746", fg="#ecf0f1", width=15, bd=1, relief=tk.RAISED)
        button.pack(pady=5)

    # Main Content Frame (2/3 of Main Part Frame)
    content_frame = ttk.Frame(main_frame, style="Light.TFrame")
    content_frame.pack(fill=tk.BOTH, expand=True)
    
    def create_treeview(treeview_frame):
        treeview = ttk.Treeview(treeview_frame, show="headings", style="Treeview")
        treeview["columns"] = tuple()
        treeview.pack(expand=True, fill=tk.BOTH)
        return treeview  # Return the created Treeview widget

    # Treeview widget for tabular and non-tabular display
    treeview_frame = ttk.Frame(content_frame, style="Light.TFrame")
    treeview_frame.pack(expand=True, fill=tk.BOTH)
    
    my_treeview = create_treeview(treeview_frame)
    
    treeview_style = ttk.Style()
    treeview_style.configure("Treeview", font=("Arial", 10), background="#ecf0f1", fieldbackground="#ecf0f1", foreground="#17202a")

    # Configure styles for Light and Dark themes
    treeview_style.configure("Light.TFrame", background="#ecf0f1")
    treeview_style.configure("Dark.TFrame", background="#2c3e50")
    treeview = ttk.Treeview(treeview_frame, show="headings", style="Treeview")
    treeview["columns"] = tuple()
    treeview.pack(expand=True, fill=tk.BOTH)

    y_scrollbar = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
    y_scrollbar.pack(side="right", fill="y")
    treeview.configure(yscrollcommand=y_scrollbar.set)

    x_scrollbar = ttk.Scrollbar(treeview_frame, orient="horizontal", command=treeview.xview)
    x_scrollbar.pack(side="bottom", fill="x")
    treeview.configure(xscrollcommand=x_scrollbar.set)

    # Footer Frame
    footer_frame = tk.Frame(root, bg="#273746", height=30, bd=1, relief=tk.SOLID)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

    footer_label = tk.Label(footer_frame, text="© 2024 EMS - A Business Intelligence Tool", font=("Arial", 8), bg="#273746", fg="white")
    footer_label.pack(pady=5)
    
    def set_theme():
        if theme == "light":
            root.configure(bg="#17202a")
            header_frame.configure(bg="#273746")
            menu_frame.configure(bg="darkgrey")
            main_frame.configure(bg="#ecf0f1")
            content_frame.configure(style="Light.TFrame")
            treeview_frame.configure(style="Light.TFrame")
            footer_frame.configure(bg="#273746")
            toggle_theme_button.configure(image=light_icon)
        else:
            root.configure(bg="black")
            header_frame.configure(bg="#001f3f")
            menu_frame.configure(bg="#1a1a1a")
            main_frame.configure(bg="#2c3e50")
            content_frame.configure(style="Dark.TFrame")
            treeview_frame.configure(style="Dark.TFrame")
            footer_frame.configure(bg="#001f3f")
            toggle_theme_button.configure(image=dark_icon)

    def toggle_theme():
        global theme
        theme = "dark" if theme == "light" else "light"
        set_theme()

    # Toggle Theme Button with Image
    toggle_image_light = Image.open("light.png")  # Replace with your light theme icon
    toggle_image_dark = Image.open("dark.png")  # Replace with your dark theme icon
    light_icon_resized = toggle_image_light.resize((20, 20))
    dark_icon_resized = toggle_image_dark.resize((20, 20))
    light_icon = ImageTk.PhotoImage(light_icon_resized)
    dark_icon = ImageTk.PhotoImage(dark_icon_resized)

    toggle_theme_button = tk.Button(menu_frame, image=light_icon, command=toggle_theme, bd=0)
    toggle_theme_button.pack(side=tk.BOTTOM, padx=10, pady=5, anchor='w')

    set_theme()

    root.mainloop()
data_open()