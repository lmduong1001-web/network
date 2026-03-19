import tkinter as tk
import os
import time
from tkinter import messagebox

from App.utils import get_checked, create_select_buttons, load_credits
from App.driver_manager import run_with_driver
from App.poster import post_text

CONTENT_DIR = "contents"
stt = 21


# ================= CREATE CHECKBOX PROFILE + CREDIT =================
def create_profile_with_credit(parent, items, credits, rows_per_col=10):
    frame = tk.Frame(parent)
    frame.pack(pady=5)

    vars_dict = {}

    for idx, item in enumerate(items):
        var = tk.IntVar()

        item_frame = tk.Frame(frame)

        # 👉 LẤY CREDIT JSON
        info = credits.get(str(item), {})
        free_line = info.get("free_line", "")
        date_line = info.get("date_line", "")

        # 👉 TEXT HIỂN THỊ 1 DÒNG
        text = f"{item}   {free_line} | {date_line}" if free_line else str(item)

        # 👉 MÀU (hết free = đỏ)
        color = "red" if "0 free" in free_line else "black"

        cb = tk.Checkbutton(
            item_frame,
            text=text,
            fg=color,
            variable=var,
            anchor="w",
            justify="left"
        )
        cb.pack(anchor="w")

        # 👉 CHIA CỘT: 1–10 / 11–20
        col = idx // rows_per_col
        row = idx % rows_per_col

        item_frame.grid(row=row, column=col, padx=20, pady=3, sticky="w")

        vars_dict[item] = var

    return vars_dict


# ================= TAB =================
def create_tab(notebook):
    tab = tk.Frame(notebook)
    notebook.add(tab, text="Create Videos")

    # ================= PROFILE =================
    tk.Label(tab, text="PROFILE ID").pack()

    credits_data = load_credits()

    profile_vars = create_profile_with_credit(
        tab,
        range(1, stt),
        credits_data
    )

    create_select_buttons(tab, profile_vars)

    # ================= CONTENT =================
    tk.Label(tab, text="CONTENT (.txt)").pack(pady=(10, 0))

    content_files = sorted(
        f for f in os.listdir(CONTENT_DIR) if f.endswith(".txt")
    )
    content_ids = [f.replace(".txt", "") for f in content_files]

    content_vars = {}
    content_frame = tk.Frame(tab)
    content_frame.pack(pady=5)

    for cid in content_ids:
        var = tk.IntVar()
        cb = tk.Checkbutton(
            content_frame,
            text=cid,
            variable=var,
            width=10
        )
        cb.pack(side="left", padx=5)
        content_vars[cid] = var

    # ================= RUN =================
    repeat_var = tk.IntVar()

    def run_create():
        profiles = get_checked(profile_vars)
        contents = get_checked(content_vars)

        if not profiles or not contents:
            messagebox.showwarning("Thiếu", "Chọn profile và content")
            return

        rounds = 3 if repeat_var.get() else 1

        for round_idx in range(rounds):
            print(f"\n🔁 ROUND {round_idx + 1}/{rounds}")

            for idx, cid in enumerate(contents):
                print(f"\n▶ CONTENT: {cid}")

                path = os.path.join(CONTENT_DIR, f"{cid}.txt")
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                for pid in profiles:
                    print(f"➡ Profile {pid}")
                    run_with_driver(pid, post_text, content, 15)
                    time.sleep(2)

                # nghỉ giữa content
                if idx < len(contents) - 1:
                    print("⏸ Nghỉ 60s...")
                    time.sleep(60)

            # nghỉ giữa vòng
            if round_idx < rounds - 1:
                print("🕒 Nghỉ 60s trước vòng tiếp...")
                time.sleep(60)

    tk.Checkbutton(
        tab,
        text="🔁 Chạy lại nhiều lần",
        variable=repeat_var
    ).pack(pady=5)

    tk.Button(
        tab,
        text="▶ RUN CREATE",
        bg="green",
        fg="white",
        width=30,
        command=run_create
    ).pack(pady=15)

    return tab