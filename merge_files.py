import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import pandas as pd

class MergeApp:
    def __init__(self, root):
        self.root = root
        self.files = []
        self.common_columns = []
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("Merge Excel Files")

        # Frame for File Display and Actions
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=10, pady=5)

        # Button to Add Files
        self.add_button = tk.Button(frame, text="Add File", command=self.add_file)
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))

        # Button to Merge Files
        self.merge_button = tk.Button(frame, text="Merge Files", command=self.prompt_merge_column)
        self.merge_button.pack(side=tk.LEFT)

        # Display Area for Files
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("File Name",)
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("File Name", anchor=tk.W, width=400)
        self.tree.heading("File Name", text="File Name", anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    def add_file(self):
        file_name = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls;*.csv")])
        if file_name:
            self.files.append(file_name)
            self.tree.insert("", tk.END, values=(file_name,))
            self.update_common_columns()

    def update_common_columns(self):
        # Reset common columns
        self.common_columns = None

        for file in self.files:
            df = pd.read_csv(file) if file.endswith('.csv') else pd.read_excel(file)
            cols = set(df.columns)

            if self.common_columns is None:
                self.common_columns = cols
            else:
                self.common_columns = self.common_columns.intersection(cols)

    def prompt_merge_column(self):
        if not self.common_columns:
            messagebox.showerror("Error", "No common columns found or no files added.")
            return

        # Convert common_columns to a list and sort it for display
        common_columns_sorted = sorted(list(self.common_columns))
        column = simpledialog.askstring("Input", "Enter the column name to merge on:\n" + "\n".join(common_columns_sorted))
        # Make the comparison case-insensitive
        if column and any(column.lower() == c.lower() for c in self.common_columns):
            # Find the exact column name from the common columns
            exact_column_name = next((c for c in self.common_columns if c.lower() == column.lower()), None)
            if exact_column_name:
                self.merge_files(exact_column_name)
            else:
                messagebox.showerror("Error", "Invalid column name entered.")
        else:
            messagebox.showerror("Error", "Invalid or empty column name entered.")

    def merge_files(self, merge_column):
        try:
            combined_df = None
            for file in self.files:
                df = pd.read_csv(file) if file.endswith('.csv') else pd.read_excel(file)
                if combined_df is None:
                    combined_df = df
                else:
                    combined_df = pd.merge(combined_df, df, on=merge_column, how='outer')

            if combined_df is not None:
                self.show_merged_data(combined_df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge files: {e}")

    def show_merged_data(self, df):
        new_window = tk.Toplevel(self.root)
        new_window.title("Merged Data")
        frame = ttk.Frame(new_window)
        frame.pack(fill=tk.BOTH, expand=True)

        tree = ttk.Treeview(frame, columns=df.columns, show="headings")
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)

        for index, row in df.iterrows():
            tree.insert("", tk.END, values=list(row))

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Initialize and run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = MergeApp(root)
    root.mainloop()
