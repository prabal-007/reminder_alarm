import time
import winsound
from win10toast import ToastNotifier

def timer(reminder, minutes):
    notificator = ToastNotifier()

    notificator.show_toast('Reminder',
    f"""Alarm will turn off in {minutes} mins.""", duration=50)

    time.sleep(minutes * 60)

    notificator.show_toast(f'Reminder', reminder, duration=50)

    #Alarm
    frequency = 2500  #in Hz
    duration = 1000 # 1 sec
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    words = input('what would you remindes of: ')
    mins = int(input('Enter minutes: '))
    timer(words, mins)
