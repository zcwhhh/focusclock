import time
import datetime

class FocusTimer:
    def __init__(self, focus_time, break_time, rounds, log_file="focus_log.txt"):
        self.focus_time = focus_time * 60  # 将分钟转换为秒
        self.break_time = break_time * 60  # 将分钟转换为秒
        self.rounds = rounds
        self.log_file = log_file
        self.current_round = 0

    def start_timer(self):
        for _ in range(self.rounds):
            self.current_round += 1
            self.log_phase(f"第 {self.current_round} 轮专注时间开始")
            self.countdown("专注时间", self.focus_time)
            self.log_phase(f"第 {self.current_round} 轮专注时间结束")
            self.notify("专注时间结束！休息一下吧。")

            self.log_phase(f"第 {self.current_round} 轮休息时间开始")
            self.countdown("休息时间", self.break_time)
            self.log_phase(f"第 {self.current_round} 轮休息时间结束")
            self.notify("休息时间结束！准备开始下一轮专注吧。")

    def countdown(self, phase, seconds):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(seconds=seconds)
        
        print(f"开始 {phase}，倒计时 {seconds // 60} 分钟。")
        
        while datetime.datetime.now() < end_time:
            time_left = end_time - datetime.datetime.now()
            minutes, seconds = divmod(time_left.seconds, 60)
            timer_format = f"{minutes:02d}:{seconds:02d}"
            print(timer_format, end="\r")
            time.sleep(1)
        
        print(f"{phase} 结束！")

    def notify(self, message):
        print(f"\n\033[1;32m{message}\033[0m\n")  # 绿色文本表示通知

    def log_phase(self, phase):
        with open(self.log_file, "a") as f:
            log_message = f"{phase}: {datetime.datetime.now()}\n"
            f.write(log_message)

if __name__ == "__main__":
    focus_time = int(input("请输入专注时间（分钟）："))
    break_time = int(input("请输入休息时间（分钟）："))
    rounds = int(input("请输入轮次："))
    timer = FocusTimer(focus_time, break_time, rounds)
    timer.start_timer()
