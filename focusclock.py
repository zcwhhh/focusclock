import time
import threading

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("时间到！休息一下吧。")

def start_timer():
    threading.Thread(target=countdown, args=(25,)).start()

if __name__ == "__main__":
    print("专注时钟已启动。25分钟倒计时开始！")
    start_timer()
    input("按Enter键结束程序...\n")
