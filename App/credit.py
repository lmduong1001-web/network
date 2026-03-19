import json
import os
import time
import pyautogui
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

JSON_FILE = "json/credits.json"

def check_credit(driver, i):
    wait = WebDriverWait(driver, 10)

    # B1: Click icon Settings
    btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[aria-label="Settings"]')
    ))
    btn.click()

    # B2: Click menuitem Settings
    menu_item = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@role="menuitem" and contains(., "Settings")]')
    ))
    menu_item.click()

    # B3: Click tab Usage
    usage_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@role="tab" and contains(., "Usage")]')
    ))
    usage_tab.click()

    # B4: Lấy panel
    panel = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.flex-1.overflow-y-auto.overflow-x-visible')
    ))

    text = panel.get_attribute("innerText")
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    line1 = ""
    line2 = ""

    for idx in range(len(lines)):
        if "free" in lines[idx].lower() and any(char.isdigit() for char in lines[idx]):
            line1 = lines[idx]
            if idx + 1 < len(lines):
                line2 = lines[idx + 1]
            break

    # nếu không tìm thấy
    if not line1:
        line1 = "Không tìm thấy"
    if not line2:
        line2 = "Không tìm thấy"

    # ===== SAVE JSON =====
    data = {}

    # nếu file đã tồn tại thì load
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = {}

    # cập nhật theo id i
    data[str(i)] = {
        "free_line": line1,
        "date_line": line2
    }

    # ghi lại file
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)