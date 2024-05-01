from shutil import copytree, copy2, rmtree
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
    CONFIG_DIR = f"{HOME_DIR}/.config"
    USR_SHARE_DIR = '/usr/share'
    IMG_DIR = f"{HOME_DIR}/Immagini"
    LOCAL_SHARE_DIR = f"{HOME_DIR}/.local/share"
    
configs = {
    "kde" : {
        "path": {
            System.CONFIG_DIR : [
                'albafetch/',
                'autostart/', 
                'btop/', 
                'dolphinrc',
                'fish/',
                'flameshot/', 
                'flameshotrc',
                'fontconfig/',
                'kdedefaults/',
                'konsolerc',
                'krunnerrc',
                'kscreenlockerrc',
                'Kvantum/', 
                'kwinrc',
                'latte',
                'neofetch/', 
                'plasma-org.kde.plasma.desktop-appletsrc',
                'plasmarc', 'powermanagementprofilesrc',
                'xsettingsd/', 
                'yakuakerc'
            ],
            System.HOME_DIR :[
                '.alias.conf',
                '.bash_profile',
                '.bashrc',
                '.bashrc1',
                '.logseq/',
                '.screenlayout/'
            ],
            System.USR_SHARE_DIR : [
                'defaultbg/'
            ],
            System.IMG_DIR : [
                'desktop.png',
                'bg konsole.png',
                'opera.jpg',
                'icon/'
            ],
            System.LOCAL_SHARE_DIR : [
                'applications/', 
                'dolphin/',
                'konsole/',
                'plasma_icons/',
                'uptime-record'
            ]
        },
        "msg" : lambda : print("saving KDE Plasma's config")
    },
    "hyprland" : {
        "path" :  {
            System.CONFIG_DIR : [
                "albafetch/",
                "btop/", 
                "Code/",
                "discord-screenaudio/",
                "fish/",
                "gtk-2.0/",
                "gtk-3.0/",
                "hypr/",
                "hyprland-autoname-workspaces/",
                "kitty/",
                "Logseq/",
                "neofetch/",
                "nvim/",
                "pipes-rs/",
                "rofi/",
                "scripts/",
                "thunar/",
                "waybar/",
                "user-dirs.dirs",
                "user-dirs.locale"
            ],
            System.HOME_DIR : [
                ".logseq/",
                ".alias.conf",
                ".bash_profile",
                ".bashrc"
            ],
            System.LOCAL_SHARE_DIR : [
                "sddm/"
            ],
            System.IMG_DIR : [
                "wallpaper"
            ]
        },
        "msg" : lambda : print("saving Hyprland's config")
    }
}

repo = Repo('./')
origin = repo.remote('origin')
##########################
#        FUNCTIONS       #
##########################

def enhanced_copy(src, dst, key):
    try:
        if isdir(src):
            copytree(src, dst, symlinks=True, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
        else:
            makedirs(dirname(dst), exist_ok=True)
            copy2(src, dst)
    except (FileNotFoundError, FileExistsError) as err:
        with open(f"{key}/log.txt", 'a+') as log:
            log.write(f'src: {src} - dst: {dst}\n{err}\n\n')
            
def commit(src, msg):
    for i in glob(join(src, '.*')) + glob(join(src, '*')):
        repo.index.add(i)
        print(f'{i} folder added to local repository')
        repo.index.commit(msg)
    print("commits mades")
    
def apply_config(key):
    config = configs.get(key)
    if config:
        config['msg']
        paths = config['path'] 
        
        rmtree(key, ignore_errors=True)
        makedirs(key, exist_ok=True)
        
        for path in paths:
            print(f"start saving {path} folder")
            
            with tqdm(total=len(paths[path])) as progressBar:
                for file in paths[path]:
                    enhanced_copy(f"{path}/{file}", f"{key}/{path[1:]}", key)
                    sleep(0.01)
                    progressBar.update(1)
        commit(key, f"update {key} .dotfile")
    
    
##########################
#         STARTUP        #
##########################
#TODO: DA AUTOMATIZZARE
choise = int(input('do you want to update KDE config or hyprland config?\n[1] KDE plasma\n[2] HyprlandWM\n'))
system('clear')
if choise == 1:
    apply_config("kde")
elif choise == 2:
    apply_config("hyprland")
else:
    print('unhandled input')
    exit(1)

origin.push()
print("local repository pushed on github")