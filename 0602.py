import tkinter as tk
from datetime import datetime
import time
import threading

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")

        self.state = None
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.long_break_time = 15 * 60  # 15 minutes
        self.reps = 0

        self.timer_label = tk.Label(text="专注时钟", font=("Arial", 50))
        self.timer_label.pack()

        self.start_button = tk.Button(text="开始", command=self.start_timer)
        self.start_button.pack()

        self.reset_button = tk.Button(text="重置", command=self.reset_timer)
        self.reset_button.pack()

        self.clock_label = tk.Label(text="00:00", font=("Arial", 48))
        self.clock_label.pack()

    def start_timer(self):
        self.reps += 1
        work_sec = self.work_time
        short_break_sec = self.break_time
        long_break_sec = self.long_break_time

        if self.reps % 8 == 0:
            self.countdown(long_break_sec)
            self.state = '长休息'
        elif self.reps % 2 == 0:
            self.countdown(short_break_sec)
            self.state = '短休息'
        else:
            self.countdown(work_sec)
            self.state = '工作'

    def countdown(self, count):
        count_min = count // 60
        count_sec = count % 60
        self.clock_label['text'] = f"{count_min:02d}:{count_sec:02d}"
        if count > 0:
            self.master.after(1000, self.countdown, count - 1)
        else:
            self.start_timer()

    def reset_timer(self):
        self.timer_label.config(text="专注时钟")
        self.clock_label.config(text="00:00")
        self.reps = 0
        self.state = None

def main():
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
