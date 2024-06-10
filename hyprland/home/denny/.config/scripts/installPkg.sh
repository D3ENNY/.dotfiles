#!/bin/sh

#  ___ _   _ ____ _____  _    _     _       ____  _  ______ 
# |_ _| \ | / ___|_   _|/ \  | |   | |     |  _ \| |/ / ___|
#  | ||  \| \___ \ | | / _ \ | |   | |     | |_) | ' / |  _ 
#  | || |\  |___) || |/ ___ \| |___| |___  |  __/| . \ |_| |
# |___|_| \_|____/ |_/_/   \_\_____|_____| |_|   |_|\_\____|
# ----------------------------------------------------- 
# Requires paru
# -----------------------------------------------------

while true; do
    read -p "do you want update only the ufficial repository [1] or AUR also [2]? [1,2]: "  choise
    case $choise in
    1* )
        echo "================="
        echo "update repo"
        echo "================="
        sudo pacman -Syu
        break;;
    2* )
        echo "================="
        echo "update AUR"
        echo "================="
        paru -Syu
        break;;
    * ) 
        echo "please enter a valid parameter";;
    esac
done
