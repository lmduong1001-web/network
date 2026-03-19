import tkinter as tk
from tkinter import messagebox
from App.utils import *
from App.driver_manager import run_with_driver
from App.bulk_delete import bulk_delete

stt = 21

def create_tab(notebook):
    tab = tk.Frame(notebook)
    notebook.add(tab, text="Delete")

    tk.Label(tab, text="PROFILE ID").pack()
    vars_ = create_checkbox_grid(tab, range(1, stt))
    create_select_buttons(tab, vars_)

    def run():
        profiles = get_checked(vars_)
        if not profiles:
            messagebox.showwarning("Thiếu", "Chưa chọn profile")
            return

        for pid in profiles:
            run_with_driver(pid, bulk_delete, solan=1)

    tk.Button(tab, text="🗑 RUN DELETE",
              bg="red", fg="white",
              width=30, command=run).pack(pady=15)

    return tab