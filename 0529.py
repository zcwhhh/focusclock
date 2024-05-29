import time
from playsound import playsound

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')
        time.sleep(1)
        total_seconds -= 1
    playsound('alarm.mp3')
    print("时间到！")

def main():
    try:
        focus_minutes = int(input("请输入专注时间（分钟）："))
        break_minutes = int(input("请输入休息时间（分钟）："))
        
        while True:
            print(f"开始专注 {focus_minutes} 分钟...")
            countdown(focus_minutes)
            
            print(f"开始休息 {break_minutes} 分钟...")
            countdown(break_minutes)
            
    except KeyboardInterrupt:
        print("\n番茄钟已停止。")

if __name__ == "__main__":
    main()
