import pyautogui
import time

def Auto(times=1):  # times: số lần chạy
    for i in range(times):
        try:
            print(f"⬇ Chạy lần {i+1}/{times}")

            time.sleep(2)  # delay trước khi chạy

            pyautogui.moveTo(687, 196)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)

            pyautogui.moveTo(599, 298)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)

            pyautogui.moveTo(687, 196)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(632, 346)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            pyautogui.moveTo(1060, 608)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)

        except Exception as e:
            print("Lỗi:", e)
            # Có thể retry hoặc bỏ qua