#!/bin/bash

current_dir=$(pwd)

touch controller.sh
echo "python3 $current_dir/desktop_support.py" >> "$current_dir/controller.sh"
chmod +x "$current_dir/controller.sh"

echo "#open desktop support when ctrl+i is pressed" >> ~/.config/i3/config
echo "bindsym Control+i exec $current_dir/controller.sh" >> ~/.config/i3/config