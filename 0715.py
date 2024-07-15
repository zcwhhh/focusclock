import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.work_time = 25 * 60
        self.short_break_time = 5 * 60
        self.long_break_time = 15 * 60
        self.cycles = 4

        self.current_cycle = 0
        self.is_running = False

        self.label = tk.Label(master, text="Pomodoro Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.timer_label = tk.Label(master, text=self.format_time(self.work_time), font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=10)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f'{mins:02d}:{secs:02d}'

    def update_timer(self):
        if self.is_running:
            if self.current_cycle % 2 == 0:  # Work time
                self.work_time -= 1
                self.timer_label.config(text=self.format_time(self.work_time))
                if self.work_time == 0:
                    self.is_running = False
                    self.current_cycle += 1
                    messagebox.showinfo("Break Time", "Time for a short break!")
                    self.work_time = 25 * 60
                    self.short_break_time = 5 * 60
                    self.start_timer()
            elif self.current_cycle % 2 != 0 and self.current_cycle % 7 != 0:  # Short break
                self.short_break_time -= 1
                self.timer_label.config(text=self.format_time(self.short_break_time))
                if self.short_break_time == 0:
                    self.is_running = False
                    self.current_cycle += 1
                    messagebox.showinfo("Work Time", "Time to get back to work!")
                    self.short_break_time = 5 * 60
                    self.start_timer()
            else:  # Long break
                self.long_break_time -= 1
                self.timer_label.config(text=self.format_time(self.long_break_time))
                if self.long_break_time == 0:
                    self.is_running = False
                    self.current_cycle = 0
                    messagebox.showinfo("Work Time", "Time to get back to work!")
                    self.long_break_time = 15 * 60
                    self.start_timer()

            self.master.after(1000, self.update_timer)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.current_cycle = 0
        self.work_time = 25 * 60
        self.short_break_time = 5 * 60
        self.long_break_time = 15 * 60
        self.timer_label.config(text=self.format_time(self.work_time))

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro = PomodoroTimer(root)
    root.mainloop()
