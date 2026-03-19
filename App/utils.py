import tkinter as tk
import json

def load_credits(path="json/credits.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
        
def get_checked(vars_dict):
    return [k for k, v in vars_dict.items() if v.get() == 1]

def select_all(vars_dict):
    for v in vars_dict.values():
        v.set(1)

def clear_all(vars_dict):
    for v in vars_dict.values():
        v.set(0)

def create_checkbox_grid(parent, items, rows_per_col=10, single=False, callback=None, labels=None):
    frame = tk.Frame(parent)
    frame.pack(pady=5)

    vars_dict = {}

    def on_click(current):
        if single:
            for k, v in vars_dict.items():
                if k != current:
                    v.set(0)
        if callback:
            callback(current)

    for idx, item in enumerate(items):
        var = tk.IntVar()

        item_frame = tk.Frame(frame)

        # 👉 LẤY DATA JSON
        text_extra = ""
        if labels and str(item) in labels:
            info = labels[str(item)]
            free_line = info.get("free_line", "")
            date_line = info.get("date_line", "")
            text_extra = f"{free_line} | {date_line}"

        # 👉 TEXT 1 DÒNG
        full_text = f"{item}   {text_extra}" if text_extra else str(item)

        cb = tk.Checkbutton(
            item_frame,
            text=full_text,
            variable=var,
            anchor="w",
            justify="left",
            command=lambda i=item: on_click(i)
        )
        cb.pack(anchor="w")

        # 👉 CHIA CỘT 1-10 / 11-20
        col = idx // rows_per_col
        row = idx % rows_per_col

        item_frame.grid(row=row, column=col, padx=20, pady=3, sticky="w")

        vars_dict[item] = var

    return vars_dict
def create_select_buttons(parent, vars_dict):
    frame = tk.Frame(parent)
    frame.pack(pady=5)

    tk.Button(frame, text="✔ Chọn tất cả",
              command=lambda: select_all(vars_dict),
              width=15).pack(side="left", padx=5)

    tk.Button(frame, text="✖ Bỏ chọn tất cả",
              command=lambda: clear_all(vars_dict),
              width=15).pack(side="left", padx=5)