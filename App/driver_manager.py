from App.Driver_Setting import open_profile

URL = "https://sora.chatgpt.com/drafts"

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