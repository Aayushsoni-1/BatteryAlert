import tkinter as tk
import psutil
from tkinter import messagebox
import threading
import time
import subprocess
import os

# Sound file name 
chargeME_sound = "ChargeMe.wav"
RemoveCharger = "Charge_Remove.wav"


# ✅ Flags to avoid repeating the same alert again and again
notified_low = False
notified_full = False
battery = psutil.sensors_battery

def play_alert_sound_removePlug():
    if os.path.exists(RemoveCharger):
        subprocess.call(["afplay", RemoveCharger])
    else:
        print("Sound File doesn't Exist!")

def play_alert_sound_addPlug():
    if os.path.exists( chargeME_sound):
        subprocess.call(["afplay", chargeME_sound])
    else: print("Sound File doesn't exist!")

def showPopUp(message):
    popup = tk.Tk() #To create a popup window!
    popup.title("Battery Alert")
    popup.attributes("-fullscreen", True) #To make it Full screen
    popup.attributes("-topmost", True) #To keep it on the top 
    popup.configure(bg="black")

    label = tk.Label(popup, text=message, font=("Helvetica", 48), fg="white", bg="black")
    label.pack(expand=True)

    popup.after(5000, popup.destroy)
    popup.mainloop()

reminder_state = {
    "low_battery": False,
    "full_battery":False,
    "last_reminder_time": 0
}

# To work here for adding the feature that if if user don't follow the instruction then again remind him for following the conditions!😉

def monitor_battery():
    global notified_low, notified_full

    while True:
            battery = psutil.sensors_battery
            percent = battery.percent
            plugged = battery.power_plugged

            if percent == 100 and plugged and not notified_full:
                threading.Thread(target=play_alert_sound_removePlug).start()
                showPopUp("Battery is 100%. Please remove charger!")
                notified_full = True
                notified_low = False
            elif percent == 20 and plugged and not notified_low:
                threading.Thread(target=play_alert_sound_addPlug).start()
                showPopUp("Battery is below 20%. Please Charge!")
                notified_full = False 
                notified_low = True
            elif 20 < percent < 100:
                notified_low = False
                notified_full = False

            time.sleep(60)

def repeated_messaging():
    battery = psutil.sensors_battery



def show_startup_confirmation():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Battery Monitor", "✅ Battery Monitor is now running in the background.")
    root.destroy()

if __name__ == "__main__":
    show_startup_confirmation()

    monitor_thread = threading.Thread(target=monitor_battery)
    monitor_thread.start()