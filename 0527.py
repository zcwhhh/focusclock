import time
from threading import Timer

class FocusTimer:
    def __init__(self, work_time, short_break, long_break, sessions_before_long_break):
        self.work_time = work_time * 60  # 工作时间（分钟转换为秒）
        self.short_break = short_break * 60  # 短暂休息时间
        self.long_break = long_break * 60  # 长休息时间
        self.sessions_before_long_break = sessions_before_long_break
        self.session_count = 0

    def start(self):
        self.session_count += 1
        print(f"专注时间开始，持续时间：{self.work_time // 60}分钟。")
        self.timer = Timer(self.work_time, self.end_work)
        self.timer。start()

    def end_work(self):
        print("工作时间结束，休息一下！")
        if self.session_count % self.sessions_before_long_break == 0:
            print(f"长休息时间开始，持续时间：{self.long_break // 60}分钟。")
            time.sleep(self.long_break)
        else:
            print(f"短暂休息时间开始，持续时间：{self.short_break // 60}分钟。")
            time.sleep(self.short_break)
        print("休息结束，回到工作吧！")
        self.start()

    def cancel(self):
        self.timer。cancel()
        print("专注时钟已取消。")

# 使用示例
if __name__ == "__main__":
    focus_timer = FocusTimer(work_time=25, short_break=5, long_break=15, sessions_before_long_break=4)
    try:
        focus_timer.start()
    except KeyboardInterrupt:
        focus_timer.cancel()
