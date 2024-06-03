import time

class PomodoroTimer:
    def __init__(self, work_minutes, short_break_minutes, long_break_minutes, cycles):
        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes
        self.cycles = cycles

    def countdown(self, minutes):
        total_seconds = minutes * 60
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            print(f'\rTime Left: {minutes:02d}:{seconds:02d}', end='')
            time.sleep(1)
            total_seconds -= 1
        print('\rTime is up!            ')

    def start(self):
        for cycle in range(1, self.cycles + 1):
            print(f'Cycle {cycle}/{self.cycles}')
            print('Work Time!')
            self.countdown(self.work_minutes)
            
            if cycle % 4 == 0:
                print('Long Break Time!')
                self.countdown(self.long_break_minutes)
            else:
                print('Short Break Time!')
                self.countdown(self.short_break_minutes)
                
        print('Pomodoro session complete!')

if __name__ == "__main__":
    work_minutes = int(input('Enter work duration (in minutes): '))
    short_break_minutes = int(input('Enter short break duration (in minutes): '))
    long_break_minutes = int(input('Enter long break duration (in minutes): '))
    cycles = int(input('Enter number of cycles: '))

    timer = PomodoroTimer(work_minutes, short_break_minutes, long_break_minutes, cycles)
    timer.start()
