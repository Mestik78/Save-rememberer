##- Settings -##
timerSecs = 10
notificationDurationSecs = 1
lookupServices = ["Photoshop", "Maya", "3dsMax"]

message = '''
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄       ▄    ▄▄▄▄▄▄▄ 
█       █       █   ▄  █ █   █    ▄█ █▄ █       █
█       █▄     ▄█  █ █ █ █   █   █▄   ▄ █  ▄▄▄▄▄█
█     ▄▄█ █   █ █   █▄▄█▄█   █     █▄█  █ █▄▄▄▄▄ 
█    █    █   █ █    ▄▄  █   █▄▄▄       █▄▄▄▄▄  █
█    █▄▄  █   █ █   █  █ █       █       ▄▄▄▄▄█ █
█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄▄▄▄▄█      █▄▄▄▄▄▄▄█
'''
##------------##

import time
import psutil
import subprocess

def isServiceRunning(lookupService):
    runningServices = psutil.process_iter()
    for runningService in runningServices:
        if lookupService.lower() in runningService.name().lower():
            return True
    return False

def isAnyServiceRunning():
    for service in lookupServices:
        if isServiceRunning(service):
            return True
    return False

def removeLineJumpsFromMessage(message):
    return '\\n'.join(message.splitlines())

def getNotificationCommand():
    parsedMessage = removeLineJumpsFromMessage(message)
    commands = [
                "import time",
                "print('%s')"%parsedMessage,
                "time.sleep(%s)"%notificationDurationSecs
                ]
    command = '; '.join(commands)
    return command

def runTerminalWithCommand(command):
    subprocess.call('start /wait python -c "%s"'% command, shell=True)

def notifySaving():
    command = getNotificationCommand()
    runTerminalWithCommand(command)

def wait():
    time.sleep(timerSecs)



def main():
    while (True):
        if isAnyServiceRunning():
            notifySaving()
        wait()
main()
