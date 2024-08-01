import tkinter as tk
from tkinter import messagebox
import threading
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟")
        self.root.geometry("300x200")
        
        self.timer_running = False
        self.timer_paused = False
        self.work_duration = 45 * 60  # 45 minutes
        self.break_duration = 10 * 60  # 10 minutes
        self.remaining_time = self.work_duration
        self.is_work_time = True

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="45:00", font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(self.root, text="开始", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20)
        
        self.pause_button = tk.Button(self.root, text="暂停", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=20)
        
        self.reset_button = tk.Button(self.root, text="重置", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()

    def pause_timer(self):
        if self.timer_running:
            self.timer_paused = not self.timer_paused
            if self.timer_paused:
                self.pause_button.config(text="继续")
            else:
                self.pause_button.config(text="暂停")
                self.update_timer()

    def reset_timer(self):
        self.timer_running = False
        self.timer_paused = False
        self.is_work_time = True
        self.remaining_time = self.work_duration
        self.label.config(text="45:00")
        self.pause_button.config(text="暂停")

    def update_timer(self):
        if self.timer_running and not self.timer_paused:
            if self.remaining_time > 0:
                mins, secs = divmod(self.remaining_time, 60)
                time_format = '{:02d}:{:02d}'.format(mins, secs)
                self.label.config(text=time_format)
                self.remaining_time -= 1
                self.root.after(1000, self.update_timer)
            else:
                if self.is_work_time:
                    messagebox.showinfo("时间到", "休息时间到！")
                    self.remaining_time = self.break_duration
                    self.is_work_time = False
                else:
                    messagebox.showinfo("时间到", "工作时间到！")
                    self.remaining_time = self.work_duration
                    self.is_work_time = True
                self.update_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
