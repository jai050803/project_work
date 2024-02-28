import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_file(file_type):
    file_path = filedialog.askopenfilename(filetypes=[(file_type, file_type)])
    if file_path:
        global df
        if file_type == "*.csv":
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        update_treeview()

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    tree["column"] = list(df.columns)
    tree["show"] = "headings"
    for column in tree["column"]:
        tree.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

def plot_graph():
    cols_to_plot = []
    num_cols = simpledialog.askinteger("Input", "How many columns to plot?", parent=window, minvalue=1, maxvalue=len(df.columns))
    for i in range(num_cols):
        col_name = simpledialog.askstring("Input", f"Enter column name {i+1}:", parent=window)
        if col_name in df.columns:
            cols_to_plot.append(col_name)
    
    if not cols_to_plot:
        tk.messagebox.showerror("Error", "No valid columns selected.")
        return

    df[cols_to_plot].plot(kind='line' if len(cols_to_plot) > 1 else 'bar')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Plot")
    plt.show()

window = tk.Tk()
window.title("Data Plotter")
window.geometry("800x600")

df = pd.DataFrame()

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

tree_frame = tk.Frame(window)
tree_frame.pack(fill=tk.BOTH, expand=True)

tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack(fill=tk.BOTH, expand=True)
tree_scroll.config(command=tree.yview)

btn_load_csv = tk.Button(left_frame, text="Open CSV", command=lambda: load_file("*.csv"))
btn_load_csv.pack(fill=tk.X)

btn_load_excel = tk.Button(left_frame, text="Open Excel", command=lambda: load_file("*.xlsx"))
btn_load_excel.pack(fill=tk.X)

btn_plot = tk.Button(right_frame, text="Plot the suggested graph", command=plot_graph)
btn_plot.pack()

window.mainloop()
