import tkinter as tk
from tkinter import ttk


from tabs import create_tab, download_tab, delete_tab
from tabs import manual_tab, edit_tab, credit_tab


root = tk.Tk()
root.title("Automation Manager")
root.geometry("1200x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

create_tab.create_tab(notebook)
download_tab.create_tab(notebook)
delete_tab.create_tab(notebook)
manual_tab.create_tab(notebook)
edit_tab.create_tab(notebook)
credit_tab.create_tab(notebook)

root.mainloop()