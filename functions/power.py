import os
def poweroff():
    os.system("poweroff")
def restart():
    os.system("reboot")
def hibernate():
    os.system("systemctl hibernate")
# logout
def logout():
    os.system("pkill -u $USER")