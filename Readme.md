# Save reminder
by [Mestik78](github.com/Mestik78)
Automatic save notification.

This program is designed for people that constantly forget to save while working. Sometimes programs can crash and you can loose lots of progress. This script is aiming to fix that.
The script will check if any of the programms you configured is running. If so, it will wait an amount of time set by the user and show a popup remembering you that you have to save.
It is fully configurable from the main file

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
'''
```

## Installation
You can download the main script and run it yourself. Although I would reccomend to start it automatically.
### Dependencies
In order to use this script you need to install psutil.
```python
pip intall psutil
```
### Windows
You can save the file under `shell:startup` (`C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`).
### Linux
You can create a daemon for the script.
