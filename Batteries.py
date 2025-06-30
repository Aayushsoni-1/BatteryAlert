import tkinter as tk   #For Making the GUI popups
from tkinter import messagebox    #For startUp info popup
import psutil       #To get the information about the battery!
import threading    #To run the monitoring in the background and giving the asynchronous nature to these code!
import time         #for delays that are there between the popups
import sys          # For exiting on error or interrupt
import subprocess   # To play sound using afplay
import os           # To check if sound files exist

# --- Constants ---
LOW_BATTERY_THRESHOLD = 20
FULL_BATTERY_THRESHOLD = 90
CHECK_INTERVAL = 5  # seconds

#-- Sound File ---
LOW_BATTERY_SOUND = 'ChargeMe.wav'
FULL_BATTERY_SOUND = 'Charge-Remove.wav'

class BatteryMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

        # Flags and state
        self.running = True
        self.alert_low_shown = False     # Prevents repeated low battery alerts
        self.alert_full_shown = False    # Prevents repeated full battery alerts

    def show_popup(self, message):
        #This is for displaying a popup message window with auto-close after 5 sec
        def popup():
            top = tk.Toplevel()
            top.title("Battery Alert")
            top.geometry("350x150")
            top.configure(bg="black")
            top.attributes("-topmost", True)  #This will keep it going on top!
            label = tk.Label(top, text=message, font=("Arial", 14), bg="black", fg="white")
            label.pack(pady=20)
            btn = tk.Button(top, text="Close", command=top.destroy)
            btn.pack()
            top.after(5000, top.destroy)  # Auto-close popup after 5 seconds

        self.root.after(0, popup)     # Schedule popup in Tkinter’s event loop

    def play_sound(self, sound_file):
        if os.path.exists(sound_file):
            try:
                subprocess.run(['afplay', sound_file])
            except Exception as e:
                print(f"[Sound Error] {e}")
            else:
                print(f"[Missing File] Sound file not found: {sound_file}")

    def monitor_battery(self):
        # The main battery monitoring loop (runs in background thread)
        while self.running:
            battery = psutil.sensors_battery()
            if battery is None:
                time.sleep(CHECK_INTERVAL)
                continue        # Retry after delay if battery info is missing

            percent = battery.percent
            plugged = battery.power_plugged

            if percent <= LOW_BATTERY_THRESHOLD and not plugged:
                self.show_popup("🔋 Battery low! Please connect the charger.")
                self.play_sound(LOW_BATTERY_SOUND)
                self.alert_low_shown = True
                self.alert_full_shown = False

            elif percent >= FULL_BATTERY_THRESHOLD and plugged:
                self.show_popup("⚡ Battery is above 90%. Please remove the charger.")
                self.play_sound(FULL_BATTERY_SOUND)
                self.alert_full_shown = True
                self.alert_low_shown = False

            else:
                # If battery is in a normal state, reset alert flags
                self.alert_low_shown = False
                self.alert_full_shown = False

            time.sleep(CHECK_INTERVAL)

    def start(self):
        # Start the monitoring loop in a background thread
        threading.Thread(target=self.monitor_battery, daemon=True).start()
        self.root.mainloop()
        #  Start the Tkinter event loop for popups

    def stop(self):
        self.running = False
        self.root.quit()

# --- Main Entry ---
if __name__ == "__main__":
    try:
        monitor = BatteryMonitor()
        messagebox.showinfo("Battery Monitor", "✅ Battery monitor is now running in background.")
        monitor.start()
    except KeyboardInterrupt:
        monitor.stop()
        sys.exit()
    except Exception as e:
        print(f"[Fatal Error] {e}")
        sys.exit(1)