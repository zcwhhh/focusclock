import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Pomodoro Timer")

        self.default_work_time = 45 * 60
        self.default_short_break_time = 10 * 60
        self.default_long_break_time = 30 * 60
        self.cycle = 3

        self.is_running = False
        self.timer = None
        self.current_cycle = 0
        self.current_phase = 'work'

        # Set up UI
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Welcome to Pomodoro Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.time_label = tk.Label(self.root, text="45:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(pady=5)

        self.customize_button = tk.Button(self.root, text="Customize", command=self.customize_timer, font=("Helvetica", 14))
        self.customize_button.pack(pady=5)

        self.progress_label = tk.Label(self.root, text="Cycle: 0", font=("Helvetica", 14))
        self.progress_label.pack(pady=5)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_next_phase()

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.is_running = False
        self.current_cycle = 0
        self.current_phase = 'work'
        self.time_label.config(text="45:00")
        self.label.config(text="Welcome to Pomodoro Timer")
        self.progress_label.config(text="Cycle: 0")

    def customize_timer(self):
        self.is_running = False
        if self.timer:
            self.root.after_cancel(self.timer)

        def save_settings():
            try:
                work_time = int(work_entry.get()) * 60
                short_break_time = int(short_break_entry.get()) * 60
                long_break_time = int(long_break_entry.get()) * 60
                cycle = int(cycle_entry.get())

                self.default_work_time = work_time
                self.default_short_break_time = short_break_time
                self.default_long_break_time = long_break_time
                self.cycle = cycle

                customize_window.destroy()
                self.reset_timer()
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")

        customize_window = tk.Toplevel(self.root)
        customize_window.title("Customize Timer")

        tk.Label(customize_window, text="Work time (minutes):").grid(row=0, column=0, padx=10, pady=10)
        work_entry = tk.Entry(customize_window)
        work_entry.insert(0, str(self.default_work_time // 60))
        work_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(customize_window, text="Short break time (minutes):").grid(row=1, column=0, padx=10, pady=10)
        short_break_entry = tk.Entry(customize_window)
        short_break_entry.insert(0, str(self.default_short_break_time // 60))
        short_break_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(customize_window, text="Long break time (minutes):").grid(row=2, column=0, padx=10, pady=10)
        long_break_entry = tk.Entry(customize_window)
        long_break_entry.insert(0, str(self.default_long_break_time // 60))
        long_break_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(customize_window, text="Pomodoros per cycle:").grid(row=3, column=0, padx=10, pady=10)
        cycle_entry = tk.Entry(customize_window)
        cycle_entry.insert(0, str(self.cycle))
        cycle_entry.grid(row=3, column=1, padx=10, pady=10)

        save_button = tk.Button(customize_window, text="Save", command=save_settings)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def start_next_phase(self):
        if self.current_phase == 'work':
            self.current_phase = 'short_break'
            self.countdown(self.default_work_time)
        elif self.current_phase == 'short_break':
            if self.current_cycle == self.cycle - 1:
                self.current_phase = 'long_break'
                self.countdown(self.default_long_break_time)
            else:
                self.current_phase = 'work'
                self.countdown(self.default_short_break_time)
                self.current_cycle += 1
        elif self.current_phase == 'long_break':
            self.current_phase = 'work'
            self.current_cycle = 0
            self.countdown(self.default_long_break_time)

    def countdown(self, count):
        mins, secs = divmod(count, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        self.time_label.config(text=time_format)
        if count > 0:
            self.timer = self.root.after(1000, self.countdown, count - 1)
        else:
            self.is_running = False
            self.root.bell()  # Visual reminder
            if self.current_phase == 'work':
                self.label.config(text="Work time over! Take a short break.")
                self.progress_label.config(text=f"Cycle: {self.current_cycle + 1}/{self.cycle}")
            elif self.current_phase == 'short_break':
                self.label.config(text="Short break over! Back to work.")
            elif self.current_phase == 'long_break':
                self.label.config(text="Long break over! Back to work.")
            self.start_next_phase()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
