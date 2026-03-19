import time
from selenium.webdriver.common.by import By

def bulk_delete(driver, solan):
    for lan in range(solan):
        print(f"🔁 Lần {lan + 1}/{solan}")

        TARGETS = list(range(16))  # data-index 0 → 9

        for idx in TARGETS:
            try:
                driver.execute_script("""
                    document.querySelector('button[aria-label="Select"]')?.click();
                """)
                time.sleep(0.3)

                driver.execute_script(f"""
                (() => {{
                    const row = document.querySelector('[data-index="{idx}"]');
                    if (!row) throw "Không tìm thấy row";

                    const cb =
                        row.querySelector('input[type=checkbox]') ||
                        row.querySelector('[role=checkbox]');
                    if (!cb) throw "Không tìm thấy checkbox";
                    cb.click();
                }})();
                """)
                time.sleep(0.4)

            except Exception as e:
                print(f"⚠️ Lỗi data-index {idx}: {e}")

        print("🎉 Đã chọn xong 10 item")

        driver.execute_script("""
            document.querySelector('[aria-label="Bulk delete"]')?.click();
        """)
        time.sleep(1)

        driver.find_element(
            By.XPATH, "//button[.//text()[contains(.,'Delete')]]"
        ).click()

        time.sleep(2)
