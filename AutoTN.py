import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import Auto
import Download
import os
import time

file_path = os.path.join("contents", "1.txt")

# ===== Biến global để dừng =====
stop_flag = False

# ===== Hàm load file =====
def load_file():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)
    except:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Không đọc được file!")

# ===== Hàm save file =====
def save_file():
    try:
        content = text_box.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        messagebox.showinfo("✅", "Lưu file thành công!")
    except:
        messagebox.showerror("❌", "Lưu file thất bại!")

# ===== Hàm dừng =====
def stop_all():
    global stop_flag
    stop_flag = True
    status_label.config(text="⏹ Đã bấm STOP!")

# ===== Hàm chạy Create (thread) =====
def run_create():
    time.sleep(10)
    global stop_flag
    try:
        raw = entry.get().strip()  # loại bỏ khoảng trắng
        if not raw.isdigit():
            raise ValueError("Không phải số nguyên dương")
        count = int(raw)
        if count <= 0:
            raise ValueError("Số phải > 0")

        stop_flag = False
        status_label.config(text="⏳ Đang tạo video...")
        Auto.Auto(times=count)
        status_label.config(text="✅ Tạo video xong!")

    except ValueError as ve:
        messagebox.showerror("Lỗi", f"Nhập số hợp lệ!\nChi tiết: {ve}")

# ===== Hàm chạy Download (thread) =====
def run_download():
    time.sleep(10)
    global stop_flag
    try:
        raw = entry.get().strip()  # loại bỏ khoảng trắng
        if not raw.isdigit():
            raise ValueError("Không phải số nguyên dương")
        count = int(raw)
        if count <= 0:
            raise ValueError("Số phải > 0")

        stop_flag = False
        status_label.config(text="⏳ Đang tải video...")
        Download.Auto(times=count)
        status_label.config(text="✅ Tải xong!")

    except ValueError as ve:
        messagebox.showerror("Lỗi", f"Nhập số hợp lệ!\nChi tiết: {ve}")

# ===== Threaded start =====
def start_create():
    threading.Thread(target=run_create).start()

def start_download():
    threading.Thread(target=run_download).start()

# ===== UI =====
root = tk.Tk()
root.title("Auto Tool")
root.geometry("700x700")

tk.Label(root, text="Nhập số lần chạy:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

btn_create = tk.Button(root, text="🎬 Create Video", command=start_create)
btn_create.pack(pady=5)

btn_download = tk.Button(root, text="⬇ Download Video", command=start_download)
btn_download.pack(pady=5)

btn_stop = tk.Button(root, text="⏹ STOP tất cả", fg="red", command=stop_all)
btn_stop.pack(pady=5)

status_label = tk.Label(root, text="Sẵn sàng", fg="blue")
status_label.pack(pady=10)

tk.Label(root, text="Chỉnh sửa nội dung ./contents/1.txt:").pack(pady=5)
text_box = scrolledtext.ScrolledText(root, width=60, height=15)
text_box.pack(pady=5)

btn_save = tk.Button(root, text="💾 Save File", command=save_file)
btn_save.pack(pady=5)

load_file()
root.mainloop()