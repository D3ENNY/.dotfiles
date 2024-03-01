from shutil import copytree, copy2, rmtree
from time import sleep
from os import makedirs, mkdir
from os.path import expanduser, join, isdir
from tqdm import tqdm
import git, sys, os

##########################
#        VARIABLES       #
##########################
class System: 
    HOME_DIR = expanduser('~')
    CONFIG_DIR = join(HOME_DIR, '.config')
    
class Kde(System):
    CONFIG_FILES = ['albafetch/', 'autostart/', 'btop/', 'dolphinrc', 'fish/', 'flameshot/', 'flameshotrc', 'fontconfig/', 'kdedefaults/', 
                    'konsolerc', 'krunnerrc', 'kscreenlockerrc', 'Kvantum/', 'kwinrc', 'latte', 'neofetch/', 
                    'plasma-org.kde.plasma.desktop-appletsrc', 'plasmarc', 'powermanagementprofilesrc', 'xsettingsd/', 'yakuakerc',] # kscreenlockerrc plasma-org.kde.plasma.desktop-appletsrc plasmarc

##########################
#        FUNCTIONS       #
##########################

def copy(src, dst):
    if isdir(src):
        copytree(src, dst)
    else:
        copy2(src, dst)

def kde():
    kde = Kde()
    
    rmtree("kde/", ignore_errors=True)
    makedirs("kde", exist_ok=True)
    
    print("start saving ~/.config folder")
    with tqdm(total=len(kde.CONFIG_FILES)) as progressBar:
        for config_file in kde.CONFIG_FILES:  
            copy(join(kde.CONFIG_DIR, config_file), join("kde/.config", config_file)  )
            sleep(0.01)
            progressBar.update(1)
            
    
def hyprland():
    print("test")
    
##########################
#         STARTUP        #
##########################
    
choise = int(input('do you want to update KDE config or hyprland config?\n[1] KDE plasma\n[2] HyprlandWM\n'))
os.system('clear')
if choise == 1:
    kde()
elif choise == 2:
    hyprland()
else:
    print('unhandled input')
    sys.exit(1)
    