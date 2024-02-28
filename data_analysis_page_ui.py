import tkinter as tk
# from tkinter import PhotoImage, Frame, Label
from tkinter import ttk  # Import ttk module for Treeview
from tkinter import messagebox
import pandas as pd

def remove_empty_cells():
    pass

def remove_duplicates():
    pass

def show_data_info():
    pass

def replace_using_mode():
    pass

def replace_using_median():
    pass

def display_in_treeview(data):
    pass

def replace_using_mean():
    pass

def replace_empty_values():
    pass

def correct_wrong_formats():
    pass

def data_cleaning():
    cleaning_window = tk.Tk()
    cleaning_window.state("zoomed")
    cleaning_window.title("Data Cleaning - Dealing with Empty Cells and Duplicates")
    cleaning_window.configure(bg="#ecf0f1")  # Background color for the cleaning window

    # Header Frame of data_cleaning
    header_frame = tk.Frame(cleaning_window, bg="#273746", height=70, bd=1, relief=tk.SOLID)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(header_frame, text="DATA WRANGLING", font=("Arial", 20, "bold"), bg="#273746", fg="white")
    header_label.pack(pady=15)

    # Main Part Frame of data_cleaning
    main_frame2 = tk.Frame(cleaning_window, bg="#ecf0f1", height=250, bd=1, relief=tk.SOLID)
    main_frame2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Skyblue Left Frame of data_cleaning
    menu_frame2 = tk.Frame(main_frame2, bg="darkgrey", width=150, bd=1, relief=tk.SOLID)
    menu_frame2.pack(fill=tk.Y, side=tk.LEFT)

    remove_empty_cells_button = tk.Button(menu_frame2, text="Removing Rows of Empty Cells", command=remove_empty_cells, bg="grey", fg="white")
    remove_empty_cells_button.pack(pady=10)

    replace_empty_values_button = tk.Button(menu_frame2, text="Replace Empty Values", command=replace_empty_values, bg="grey", fg="white")
    replace_empty_values_button.pack(pady=10)

    replace_using_mean_button = tk.Button(menu_frame2, text="Replace Empty Cells Using Mean", command=replace_using_mean, bg="grey", fg="white")
    replace_using_mean_button.pack(pady=10)

    replace_using_median_button = tk.Button(menu_frame2, text="Replace Empty Cells Using Median", command=replace_using_median, bg="grey", fg="white")
    replace_using_median_button.pack(pady=10)

    replace_using_mode_button = tk.Button(menu_frame2, text="Replace Empty Cells Using Mode", command=replace_using_mode, bg="grey", fg="white")
    replace_using_mode_button.pack(pady=10)

    remove_duplicates_button = tk.Button(menu_frame2, text="Remove Duplicates", command=remove_duplicates, bg="grey", fg="white")
    remove_duplicates_button.pack(pady=10)

    correct_formats_button = tk.Button(menu_frame2, text="Correct Wrong Formats", command=correct_wrong_formats, bg="grey", fg="white")
    correct_formats_button.pack(pady=10)

    cleaning_window.mainloop()


data_cleaning()