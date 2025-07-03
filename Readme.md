# 🔋 Battery Monitor App

> Never overcharge or drain your battery again! Your laptop's personal battery guardian.

---

## 💡 What is This?

**Battery Monitor** is a lightweight desktop application built with **Python** and **Tkinter** that watches your battery percentage and alerts you when it’s:

- 🔌 **Fully charged** (time to unplug)
- 🔋 **Too low** (time to plug in)

This helps protect your battery health and saves you from accidental overcharging or deep discharging.

---

## 🧠 Why Use This App?

Laptop batteries lose capacity faster when:

- You **let them drain below 20%**
- You **keep them at 100% while charging**
- You **miss the OS notifications** (which are easy to ignore)

### ✅ This app gives you:
- Low battery alerts at **20%**
- Full battery alerts at **98%**
- 🔔 Persistent popup + 🎵 sound alerts every few seconds
- 💻 Lightweight, background-friendly design

---

## 🎧 Features

- 🪟 **Popup notifications** using `tkinter`
- 🎵 **Sound alerts** using:
  - `winsound` on **Windows**
  - `afplay` on **macOS**
- ⚡ **Smart status tracking** — alerts only when status changes
- 🧵 **Multithreaded** for a responsive UI
- ⏲️ **Customizable** thresholds and check intervals

---

## 📦 Requirements

- Python 3.x
- `psutil` library (for battery status)
- `.wav` sound files for alerts

Install `psutil` using:

```bash
pip install psutil
````

---

🚀 Getting Started
1) Clone the Repo
   
```bash
   git clone https://github.com/your-username/battery-monitor.git
   cd battery-monitor
````

For MacOS users: 

```bash
   python3 Batteries.py
````


For Windows Users:

```bash
   python3 BatteriesWin.py
````

---

##Acknowledgements
Built with love to help laptop users:
Improve battery life
Avoid battery degradation
Stay stress-free while working
Because good batteries make happy laptops! 🧠🔋

📄 License
MIT License — Use freely, modify easily, and share widely.

🙋‍♂️ Contribute
Found a bug? Want a new feature?
Feel free to open an issue or submit a pull request. Contributions are always welcome!




