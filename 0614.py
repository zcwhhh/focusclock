import tkinter as tk
from datetime import datetime

class FocusClock:
    def __init__(self, root):
        self.root = root
        self.root.title("专注时钟")
        self.root.geometry("400x300")

        self.work_time = 90 * 60  # 默认工作时间90分钟
        self.break_time = 30 * 60  # 默认休息时间30分钟
        self.time_left = self.work_time
        self.is_work_time = True
        self.running = False
        self.paused = False

        self.create_widgets()
        self.update_current_time()

    def create_widgets(self):
        self.current_time_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.current_time_label.pack(pady=10)

        self.label = tk.Label(self.root, text=self.format_time(self.work_time), font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.status_label = tk.Label(self.root, text="工作时间", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        self.start_button = tk.Button(frame, text="开始", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(frame, text="暂停", command=self.pause_timer)
        self.pause_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(frame, text="重置", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=10)

        settings_frame = tk.Frame(self.root)
        settings_frame.pack(pady=10)

        tk.Label(settings_frame, text="工作时间(分钟):").grid(row=0, column=0, padx=5)
        self.work_time_entry = tk.Entry(settings_frame, width=5)
        self.work_time_entry.grid(row=0, column=1, padx=5)
        self.work_time_entry.insert(0, "90")

        tk.Label(settings_frame, text="休息时间(分钟):").grid(row=1, column=0, padx=5)
        self.break_time_entry = tk.Entry(settings_frame, width=5)
        self.break_time_entry.grid(row=1, column=1, padx=5)
        self.break_time_entry.insert(0, "30")

        self.apply_button = tk.Button(settings_frame, text="应用", command=self.apply_settings)
        self.apply_button.grid(row=2, column=0, columnspan=2, pady=5)

    def start_timer(self):
        if not self.running and not self.paused:
            self.running = True
            self.paused = False
            self.count_down()

    def pause_timer(self):
        if self.running:
            self.running = False
            self.paused = True

    def reset_timer(self):
        self.running = False
        self.paused = False
        self.is_work_time = True
        self.time_left = self.work_time
        self.update_label()
        self.status_label.config(text="工作时间")
        self.root.configure(bg='white')

    def apply_settings(self):
        try:
            self.work_time = int(self.work_time_entry.get()) * 60
            self.break_time = int(self.break_time_entry.get()) * 60
            self.reset_timer()
        except ValueError:
            pass  # 如果输入无效，忽略

    def count_down(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_label()
            self.root.after(1000, self.count_down)
        elif self.time_left == 0:
            self.switch_mode()

    def switch_mode(self):
        self.is_work_time = not self.is_work_time
        if self.is_work_time:
            self.time_left = self.work_time
            self.status_label.config(text="工作时间")
            self.root.configure(bg='white')
        else:
            self.time_left = self.break_time
            self.status_label.config(text="休息时间")
            self.root.configure(bg='lightgreen')
        self.update_label()
        self.start_timer()

    def update_label(self):
        self.label.config(text=self.format_time(self.time_left))

    def update_current_time(self):
        现在 = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"当前时间: {now}")
        self.root.after(1000, self.update_current_time)

    @staticmethod
    def format_time(seconds):
        mins, secs = divmod(seconds, 60)
        return f'{mins:02d}:{secs:02d}'

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusClock(root)
    root.mainloop()
