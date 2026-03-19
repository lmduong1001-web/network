import tkinter as tk
from tkinter import ttk, messagebox
import os
import time
from App.Driver_Setting import open_profile
from App.poster import post_text
from App.bulk_delete import bulk_delete
from App.video_downloader import download_latest_videos

URL = "https://sora.chatgpt.com/drafts"
CONTENT_DIR = "contents"
stt = 11

# ================= DRIVER =================
def run_with_driver(profile_id, action, *args, headless=False, **kwargs):
    driver = None
    try:
        print(f"🚀 Profile {profile_id} | Start")
        driver = open_profile(profile_id, URL, headless=headless)
        action(driver, *args, **kwargs)
    except Exception as e:
        print(f"❌ Profile {profile_id} | Lỗi: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"🧹 Profile {profile_id} | Closed")


# ================= MANUAL DRIVER =================
manual_drivers = {}


def open_profile_manual(profile_id):
    if profile_id in manual_drivers:
        messagebox.showinfo("Info", f"Profile {profile_id} đã mở rồi")
        return
    try:
        print(f"🟢 Manual Open | Profile {profile_id}")
        driver = open_profile(profile_id, URL, headless=False)
        manual_drivers[profile_id] = driver
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def close_profile_manual(profile_id):
    driver = manual_drivers.get(profile_id)
    if not driver:
        messagebox.showwarning("Info", f"Profile {profile_id} chưa mở")
        return
    try:
        driver.quit()
    finally:
        del manual_drivers[profile_id]
        print(f"🔴 Manual Close | Profile {profile_id}")


# ================= UTILS =================
def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_txt(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def get_checked(vars_dict):
    return [k for k, v in vars_dict.items() if v.get() == 1]


def select_all(vars_dict):
    for v in vars_dict.values():
        v.set(1)


def clear_all(vars_dict):
    for v in vars_dict.values():
        v.set(0)


def create_checkbox_row(parent, items, single=False, callback=None):
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

    for item in items:
        var = tk.IntVar()
        cb = tk.Checkbutton(
            frame,
            text=str(item),
            variable=var,
            width=3,
            command=lambda i=item: on_click(i)
        )
        cb.pack(side="left", padx=5)
        vars_dict[item] = var

    return vars_dict


def create_select_buttons(parent, vars_dict):
    frame = tk.Frame(parent)
    frame.pack(pady=5)

    tk.Button(
        frame, text="✔ Chọn tất cả",
        command=lambda: select_all(vars_dict),
        width=15
    ).pack(side="left", padx=5)

    tk.Button(
        frame, text="✖ Bỏ chọn tất cả",
        command=lambda: clear_all(vars_dict),
        width=15
    ).pack(side="left", padx=5)


# ================= UI =================
root = tk.Tk()
root.title("Automation Manager")
root.geometry("1920x560")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# =====================================================
# ================= CREATE TAB =========================
# =====================================================
tab_create = tk.Frame(notebook)
notebook.add(tab_create, text="Create Videos")

tk.Label(tab_create, text="PROFILE ID").pack()
profile_vars = create_checkbox_row(tab_create, range(1, stt))
create_select_buttons(tab_create, profile_vars)

tk.Label(tab_create, text="CONTENT (.txt)").pack(pady=(10, 0))

content_files = sorted(f for f in os.listdir(CONTENT_DIR) if f.endswith(".txt"))
content_ids = [f.replace(".txt", "") for f in content_files]
content_vars = create_checkbox_row(tab_create, content_ids)


def run_create():
    profiles = get_checked(profile_vars)
    contents = get_checked(content_vars)

    if not profiles or not contents:
        messagebox.showwarning("Thiếu", "Chọn profile và content")
        return

    # Nếu check thì chạy 30 lần, không thì chạy 1 lần
    total_rounds = 3 if repeat_30_var.get() == 1 else 1

    for round_idx in range(total_rounds):
        print(f"\n==============================")
        print(f"🔁 VÒNG CHẠY: {round_idx + 1}/{total_rounds}")
        print(f"==============================")

        for idx, cid in enumerate(contents):
            print(f"\n▶ CONTENT: {cid}")

            content_path = os.path.join(CONTENT_DIR, f"{cid}.txt")
            content = read_txt(content_path)

            for pid in profiles:
                print(f"➡ Profile {pid} | Content {cid}")
                run_with_driver(pid, post_text, content, 15)
                time.sleep(3)

            # Nghỉ giữa content (trừ content cuối)
            if idx < len(contents) - 1:
                print("⏸️ Nghỉ 5 phút trước content tiếp theo...\n")
                time.sleep(60)

        # Nghỉ giữa mỗi vòng (trừ vòng cuối)
        if round_idx < total_rounds - 1:
            print("🕒 Nghỉ 5 phút trước khi chạy lại vòng tiếp theo...\n")
            time.sleep(60)

repeat_30_var = tk.IntVar()

tk.Checkbutton(
    tab_create,
    text="🔁 Chạy lại 30 lần",
    variable=repeat_30_var
).pack(pady=5)

tk.Button(
    tab_create, text="▶ RUN CREATE",
    bg="green", fg="white",
    width=30, command=run_create
).pack(pady=15)


# =====================================================
# ================= DOWNLOAD TAB ======================
# =====================================================
tab_download = tk.Frame(notebook)
notebook.add(tab_download, text="Download")

tk.Label(tab_download, text="PROFILE ID").pack()
download_vars = create_checkbox_row(tab_download, range(1, stt))
create_select_buttons(tab_download, download_vars)


def run_download():
    profiles = get_checked(download_vars)
    if not profiles:
        messagebox.showwarning("Thiếu", "Chưa chọn profile")
        return
    for pid in profiles:
        run_with_driver(pid, download_latest_videos, pid, limit=30, headless=False)


tk.Button(
    tab_download, text="⬇ RUN DOWNLOAD",
    bg="blue", fg="white",
    width=30, command=run_download
).pack(pady=15)


# =====================================================
# ================= DELETE TAB ========================
# =====================================================
tab_delete = tk.Frame(notebook)
notebook.add(tab_delete, text="Delete")

tk.Label(tab_delete, text="PROFILE ID").pack()
delete_vars = create_checkbox_row(tab_delete, range(1, stt))
create_select_buttons(tab_delete, delete_vars)


def run_delete():
    profiles = get_checked(delete_vars)
    if not profiles:
        messagebox.showwarning("Thiếu", "Chưa chọn profile")
        return
    for pid in profiles:
        run_with_driver(pid, bulk_delete, solan=1, headless=False)


tk.Button(
    tab_delete, text="🗑 RUN DELETE",
    bg="red", fg="white",
    width=30, command=run_delete
).pack(pady=15)


# =====================================================
# ================= MANUAL TAB ========================
# =====================================================
tab_manual = tk.Frame(notebook)
notebook.add(tab_manual, text="Manual")

tk.Label(tab_manual, text="PROFILE ID (chọn 1)").pack(pady=5)

manual_vars = create_checkbox_row(tab_manual, range(1, stt), single=True)

tk.Button(
    tab_manual,
    text="🟢 MỞ PROFILE (TỰ THAO TÁC)",
    bg="darkgreen",
    fg="white",
    width=35,
    command=lambda: [
        open_profile_manual(pid)
        for pid in get_checked(manual_vars)
    ]
).pack(pady=10)

tk.Button(
    tab_manual,
    text="🔴 ĐÓNG PROFILE",
    bg="darkred",
    fg="white",
    width=35,
    command=lambda: [
        close_profile_manual(pid)
        for pid in get_checked(manual_vars)
    ]
).pack(pady=5)


# =====================================================
# ================= EDIT CONTENT TAB ==================
# =====================================================
tab_edit = tk.Frame(notebook)
notebook.add(tab_edit, text="Edit Contents")

tk.Label(tab_edit, text="CHỌN 1 CONTENT ĐỂ SỬA").pack(pady=5)

selected_content = {"id": None}


def load_content(cid):
    if content_edit_vars[cid].get() == 1:
        path = os.path.join(CONTENT_DIR, f"{cid}.txt")
        if not os.path.exists(path):
            return
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, read_txt(path))
        selected_content["id"] = cid


content_edit_vars = create_checkbox_row(
    tab_edit,
    content_ids,
    single=True,
    callback=load_content
)

text_box = tk.Text(tab_edit, height=15, width=110)
text_box.pack(padx=10, pady=10)


def save_content():
    cid = selected_content["id"]
    if not cid:
        messagebox.showwarning("Thiếu", "Chưa chọn content")
        return
    path = os.path.join(CONTENT_DIR, f"{cid}.txt")
    write_txt(path, text_box.get("1.0", tk.END).strip())


tk.Button(
    tab_edit, text="💾 SAVE CONTENT",
    bg="orange", fg="black",
    width=30, command=save_content
).pack(pady=10)


root.mainloop()
