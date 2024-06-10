#!/bin/bash
#  _   _           _       _             
# | | | |_ __   __| | __ _| |_ ___  ___  
# | | | | '_ \ / _` |/ _` | __/ _ \/ __| 
# | |_| | |_) | (_| | (_| | ||  __/\__ \ 
#  \___/| .__/ \__,_|\__,_|\__\___||___/ 
#       |_|                              
#  
# ----------------------------------------------------- 
# Requires paru

# ----------------------------------------------------- 
# Define threshholds for color indicators
# ----------------------------------------------------- 

threshhold_green=0
threshhold_yellow=25
threshhold_red=100

# ----------------------------------------------------- 
# Calculate available updates pacman and aur
# ----------------------------------------------------- 
pacman -Sy

if ! updates_arch=$(pacman -Qu | wc -l ); then
    updates_arch=0
fi

if ! updates_aur=$(paru -Qum | wc -l); then
    updates_aur=0
fi

updates=$(("$updates_arch" + "$updates_aur"))
# ------------- #

css_class="green"

if [ "$updates" -gt $threshhold_yellow ]; then
    css_class="yellow"
fi

if [ "$updates" -gt $threshhold_red ]; then
    css_class="red"
fi

if [ "$updates" -gt $threshhold_green ]; then
    printf '{"text": "%s", "alt": "%s", "tooltip": "Updates repo: %s\rUpdate AUR: %s\rTotal Update: %s", "class": "%s"}' "$updates" "$updates" "$updates_arch" "$updates_aur" "$updates" "$css_class"
else
    printf '{"text": "0", "alt": "0", "tooltip": "0 Updates", "class": "green"}'
fi
