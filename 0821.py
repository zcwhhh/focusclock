import time

def focus_timer(minutes):
    try:
        seconds = minutes * 60
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            seconds -= 1
        print("\n时间到！专注时间结束。")
    except KeyboardInterrupt:
        print("\n计时器中断。")

if __name__ == "__main__":
    # 设定默认专注时长为5分钟
    minutes = 5
    print(f"计时开始：{minutes}分钟")
    focus_timer(minutes)
