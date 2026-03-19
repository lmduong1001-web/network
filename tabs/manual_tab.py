import tkinter as tk
from tkinter import messagebox
from App.utils import *
from App.Driver_Setting import open_profile

stt = 21
URL = "https://sora.chatgpt.com/drafts"

manual_drivers = {}

def create_tab(notebook):
    tab = tk.Frame(notebook)
    notebook.add(tab, text="Manual")

    tk.Label(tab, text="PROFILE ID (1 cái)").pack()

    vars_ = create_checkbox_grid(tab, range(1, stt), single=True)

    def open_manual():
        for pid in get_checked(vars_):
            if pid in manual_drivers:
                messagebox.showinfo("Info", "Đã mở")
                return
            driver = open_profile(pid, URL)
            manual_drivers[pid] = driver

    def close_manual():
        for pid in get_checked(vars_):
            driver = manual_drivers.get(pid)
            if driver:
                driver.quit()
                del manual_drivers[pid]

    tk.Button(tab, text="🟢 OPEN", bg="green", fg="white",
              width=30, command=open_manual).pack(pady=5)

    tk.Button(tab, text="🔴 CLOSE", bg="red", fg="white",
              width=30, command=close_manual).pack(pady=5)

    return tab