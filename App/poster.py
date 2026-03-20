import time
import pyautogui
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from App.credit import check_credit

def post_text(driver, text, solan, pid):
    pyperclip.copy(text)

    max_retry = 3
    attempt = 0

    while attempt < max_retry:
        try:
            print(f"🔄 Thử lần {attempt + 1}")

            textarea = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//textarea[@placeholder='Describe your video...']")
                )
            )

            # Nếu tìm thấy thì break khỏi retry
            print("✅ Đã tìm thấy textarea")
            break

        except Exception as e:
            print(f"❌ Không thấy textarea, thử lại... ({attempt + 1}/3)")
            attempt += 1
            time.sleep(3)

            if attempt == max_retry:
                raise Exception("❌ Lỗi: Không tìm thấy textarea sau 3 lần thử")

    # ===== Nếu tới đây nghĩa là đã tìm thấy =====
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        textarea
    )
    time.sleep(1)

    box = textarea.location
    size = textarea.size

    center_x = box["x"] + size["width"] / 2
    center_y = box["y"] + size["height"] / 2

    window_pos = driver.get_window_position()
    click_x = window_pos["x"] + center_x
    click_y = window_pos["y"] + center_y + 100

    for i in range(solan):
        print(f"✏️ Gửi lần {i+1}/{solan}")

        pyautogui.moveTo(click_x, click_y, duration=0.2)
        pyautogui.click()
        time.sleep(1)

        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        pyautogui.press("enter")
        time.sleep(90)

    check_credit(driver, pid)