from shutil import copy, copytree, copy2, rmtree
from time import sleep
from os import makedirs, mkdir, system
from os.path import expanduser, join, isdir, dirname
from sys import exit
from tqdm import tqdm
from git import Repo
from glob import glob

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
    
    LOCAL_SHARE_FILE = ['applications/', 'konsole/', 'plasma_icons/', 'uptime-record']

repo = Repo('./')
origin = repo.remote('origin')
##########################
#        FUNCTIONS       #
##########################

def copy(src, dst):
    if isdir(src):
        copytree(src, dst, symlinks=True, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    else:
        makedirs(dirname(dst), exist_ok=True)
        copy2(src, dst)
        
def backupCategory(src, dst, files):
    with tqdm(total=len(files)) as progressBar:
        for i in files:
            copy(join(src, i), join(dst, i))
            sleep(0.01)
            progressBar.update(1)
            
def commit(src, msg):
    for i in glob(join(src, '.*')) + glob(join(src, '*')):
        repo.index.add(i)
        print(f'{i} folder added to local repository')
        repo.index.commit(msg)
    print("commits effettuated")
    

def kde():
    
    rmtree('kde/', ignore_errors=True)
    makedirs('kde', exist_ok=True)
    
    print('start saving ~/.config folder')
    backupCategory(Kde.CONFIG_DIR, join('kde', '.config'), Kde.CONFIG_FILES)
            
    print('start saving home (~/) folder')
    backupCategory(Kde.HOME_DIR, join('kde', 'home'), Kde.HOME_FILES)
    
    print('start saving /usr/share folder')
    backupCategory(Kde.USR_SHARE_DIR, f'kde/{Kde.USR_SHARE_DIR}', Kde.USR_SHARE_FILE)
            
    print('start saving ~/Immagini folder')
    backupCategory(Kde.IMG_DIR, join('kde', 'Immagini'), Kde.IMG_FILE)
            
    print('start saving ~/.local/share folder')
    backupCategory(Kde.LOCAL_SHARE_DIR, join('kde', '.local', 'share'), Kde.LOCAL_SHARE_FILE)
    
    print('\n\n.dotfile saved')
    
            
#TODO implementare backup hyprland
def hyprland():
    print('TODO')
    
##########################
#         STARTUP        #
##########################
    
choise = int(input('do you want to update KDE config or hyprland config?\n[1] KDE plasma\n[2] HyprlandWM\n'))
system('clear')
if choise == 1:
    kde()
    commit("kde/", 'update KDE .dotfile')
elif choise == 2:
    hyprland()
else:
    print('unhandled input')
    exit(1)

# origin.push()
# print("local repository pushed on github")