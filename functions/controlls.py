import os
def increase_brightness(self):
    os.system("light -A 10")
    # op=os.popen("light -A 10").read()
    # print(op)
def decrease_bringtness(self):
    os.system("light -U 10")
def wifi_on(self):
    os.system("nmcli radio wifi on")
    os.system('notify-send "Wifi on"')
def wifi_off(self):
    os.system("nmcli radio wifi off")
    os.system('notify-send "Wifi off"')
def show_wifi_list(self):
    wifi_list = os.popen("nmcli -t -f SSID device wifi list").read()
    self.wifi_list.config(text=wifi_list)
    self.button5.config(text="hide list",command=self.hide_wifi_list)
    # print(list.read())
    # add function to show wifi list here  # TODO: implement this function
def hide_wifi_list(self):
    self.wifi_list.config(text="")
    self.button5.config(text="wifi list" , command=self.show_wifi_list)