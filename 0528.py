import tkinter as tk
from tkinter import messagebox
import time

class FocusClock:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟")
        self.root.geometry("400x300")

        self.focus_time = 25 * 60  # 默认专注时间为25分钟
        self.break_time = 5 * 60  # 默认休息时间为5分钟
        self.remaining_time = self.focus_time
        self.is_running = False
        self.is_focus_time = True

        self.create_widgets()

    def create_widgets(self):
        self.time_label = tk.Label(self.root, text=self.format_time(self.remaining_time), font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="开始", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(self.root, text="暂停", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(self.root, text="重置", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=20)

        self.focus_entry = tk.Entry(self.root, width=5)
        self.focus_entry.insert(0, "25")
        self.focus_entry.pack(side=tk.LEFT, padx=5)
        self.focus_label = tk.Label(self.root, text="分钟专注")
        self.focus_label.pack(side=tk.LEFT, padx=5)

        self.break_entry = tk.Entry(self.root, width=5)
        self.break_entry.insert(0, "5")
        self.break_entry.pack(side=tk.LEFT, padx=5)
        self.break_label = tk.Label(self.root, text="分钟休息")
        self.break_label.pack(side=tk.LEFT, padx=5)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def pause_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.focus_time = int(self.focus_entry.get()) * 60
        self.break_time = int(self.break_entry.get()) * 60
        self.remaining_time = self.focus_time if self.is_focus_time else self.break_time
        self.time_label.config(text=self.format_time(self.remaining_time))

    def update_timer(self):
        if self.is_running:
            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.time_label.config(text=self.format_time(self.remaining_time))
                self.root.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.is_focus_time = not self.is_focus_time
                self.remaining_time = self.focus_time if self.is_focus_time else self.break_time
                self.time_label.config(text=self.format_time(self.remaining_time))
                session_type = "专注时间" if self.is_focus_time else "休息时间"
                messagebox.showinfo("提示", f"{session_type}结束了！")
                self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusClock(root)
    root.mainloop()
