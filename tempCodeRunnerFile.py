lf):
        # Execute the command and get the VPN list
        vpn_list = os.popen("nmcli -t -f NAME,TYPE connection show | grep vpn | cut -d: -f1").read()
        vpn_list = vpn_list.strip().split('\n')

        # Print the list (for debugging purposes)
        print(vpn_list)

        # Loop through each VPN and create a button
        for vpn_name in vpn_list:
            b = Sbutton(self.vpn_list, text=vpn_name)
            
            # Use partial to pass the correct vpn_name to the command
            b.config(command=partial(self.select_vpn, vpn_name=vpn_name))
            b.pack()

        # Optional: Update the button to hide the list (if needed)
        # self.button6.config(text="hide list", command=self.hide_vpn_list)

    def select_vpn(self, vpn_name):
        print(vpn_name) 