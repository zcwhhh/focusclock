import time
import threading

class PomodoroTimer:
    def __init__(self, work_minutes=25, break_minutes=5):
        self.work_time = work_minutes * 60  # 转换为秒
        self.break_time = break_minutes * 60  # 转换为秒
        self.time_left = self.work_time
        self.is_running = False
        self.is_break = False
        self.timer_thread = None

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.start()

    def pause(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.is_break = False
        self.time_left = self.work_time
        self.display_time()

    def run_timer(self):
        while self.is_running and self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.display_time()
        if self.time_left == 0:
            self.is_running = False
            if self.is_break:
                print("休息结束，开始工作！")
                self.time_left = self.work_time
                self.is_break = False
            else:
                print("工作结束，开始休息！")
                self.time_left = self.break_time
                self.is_break = True
            self.display_time()

    def display_time(self):
        mins, secs = divmod(self.time_left, 60)
        print(f'{mins:02d}:{secs:02d}', end="\r")

def main():
    timer = PomodoroTimer(work_minutes=25, break_minutes=5)

    while True:
        command = input("输入 'start' 开始, 'pause' 暂停, 'reset' 重置, 'exit' 退出: ").strip().lower()
        if command == "start":
            timer.start()
        elif command == "pause":
            timer.pause()
        elif command == "reset":
            timer.reset()
        elif command == "exit":
            timer.pause()
            break
        else:
            print("未知命令，请输入 'start', 'pause', 'reset' 或 'exit'")

if __name__ == "__main__":
    main()
