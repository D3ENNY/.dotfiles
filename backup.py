from shutil import copy, copytree, copy2, rmtree
from time import sleep
from os import makedirs, mkdir
from os.path import expanduser, join, isdir, dirname
from tqdm import tqdm
import git, sys, os

##########################
#        VARIABLES       #
##########################
class System: 
    HOME_DIR = expanduser('~')
    CONFIG_DIR = join(HOME_DIR, '.config')
    USR_SHARE_DIR = '/usr/share'
    IMG_DIR = join(HOME_DIR, 'Immagini')
    
class Kde(System):
    CONFIG_FILES = ['albafetch/', 'autostart/', 'btop/', 'dolphinrc', 'fish/', 'flameshot/', 'flameshotrc', 'fontconfig/', 'kdedefaults/', 
                    'konsolerc', 'krunnerrc', 'kscreenlockerrc', 'Kvantum/', 'kwinrc', 'latte', 'neofetch/', 
                    'plasma-org.kde.plasma.desktop-appletsrc', 'plasmarc', 'powermanagementprofilesrc', 'xsettingsd/', 'yakuakerc',] 
    
    HOME_FILES = ['.alias.conf', '.bash_profile', '.bashrc', '.bashrc1', '.logseq/', '.screenlayout/']
    
    USR_SHARE_FILE = ['defaultbg/XeroLinux.png']
    
    IMG_FILE = ['desktop.png', 'bg konsole.png', 'opera.jpg', 'icon/']
    

##########################
#        FUNCTIONS       #
##########################

def copy(src, dst):
    if isdir(src):
        copytree(src, dst)
    else:
        makedirs(dirname(dst), exist_ok=True)
        copy2(src, dst)


def kde():
    kde = Kde()
    
    rmtree('kde/', ignore_errors=True)
    makedirs('kde', exist_ok=True)
    
    print('start saving ~/.config folder')
    with tqdm(total=len(kde.CONFIG_FILES)) as progressBar:
        for i in kde.CONFIG_FILES:  
            copy(join(kde.CONFIG_DIR, i), join('kde/.config', i))
            sleep(0.01)
            progressBar.update(1)
            
    print('start saving home (~/) folder')
    with tqdm(total=len(kde.HOME_FILES)) as progressBar:
        for i in kde.HOME_FILES:
            copy(join(kde.HOME_DIR, i), join("kde/home", i))
            sleep(0.01)
            progressBar.update(1)
    
    print('start saving /usr/share folder')
    with tqdm(total=len(kde.USR_SHARE_FILE)) as progressBar:
        for i in kde.USR_SHARE_FILE:
            copy(join(kde.USR_SHARE_DIR, i), join("kde/" + kde.USR_SHARE_DIR, i))
            sleep(0.01)
            progressBar.update(1)
            
    print('start saving ~/Immagini folder')
    with tqdm(total=len(kde.IMG_FILE)) as progressBar:
        for i in kde.IMG_FILE:
            copy(join(kde.IMG_DIR, i), join("kde/Immagini", i))
            sleep(0.01)
            progressBar.update(1)
    
            
#TODO implementare backup hyprland
def hyprland():
    print('TODO')
    
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
    