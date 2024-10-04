if op.strip()=="true":
            os.system('notify-send "muted"')
        else:
            os.system('notify-send "unmuted"')