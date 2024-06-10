#!/usr/bin/env bash

## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
#
## Rofi   : Power Menu
#
## Available Styles
#
## style-1   style-2   style-3   style-4   style-5

# Current Theme


get_uptime() {
  uptime=$1
  formatted_uptime=''

  days=$(($uptime / 86400))
  hours=$(($uptime / 3600 - days * 24))
  mins=$(($uptime / 60 - days * 1440 - hours * 60))
  sec=$(($uptime - days*86400 - hours * 3600 - mins * 60))
  
  if [[ $days -gt 0 ]]; then
    formatted_uptime="${days}days"
  fi 

  if [[ $hours -gt 0 ]]; then
    formatted_uptime="${formatted_uptime} ${hours} hours"
  fi

  if [[ $mins -gt 0 ]]; then 
    formatted_uptime="${formatted_uptime} ${mins} minutes"
  fi

  echo "$formatted_uptime"
}

dir="$HOME/.config/rofi/powermenu/type-4"
theme='style-2'

# CMDs
uptime="`uptime -p | sed -e 's/up //g'`"
uptime-record
seconds="`cat ~/.local/share/uptime-record`"
uptime_record=$(get_uptime $seconds)
host=`hostname`

# Options
shutdown=''
reboot=''
lock=''
suspend=''
logout=''
yes=''
no=''

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "Goodbye ${USER}" \
		-mesg "Higest Uptime:$uptime_record" \
		-theme ${dir}/${theme}.rasi
}

# Confirmation CMD
confirm_cmd() {
	rofi -dmenu \
		-p 'Confirmation' \
		-mesg 'Are you Sure?' \
		-theme ${dir}/shared/confirm.rasi
}

# Ask for confirmation
confirm_exit() {
	echo -e "$yes\n$no" | confirm_cmd
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd
}

# Execute Command
run_cmd() {
	selected="$(confirm_exit)"
	if [[ "$selected" == "$yes" ]]; then
		if [[ $1 == '--shutdown' ]]; then
			systemctl poweroff
		elif [[ $1 == '--reboot' ]]; then
			systemctl reboot
		elif [[ $1 == '--suspend' ]]; then
			mpc -q pause
			amixer set Master mute
			systemctl suspend
		elif [[ $1 == '--logout' ]]; then
			hyprctl dispatch exit
		fi
	else
		exit 0
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $lock)
		if [[ -x '/usr/bin/betterlockscreen' ]]; then
			betterlockscreen -l
		fi
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $logout)
		run_cmd --logout
        ;;
esac
