import time

class PomodoroTimer:
    def __init__(self, work_minutes, short_break_minutes, long_break_minutes, cycles):
        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes
        self.cycles = cycles
        self.logs = []
        self.paused = False
        self.remaining_time = 0
        self.current_phase = None
        self.current_cycle = 0

    def log(self, cycle, phase, start_time, end_time):
        self.logs.append({
            "cycle": cycle,
            "phase": phase,
            "start_time": start_time,
            "end_time": end_time,
        })

    def countdown(self, minutes, label):
        self.current_phase = label
        self.remaining_time = minutes * 60
        start_time = time.time()
        while self.remaining_time > 0:
            if not self.paused:
                mins, secs = divmod(self.remaining_time, 60)
                timer = f"{label} - {mins:02d}:{secs:02d}"
                print(timer, end="\r")
                time.sleep(1)
                self.remaining_time -= 1
            else:
                print(f"{label} - 暂停中...     ", end="\r")
                time.sleep(1)
        end_time = time.time()
        self.log(self.current_cycle, label, start_time, end_time)
        print(f"\n{label} 时间到！")

    def start_timer(self):
        for i in range(1, self.cycles + 1):
            self.current_cycle = i
            print(f"第 {i} 个工作周期开始!")
            self.countdown(self.work_minutes, "工作")
            
            if i % 4 == 0:
                print("长休息时间!")
                self.countdown(self.long_break_minutes, "长休息")
            else:
                print("短休息时间!")
                self.countdown(self.short_break_minutes, "短休息")
        
        print("所有工作周期结束！")
        self.show_logs()

    def pause_timer(self):
        self.paused = True

    def resume_timer(self):
        self.paused = False

    def show_logs(self):
        print("\n日志记录:")
        for log in self.logs:
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log['start_time']))
            end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log['end_time']))
            print(f"周期 {log['cycle']}, {log['phase']}, 开始: {start_time}, 结束: {end_time}")

def input_with_validation(prompt, valid_type=int, min_value=None, max_value=None):
    while True:
        try:
            value = valid_type(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"请输入一个介于 {min_value} 和 {max_value} 之间的值。")
            else:
                return value
        except ValueError:
            print(f"请输入一个有效的 {valid_type.__name__} 类型的值。")

if __name__ == "__main__":
    print("欢迎使用番茄工作法计时器!")
    
    work_minutes = input_with_validation("请输入每个工作周期的时长（分钟）：", min_value=1)
    short_break_minutes = input_with_validation("请输入每个短休息周期的时长（分钟）：", min_value=1)
    long_break_minutes = input_with_validation("请输入每个长休息周期的时长（分钟）：", min_value=1)
    cycles = input_with_validation("请输入工作周期的次数：", min_value=1)
    
    pomodoro_timer = PomodoroTimer(work_minutes, short_break_minutes, long_break_minutes, cycles)
    
    while True:
        command = input("请输入命令（start: 开始, pause: 暂停, resume: 继续, logs: 查看日志, exit: 退出）：").strip().lower()
        if command == "start":
            pomodoro_timer.start_timer()
        elif command == "pause":
            pomodoro_timer.pause_timer()
        elif command == "resume":
            pomodoro_timer.resume_timer()
        elif command == "logs":
            pomodoro_timer.show_logs()
        elif command == "exit":
            break
        else:
            print("无效命令，请重新输入。")
