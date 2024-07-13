import time

# 定义鼓励语句
encouragements = [
    "做得好！休息一下吧！",
    "继续努力！休息时间到了！",
    "你很棒！快来休息一会儿！",
    "不错的进展！短暂休息一下吧！"
]

# 倒计时函数
def countdown(minutes, message):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print(message)

# 番茄钟函数
def pomodoro_timer(work_duration, short_break_duration, long_break_duration, cycles):
    total_focus_time = 0
    total_break_time = 0

    log = []

    for cycle in range(1, cycles + 1):
        print(f"专注时间第 {cycle} 轮")
        log.append(f"专注时间第 {cycle} 轮")
        countdown(work_duration, "专注时间结束！休息一下吧！")
        total_focus_time += work_duration
        log.append(f"完成专注时间第 {cycle} 轮: {work_duration} 分钟")
        print(encouragements[(cycle - 1) % len(encouragements)])
        
        if cycle % 4 == 0:
            print(f"长休息时间第 {cycle // 4} 次")
            log.append(f"长休息时间第 {cycle // 4} 次")
            countdown(long_break_duration, "长休息结束！准备开始新一轮的专注吧！")
            total_break_time += long_break_duration
            log.append(f"完成长休息时间第 {cycle // 4} 次: {long_break_duration} 分钟")
        elif cycle < cycles:
            print(f"休息时间第 {cycle} 轮")
            log.append(f"休息时间第 {cycle} 轮")
            countdown(short_break_duration, "休息时间结束！继续专注吧！")
            total_break_time += short_break_duration
            log.append(f"完成休息时间第 {cycle} 轮: {short_break_duration} 分钟")

    print("所有轮次完成！")
    log.append("所有轮次完成！")
    print(f"总专注时间: {total_focus_time} 分钟")
    log.append(f"总专注时间: {total_focus_time} 分钟")
    print(f"总休息时间: {total_break_time} 分钟")
    log.append(f"总休息时间: {total_break_time} 分钟")

    with open("pomodoro_log.txt", "w") as file:
        for entry in log:
            file.write(entry + "\n")

# 从用户处获取自定义设置
work_duration = int(input("请输入工作时间（分钟）："))
short_break_duration = int(input("请输入短休息时间（分钟）："))
long_break_duration = int(input("请输入长休息时间（分钟）："))
cycles = int(input("请输入循环次数："))

pomodoro_timer(work_duration, short_break_duration, long_break_duration, cycles)
