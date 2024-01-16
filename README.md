# RPi5_activeFan_control
Simple script to turn the active fan control on and off upon installation to verify it is working 


## Check fan configuration - adjust if needed
    cat /sys/class/thermal/cooling_device0/type
    cat /sys/class/thermal/cooling_device0/max_state

## make scirpt executable 
    chmod +x fan_control.sh

## Turn the fan on
    ./fan_control.sh on

## Turn the fan off
    ./fan_control.sh off

## Check current fan status 
    ./fan)control.sh status
