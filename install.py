from shutil import copy2, copytree
from os import makedirs, system
from os.path import expanduser, join, isdir, dirname

##########################
#        VARIABLES       #
##########################

class System: 
    HOME_DIR = expanduser('~')
    CONFIG_DIR = join(HOME_DIR, '.config')
    USR_SHARE_DIR = '/usr/share'
    IMG_DIR = join(HOME_DIR, 'Immagini')
    LOCAL_SHARE_DIR = join(HOME_DIR, '.local', 'share')

configs = {
    "kde" : {
        "path": [
            { "from": "kde/home", "to" : System.HOME_DIR},
            { "from": "kde/.config", "to" : System.CONFIG_DIR},
            { "from": "kde/.local/share", "to" : System.LOCAL_SHARE_DIR},
            { "from": "kde/Immagini", "to" : System.IMG_DIR},
            { "from": "kde/usr/share", "to" : System.USR_SHARE_DIR}
        ],
        "msg" : lambda : print("applying KDE Plasma config")
    },
    "hyprland" : {
        
    }
}


##########################
#        FUNCTIONS       #
##########################

def enhanced_copy(src, dst):
    if isdir(src):
        copytree(src, dst, symlinks=True, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    else:
        makedirs(dirname(dst), exist_ok=True)
        copy2(src, dst)

def apply_config(key):
    config = configs.get(key)
    if config:
        config['msg']
        
    else:
        print("one error was occured while keying ")
    
##########################
#         STARTUP        #
##########################
    
choise = int(input('do you want to apply KDE config or hyprland config?\n[1] KDE plasma\n[2] HyprlandWM\n'))
system('clear')
if choise == 1:
    apply_config("kde")
elif choise == 2:
    apply_config("hyprlad")
else:
    print('unhandled input')
    exit(1)