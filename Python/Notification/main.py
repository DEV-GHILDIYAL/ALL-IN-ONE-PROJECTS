from plyer import notification
import time
import psutil

def check_battery_Status(battery, plugged=False):
    if plugged:
        if(battery >= 80):
            notification.notify(
                title = f"BATTERY REMINDER",
                message="PLEASE CHARGE OFF" ,
                timeout = 2
            )
        elif (battery <= 20):
            notification.notify(
                title = f"BATTERY REMINDER",
                message="PLEASE CHARGE ON" ,
                timeout = 2
            )

    else:
        if(battery >= 80):
            notification.notify(
                title = f"BATTERY REMINDER",
                message="PLEASE CHARGE OFF" ,
                timeout = 2
            )
        elif (battery <= 20):
            notification.notify(
                title = f"BATTERY REMINDER",
                message="PLEASE CHARGE ON" ,
                timeout = 2
            )


battery = psutil.sensors_battery()
plugged = battery.power_plugged  
battery = battery.percent
print(battery)
check_battery_Status(battery, True)