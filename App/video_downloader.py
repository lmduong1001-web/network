# App/video_downloader.py
import os
import requests
from selenium.webdriver.common.by import By

def download_file(url, output_path):
    r = requests.get(url, stream=True, timeout=30)
    r.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in r.iter_content(8192):
            if chunk:
                f.write(chunk)


def download_latest_videos(driver, profile_id, limit=10):
    parent = driver.find_element(By.CSS_SELECTOR, "div.w-full")
    items = parent.find_elements(By.CSS_SELECTOR, "div[data-index]")

    video_sources = []

    for item in items:
        videos = item.find_elements(By.TAG_NAME, "video")
        for v in videos:
            src = v.get_attribute("src")
            if src:
                video_sources.append(src)

    video_sources = video_sources[:limit]

    folder = "downloads/0"
    os.makedirs(folder, exist_ok=True)
    for i, link in enumerate(video_sources, 1):
        ext = link.split("?")[0].split(".")[-1]
        if len(ext) > 5:
            ext = "mp4"

        save_path = f"{folder}/{profile_id}_{i}.{ext}"
        download_file(link, save_path)
        print("⬇️ Đã tải:", save_path)
