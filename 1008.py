import tkinter as tk
from datetime import timedelta

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟")
        
        self.work_time = 45 * 60  # 45 minutes in seconds
        self.short_break = 10 * 60  # 10 minutes in seconds
        self.long_break = 20 * 60  # 20 minutes in seconds
        self.current_time = self.work_time
        self.timer_running = False
        self.reps = 0
        
        self.label = tk.Label(root, text="专注时钟", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.timer_label = tk.Label(root, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.timer_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="开始", command=self.start_timer)
        self.start_button.pack(side="left", padx=20)

        self.pause_button = tk.Button(root, text="暂停", command=self.pause_timer)
        self.pause_button.pack(side="left", padx=20)

        self.reset_button = tk.Button(root, text="重置", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=20)

    def format_time(self, seconds):
        return str(timedelta(seconds=seconds))

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.current_time = self.work_time
        self.reps = 0
        self.timer_label.config(text=self.format_time(self.current_time))
        self.label.config(text="专注时钟")

    def update_timer(self):
        if self.timer_running and self.current_time > 0:
            self.current_time -= 1
            self.timer_label.config(text=self.format_time(self.current_time))
            self.root.after(1000, self.update_timer)
        elif self.current_time == 0:
            self.timer_running = False
            self.reps += 1
            if self.reps % 8 == 0:
                self.current_time = self.long_break
                self.label.config(text="长休息")
            elif self.reps % 2 == 0:
                self.current_time = self.short_break
                self.label.config(text="短休息")
            else:
                self.current_time = self.work_time
                self.label.config(text="专注时钟")
            self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()
