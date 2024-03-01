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
    LOCAL_SHARE_DIR = join(HOME_DIR, '.local', 'share')
    
class Kde(System):
    CONFIG_FILES = ['albafetch/', 'autostart/', 'btop/', 'dolphinrc', 'fish/', 'flameshot/', 'flameshotrc', 'fontconfig/', 'kdedefaults/', 
                    'konsolerc', 'krunnerrc', 'kscreenlockerrc', 'Kvantum/', 'kwinrc', 'latte', 'neofetch/', 
                    'plasma-org.kde.plasma.desktop-appletsrc', 'plasmarc', 'powermanagementprofilesrc', 'xsettingsd/', 'yakuakerc',] 
    
    HOME_FILES = ['.alias.conf', '.bash_profile', '.bashrc', '.bashrc1', '.logseq/', '.screenlayout/']
    
    USR_SHARE_FILE = ['defaultbg/XeroLinux.png']
    
    IMG_FILE = ['desktop.png', 'bg konsole.png', 'opera.jpg', 'icon/']
    
    LOCAL_SHARE_FILE = ['applications/', 'icons/', 'konsole/', 'plasma_icons/', 'uptime-record']

##########################
#        FUNCTIONS       #
##########################

def copy(src, dst):
    if isdir(src):
        copytree(src, dst, symlinks=True, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    else:
        makedirs(dirname(dst), exist_ok=True)
        copy2(src, dst)

def kde():
    
    rmtree('kde/', ignore_errors=True)
    makedirs('kde', exist_ok=True)
    
    print('start saving ~/.config folder')
    with tqdm(total=len(Kde.CONFIG_FILES)) as progressBar:
        for i in Kde.CONFIG_FILES:  
            copy(join(Kde.CONFIG_DIR, i), join('kde/.config', i))
            sleep(0.01)
            progressBar.update(1)
            
    print('start saving home (~/) folder')
    with tqdm(total=len(Kde.HOME_FILES)) as progressBar:
        for i in Kde.HOME_FILES:
            copy(join(Kde.HOME_DIR, i), join("kde/home", i))
            sleep(0.01)
            progressBar.update(1)
    
    print('start saving /usr/share folder')
    with tqdm(total=len(Kde.USR_SHARE_FILE)) as progressBar:
        for i in Kde.USR_SHARE_FILE:
            copy(join(Kde.USR_SHARE_DIR, i), join("kde/" + Kde.USR_SHARE_DIR, i))
            sleep(0.01)
            progressBar.update(1)
            
    print('start saving ~/Immagini folder')
    with tqdm(total=len(Kde.IMG_FILE)) as progressBar:
        for i in Kde.IMG_FILE:
            copy(join(Kde.IMG_DIR, i), join("kde/Immagini", i))
            sleep(0.01)
            progressBar.update(1)
            
    print('start saving ~/.local/share folder')
    with tqdm(total=len(Kde.LOCAL_SHARE_FILE)) as progressBar:
        for i in Kde.LOCAL_SHARE_FILE:
            copy(join(Kde.LOCAL_SHARE_DIR, i), join("kde", '.local', 'share', i))
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
    