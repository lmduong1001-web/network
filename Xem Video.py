import os
import tkinter as tk
from tkinter import messagebox
import vlc
import time

VIDEO_EXTS = (".mp4", ".avi", ".mov", ".mkv", ".webm")
FIXED_FOLDER = r"downloads"

class VideoViewer:
    def __init__(self, root, folder):
        self.root = root
        self.folder = folder

        self.videos = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.lower().endswith(VIDEO_EXTS)
        ]
        self.videos.sort()

        self.index = 0
        self.is_paused = False

        # --- Khung hiển thị video ---
        self.video_frame = tk.Frame(root, bg="black")
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        # --- Nút điều khiển ---
        ctrl = tk.Frame(root)
        ctrl.pack(fill=tk.X, pady=5)

        tk.Button(ctrl, text="⬆ Video trước", width=12, command=self.prev_video).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="❌ Xóa", width=12, fg="red", command=self.delete_video).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="⬇ Video sau", width=12, command=self.next_video).pack(side=tk.LEFT, padx=5)

        # --- VLC ---
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.root.update()
        self.player.set_hwnd(self.video_frame.winfo_id())  # Windows

        # --- Phím tắt ---
        root.bind("<Up>", lambda e: self.prev_video())
        root.bind("<Down>", lambda e: self.next_video())
        root.bind("<Delete>", lambda e: self.delete_video())
        root.bind("<space>", lambda e: self.toggle_pause())

        if self.videos:
            self.play_video()
        else:
            self.root.title("Không có video trong thư mục")

    def play_video(self):
        if not self.videos:
            return

        video = self.videos[self.index]
        media = self.instance.media_new(video)
        self.player.set_media(media)
        self.player.play()

        time.sleep(0.1)

        self.root.title(
            f"Video {self.index + 1}/{len(self.videos)} - {os.path.basename(video)}"
        )

        self.is_paused = False

    def toggle_pause(self):
        if self.player.is_playing():
            self.player.pause()
            self.is_paused = True
        else:
            self.player.play()
            self.is_paused = False

    def prev_video(self):
        if self.index > 0:
            self.index -= 1
            self.player.stop()
            self.play_video()

    def next_video(self):
        if self.index < len(self.videos) - 1:
            self.index += 1
            self.player.stop()
            self.play_video()

    def delete_video(self):
        if not self.videos:
            return

        video = self.videos[self.index]

        try:
            self.player.stop()
            os.remove(video)
            del self.videos[self.index]

            if self.index >= len(self.videos) and self.index > 0:
                self.index -= 1

            if self.videos:
                self.play_video()
            else:
                self.root.title("Hết video")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))


# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    root.title("Video Viewer")

    if not os.path.isdir(FIXED_FOLDER):
        messagebox.showerror("Lỗi", f"Không tồn tại thư mục:\n{FIXED_FOLDER}")
    else:
        VideoViewer(root, FIXED_FOLDER)
        root.mainloop()
