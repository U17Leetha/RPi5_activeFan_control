#!/bin/bash

# Path to the fan control directory
FAN_DIR="/sys/class/thermal/cooling_device0"

# Turn the fan off
turn_fan_off() {
    echo 0 | sudo tee "$FAN_DIR/cur_state"
    echo "Fan turned off"
}

# Turn the fan on
turn_fan_on() {
    echo 4 | sudo tee "$FAN_DIR/cur_state"
    echo "Fan turned on"
}

# Check the current state of the fan
check_fan_state() {
    current_state=$(cat "$FAN_DIR/cur_state")
    echo "Current fan state: $current_state"
}

# Main script

if [ "$1" == "on" ]; then
    turn_fan_on
elif [ "$1" == "off" ]; then
    turn_fan_off
elif [ "$1" == "status" ]; then
    check_fan_state
else
    echo "Usage: $0 [on|off|status]"
    exit 1
fi
