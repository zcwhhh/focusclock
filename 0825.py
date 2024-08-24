import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("时间到！休息一下吧。")

if __name__ == "__main__":
    work_time = 25  # 专注时间设置为25分钟
    break_time = 5  # 休息时间设置为5分钟

    while True:
        print("开始工作...")
        countdown(work_time)
        print("休息时间...")
        countdown(break_time)
