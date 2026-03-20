import undetected_chromedriver as uc
import os
import json
import time
import pyautogui
import winreg
def get_chrome_version():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Google\Chrome\BLBeacon"
        )
        version, _ = winreg.QueryValueEx(key, "version")
        return int(version.split(".")[0])
    except:
        return None

def open_profile(i, website_url, headless=False):
    chrome_version = get_chrome_version()
    if chrome_version is None:
        raise Exception("Không tìm thấy Chrome")

    json_file = f"./profile/profile_{i}.json"

    with open(json_file, "r", encoding="utf-8") as file:
        config = json.load(file)

    user_agent = config["user_agent"]

    profile_path = os.path.abspath(f"./data/profile_{i}")

    options = uc.ChromeOptions()
    #options.add_argument("--start-fullscreen")
    if headless:
        options.add_argument("--headless=new")
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(
        options=options,
        version_main=chrome_version - 1,      # 👈 ÉP CHROMEDRIVER 144
        use_subprocess=True
    )
    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {"userAgent": user_agent}
    )

    driver.get("https://sora.chatgpt.com/drafts")
    time.sleep(3)
    return driver