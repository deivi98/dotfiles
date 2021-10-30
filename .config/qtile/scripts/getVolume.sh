#!/bin/sh

currentSink=$(pacmd stat | grep "Default sink name" | cut -d" " -f4 2>&1)
mute=$(pactl get-sink-mute $currentSink | cut -d" " -f2 2>&1)
volume=$(pactl get-sink-volume $currentSink | grep Volume | cut -d"/" -f2 | tr -dc '0-9' 2>&1)
# headsetBattery=$(echo david | sudo -S headsetcontrol -b -c 2>&1)
emoji=""

if [ "$currentSink" == "alsa_output.pci-0000_01_00.1.hdmi-stereo" ]; then
    emoji=''
fi

if [ "$mute" == "no" ]; then
    echo -e "$emoji $volume%"
else
    echo -e ' Mute'
fi
