import webbrowser
import time
import os

total_breaks = 3
break_count = 0
duration = 1  # seconds
freq = 440  # Hz

print("This program started on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=eFSlDeA9fWE")
    print("Reminder to Take a Break" + time.ctime())
    break_count = break_count + 1
    os.system('say "Phillip Take a Break Please!"')
