import tkinter as tk
from tkinter import messagebox
import psutil
import threading
import time
import sys
import os
import winsound  # Windows-only sound module

# --- Constants ---
LOW_BATTERY_THRESHOLD = 20
FULL_BATTERY_THRESHOLD = 98
CHECK_INTERVAL = 5  # seconds

# --- Sound File Paths ---
LOW_BATTERY_SOUND = 'ChargeMe.wav'
FULL_BATTERY_SOUND = 'Charge-Remove.wav'

class BatteryMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

        # Flags to avoid repeated alerts
        self.running = True
        self.alert_low_shown = False
        self.alert_full_shown = False

    def show_popup(self, message):
        def popup():
            top = tk.Toplevel()
            top.title("Battery Alert")
            top.geometry("350x150")
            top.configure(bg="black")
            top.attributes("-topmost", True)
            label = tk.Label(top, text=message, font=("Arial", 14), bg="black", fg="white")
            label.pack(pady=20)
            btn = tk.Button(top, text="Close", command=top.destroy)
            btn.pack()
            top.after(5000, top.destroy)  # Auto-close after 5 seconds

        self.root.after(0, popup)

    def play_sound(self, sound_file):
        if os.path.exists(sound_file):
            try:
                winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"[Sound Error] {e}")
        else:
            print(f"[Missing File] Sound file not found: {sound_file}")

    def monitor_battery(self):
        while self.running:
            battery = psutil.sensors_battery()
            if battery is None:
                time.sleep(CHECK_INTERVAL)
                continue

            percent = battery.percent
            plugged = battery.power_plugged

            if percent <= LOW_BATTERY_THRESHOLD and not plugged and not self.alert_low_shown:
                self.show_popup("🔋 Battery low! Please connect the charger.")
                self.play_sound(LOW_BATTERY_SOUND)
                self.alert_low_shown = True
                self.alert_full_shown = False

            elif percent >= FULL_BATTERY_THRESHOLD and plugged and not self.alert_full_shown:
                self.show_popup("⚡ Battery is above 90%. Please remove the charger.")
                self.play_sound(FULL_BATTERY_SOUND)
                self.alert_full_shown = True
                self.alert_low_shown = False

            elif (percent > LOW_BATTERY_THRESHOLD or plugged):
                self.alert_low_shown = False

            elif (percent < FULL_BATTERY_THRESHOLD or not plugged):
                self.alert_full_shown = False

            time.sleep(CHECK_INTERVAL)

    def start(self):
        threading.Thread(target=self.monitor_battery, daemon=True).start()
        self.root.mainloop()

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
