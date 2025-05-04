# 🔋 Battery Monitor App

Never overcharge or drain your battery again! Your laptop's new personal guardian is here.

## 💡 What's This?

**Battery Monitor** is a lightweight desktop app built with Python + Tkinter that keeps an eye on your battery and reminds you (with full-screen popups and sounds!) when:
- Your battery is **fully charged** and it's time to unplug 🔌
- Your battery is **too low** and it's time to plug in 🔋

No more forgetting the charger or leaving it on overnight. Your battery health will thank you!

---

## 🧠 Why This?

Laptop batteries degrade faster if you:
- Frequently drain them below 20%
- Leave them plugged in at 100% for hours 😖
- Also just the small notification about the battery status won't be much usefull as these app might be!
This app:
✅ Warns you at 20%  
✅ Alerts you at 100%  
✅ Repeats the reminder every 60 seconds until you take action  
✅ Works quietly in the background without hogging system resources  

---

## 🎧 Features

- 🎵 Plays custom sound alerts (.wav files)
- ⚠️ Full-screen popup reminders you can’t ignore
- 🧵 Non-blocking threads for smooth experience
- 🔁 Keeps checking your battery every minute
- 🧰 Runs at startup

---

## 🛠 How to Use ??

1. Clone this repo or download the `.py` script along with the `.wav file`
2. Place your custom `.wav` alert sounds as:
   - `ChargeMe.wav` → for low battery
   - `Charge_Remove.wav` → for full battery
3. Run the app:
   ```bash
   python3 BatteryMonitor.py  #For macOS user it is necessary to maintain python version you are using!

Any Changes or Recommendations are welcomed🤗

Note:- This app is currently for MACOS only!🥲😅

