import tkinter as tk #To create a GUI
import psutil   #To get the sensor reading of the battery
from tkinter import messagebox #To create a pop up message
import threading #To create a thread
import time #To create a delay
import subprocess #To play the sound in macOS using afplay
import os #To check if the sound file exists in the direcotory or not!

# Sound file name 
chargeME_sound = "ChargeMe.wav"
RemoveCharger = "Charge-Remove.wav"


last_low_battery_alert = 0  #To keep track of the last low battery alert time
last_full_battery_alert = 0  #To keep track of the last full battery alert time
reminder_interval = 20  # 20 seconds interval for reminders if user doesn't take the actions

# Declaring the Global Variables
# ✅ Flags to avoid repeating the same alert again and again
notified_low = False       #Currently setting the notification at low battery to False
notified_full = False      #Currently setting the notification at high battery to False
battery = psutil.sensors_battery

#This functions checks if the sound file exists in the directory or not! and then plays the sound.
def play_alert_sound_removePlug():
    if os.path.exists(RemoveCharger):
        subprocess.call(["afplay", RemoveCharger])
    else:
        print("Sound File doesn't Exist!")

def play_alert_sound_addPlug():
    if os.path.exists(chargeME_sound):
        subprocess.call(["afplay", chargeME_sound])
    else: 
        print("Sound File doesn't exist!")

#This function creates a pop up message with the given message and then closes it after 5 seconds.
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

#This function checks the battery status and sends notifications to the user if the battery is low or full.
def monitor_battery():
    global notified_low, notified_full
    global last_low_battery_alert, last_full_battery_alert

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        current_time = time.time()

        if percent <= 20 and not plugged:
            if current_time - last_low_battery_alert >= reminder_interval:
                threading.Thread(target=play_alert_sound_addPlug).start()
                showPopUp("Battery is below 20%. Please charge")
                last_low_battery_alert = current_time
            notified_full = False
            notified_low = True

        elif percent == 100 and plugged:
            if current_time - last_full_battery_alert >= reminder_interval:
                threading.Thread(target=play_alert_sound_removePlug).start()
                showPopUp("Battery is Full. Remove the Charger Please!")
                last_full_battery_alert = current_time
            notified_full = True
            notified_low = False

        else:
            # Reset times if battery is in a normal state
            last_low_battery_alert = 0
            last_full_battery_alert = 0
            notified_low = False
            notified_full = False

        time.sleep(600)  # Check every 10 minutes for the battery status.

# This function shows a confirmation message when the script starts.
def show_startup_confirmation():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Battery Monitor", "✅ Battery Monitor is now running in the background.")
    root.destroy()

# This function shows a pop up message when the script starts.
if __name__ == "__main__":
    show_startup_confirmation()
    monitor_battery()
    showPopUp()
# This function creates a thread to run the monitor_battery function in the background.
    monitor_thread = threading.Thread(target=monitor_battery)
    monitor_thread.start()