import pyautogui
import pyperclip
import time
import os

# ===== Đường dẫn file =====
file_path = os.path.join("contents", "1.txt")

# ===== Đọc nội dung file =====
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

time.sleep(10)
def Auto():
# ===== Delay để bạn chuyển sang màn hình cần paste =====
    pyautogui.moveTo(311, 77)
    time.sleep(1)
    pyautogui.click(311, 77)
    time.sleep(3)
    pyautogui.moveTo(948, 948)
    time.sleep(1)
    pyautogui.click(948, 948)
    time.sleep(2)
    
    pyautogui.moveTo(550, 362)
    time.sleep(1)
    pyautogui.click(550, 362)
    time.sleep(1)
    pyautogui.moveTo(437, 574)
    time.sleep(1)
    pyautogui.click(437, 574)
    time.sleep(1)

    pyautogui.scroll(1000)
    pyautogui.moveTo(909, 280)
    time.sleep(1)
    pyautogui.click(909, 280)
    time.sleep(1)
    pyautogui.moveTo(805, 399)
    time.sleep(1)
    pyautogui.click(805, 399)
    time.sleep(1)
    pyautogui.moveTo(696, 442)
    time.sleep(1)
    pyautogui.click(696, 442)
    time.sleep(1)
    pyautogui.mouseDown(932, 484)  # nhấn giữ chuột
    time.sleep(2)              # giữ 2 giây
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.moveTo(596, 552)
    time.sleep(1)
    pyautogui.click(596, 552)
    time.sleep(1)
    pyautogui.click(596, 552)
    time.sleep(1)
    pyperclip.copy(content)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    pyautogui.click(610, 633)
    time.sleep(60)

while True:
    Auto()