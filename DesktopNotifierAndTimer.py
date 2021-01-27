from plyer import notification
# from timer import timer
import time

title = 'Hello am Stecie Niyonzima'

message = 'My sitMate is tracy'

seconds = int(input("How many seconds to wait? "))

for i in range(seconds):
    print(str(seconds - i) + "seconds remaining")
    notification.notify(title=title, message=message, app_icon=None, timeout=5, toast=False)
    time.sleep(1)

print("TIME IS UP")

