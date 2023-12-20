# Save Reminder
by [Mestik78](github.com/Mestik78)
Automatic save reminders.

This program is designed for people who constantly forget to save while working. Sometimes programs can crash, and you can lose lots of progress. This script aims to fix that.
The script will check if any of the programs you configured are running. If so, it will wait for an amount of time set by the user and show a popup reminding you that you have to save.
It is fully configurable from the main file.

## Configuration
You can change the settings from the main script on the first few lines.
### Example Configuration
```python
# Set the time (in seconds) between each notification
timerSecs = 10

# Set the duration (in seconds) that notifications will be shown
notificationDurationSecs = 1

# Specify the programs to monitor (not case-sensitive)
lookupServices = ["Photoshop", "Maya", "3dMax"]

# Customize the notification message
message = '''
▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄       ▄    ▄▄▄▄▄▄▄ 
█       █       █   ▄  █ █   █    ▄█ █▄ █       █
█       █▄     ▄█  █ █ █ █   █   █▄   ▄ █  ▄▄▄▄▄█
█     ▄▄█ █   █ █   █▄▄█▄█   █     █▄█  █ █▄▄▄▄▄ 
█    █    █   █ █    ▄▄  █   █▄▄▄       █▄▄▄▄▄  █
█    █▄▄  █   █ █   █  █ █       █       ▄▄▄▄▄█ █
█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄▄▄▄▄█      █▄▄▄▄▄▄▄█ 🫶
```

## Installation
You can download the main script and run it yourself, although I would recommend starting it automatically.
### Dependencies
To use this script, you need to install psutil.
```python
pip install psutil
```
### Windows
You can save the file under `shell:startup` (`C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`).
### Linux
You can create a daemon for the script.
```

These changes should make your README even more clear and polished.
