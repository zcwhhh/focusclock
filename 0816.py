import time
import os
import json
from datetime import datetime

SETTINGS_FILE = "pomodoro_settings.json"
LOG_FILE = "pomodoro_log.txt"

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return None

def log_cycle(start_time, end_time, cycle_number):
    with open(LOG_FILE, 'a') as f:
        f.write(f"Cycle {cycle_number}: Start: {start_time}, End: {end_time}\n")

def countdown(minutes, message):
    total_seconds = minutes * 60
    for elapsed_seconds in range(total_seconds):
        mins, secs = divmod(total_seconds - elapsed_seconds, 60)
        progress = int((elapsed_seconds / total_seconds) * 50)
        timer = f"{message}: {mins:02d}:{secs:02d} [{'#' * progress}{'-' * (50 - progress)}]"
        print(timer, end="\r")
        time.sleep(1)
    print(f"\n{message}: 时间到！" + " " * 10)

def pomodoro_cycle(settings):
    cycles = settings["cycles"]
    for i in range(1, cycles + 1):
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n第 {i} 个工作周期开始！")
        countdown(settings["work_minutes"], "工作时间")
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_cycle(start_time, end_time, i)
        
        if i < cycles:
            print("\n短暂休息时间")
            countdown(settings["short_break_minutes"], "休息时间")
        else:
            print("\n长时间休息时间")
            countdown(settings["long_break_minutes"], "休息时间")

if __name__ == "__main__":
    print("欢迎使用番茄钟！")

    settings = load_settings()
    if settings:
        print("加载上次的设置：")
        print(f"  专注时间: {settings['work_minutes']} 分钟")
        print(f"  短休息时间: {settings['short_break_minutes']} 分钟")
        print(f"  长休息时间: {settings['long_break_minutes']} 分钟")
        print(f"  工作周期数: {settings['cycles']}")

        use_previous = input("是否使用上次的设置？(y/n): ").strip().lower() == 'y'
        if not use_previous:
            settings = None

    if not settings:
        try:
            work_minutes = int(input("请输入每次专注的时间（分钟）："))
            short_break_minutes = int(input("请输入短暂休息时间（分钟）："))
            long_break_minutes = int(input("请输入长时间休息时间（分钟）："))
            cycles = int(input("请输入工作周期数："))
            
            settings = {
                "work_minutes": work_minutes,
                "short_break_minutes": short_break_minutes,
                "long_break_minutes": long_break_minutes,
                "cycles": cycles
            }
            save_settings(settings)
        except ValueError:
            print("请输入有效的数字。")
            exit(1)

    pomodoro_cycle(settings)
    print("\n全部周期完成！恭喜你完成了今天的工作！")
