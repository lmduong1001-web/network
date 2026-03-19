import tkinter as tk
import os
from tkinter import messagebox
from App.utils import *

CONTENT_DIR = "contents"

def create_tab(notebook):
    tab = tk.Frame(notebook)
    notebook.add(tab, text="Edit")

    files = sorted(f for f in os.listdir(CONTENT_DIR) if f.endswith(".txt"))
    ids = [f.replace(".txt", "") for f in files]

    selected = {"id": None}

    def load(cid):
        path = os.path.join(CONTENT_DIR, f"{cid}.txt")
        with open(path, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
        selected["id"] = cid

    vars_ = create_checkbox_grid(tab, ids, single=True, callback=load)

    text = tk.Text(tab, height=15, width=100)
    text.pack()

    def save():
        if not selected["id"]:
            return
        path = os.path.join(CONTENT_DIR, f"{selected['id']}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

    tk.Button(tab, text="💾 SAVE", bg="orange",
              width=30, command=save).pack(pady=10)

    return tab