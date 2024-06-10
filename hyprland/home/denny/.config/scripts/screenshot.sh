#  ____   ____ ____  _____ _____ _   _ ____  _   _  ___ _____ 
# / ___| / ___|  _ \| ____| ____| \ | / ___|| | | |/ _ \_   _|
# \___ \| |   | |_) |  _| |  _| |  \| \___ \| |_| | | | || |  
#  ___) | |___|  _ <| |___| |___| |\  |___) |  _  | |_| || |  
# |____/ \____|_| \_\_____|_____|_| \_|____/|_| |_|\___/ |_|  
                                                            
screenshotCopy(){
  # hyprpicker -r -z
  grim -g "$(slurp -d)"  - | wl-copy 
  hyprctl notify -1 3000 "rgb(9900c6)" "Screenshot copied"
}

fullscreenshotCopy(){
  grim - | wl-copy
  hyprctl notify -1 3000 "rgb(9900c6)" "Screenshot copied"
}

screenshotSave(){
   # hyprpicker -r -z
   grim -g "$(slurp -d)" - ~/Immagini/Screenshot/screen-$(date +"%Y%m%d_%H%M%S").png
   wl-copy < ~/Immagini/Screenshot/$(ls -1 -t ~/Immagini/Screenshot | head -1)
   hyprctl notify -1 3000 "rgb(9900c6)" "Screenshot saved"
}

fullscreenshotSave(){
   grim ~/Immagini/Screenshot/screen-$(date +"%Y%m%d_%H%M%S").png
   wl-copy < ~/Immagini/Screenshot/$(ls -1 -t ~/Immagini/Screenshot | head -1)
   hyprctl notify -1 3000 "rgb(9900c6)" "Screenshot saved"
}

if [ $# -gt 0 ]; then
  case $1 in 
    "screenshotCopy"*) screenshotCopy;;
    "fullScreenshotCopy"*) fullscreenshotCopy;;
    "screenshotSave"*) screenshotSave;;
    "fullScreenshotSave"*) fullscreenshotSave;;
  esac
fi 
