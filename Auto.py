import pyautogui
import pyperclip
import time
import os

file_path = os.path.join("contents", "1.txt")

def Auto(times=1):  # times: số lần chạy
    for i in range(times):
        try:
            print(f"▶ Chạy lần {i+1}/{times}")

            # ===== Đọc lại file mỗi lần =====
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            pyautogui.moveTo(311, 77)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)

            pyautogui.moveTo(948, 948)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)

            pyautogui.moveTo(550, 362)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(350, 521)
            #pyautogui.moveTo(384, 569)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.scroll(1000)

            pyautogui.moveTo(909, 280)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(805, 399)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(696, 442)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.mouseDown(932, 484)
            time.sleep(2)
            pyautogui.mouseUp()
            time.sleep(1)

            pyautogui.moveTo(596, 552)
            time.sleep(1)
            pyautogui.click()
            pyautogui.click()
            time.sleep(1)

            pyperclip.copy(content)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)

            pyautogui.scroll(-1000)
            time.sleep(1)
            pyautogui.moveTo(610, 633)
            time.sleep(1)
            pyautogui.click(610, 633)
            time.sleep(50)

        except Exception as e:
            print("Lỗi:", e)
            # Có thể retry hoặc bỏ qua