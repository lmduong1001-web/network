import time
import pyautogui
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def post_text(driver, text, solan):
    pyperclip.copy(text)

    for _ in range(1):
        textarea = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Describe your video...']")
            )
        )

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
            pyautogui.moveTo(click_x, click_y, duration=0.2)
            pyautogui.click()
            time.sleep(1)

            pyautogui.hotkey("ctrl", "a")
            time.sleep(1)

            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)

            pyautogui.press("enter")
            time.sleep(60)