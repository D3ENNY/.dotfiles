#!/bin/sh

handle(){
  case $1 in 
    "submap>>resize"*) open;;
    "submap>>"*) close;;
  esac
}

open(){
  hyprctl keyword general:col.active_border 0xb000ffff
  hyprctl notify -1 3000 "rgb(da00ff)" "resize mode enabled"
}

close(){
  hyprctl keyword general:col.active_border 0xffda00ff 0xff9900c6 0xff5900c6 0xff2d0396 45deg
  hyprctl notify -1 3000 "rgb(9900c6)" "resize mode disabled"
}

socat -U - UNIX-CONNECT:/tmp/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock | while read -r line; do handle "$line"; done
