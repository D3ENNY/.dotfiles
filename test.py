from shutil import copy2, copytree
from os import makedirs, system
from os.path import expanduser, join, isdir, dirname
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
 
configs = {
    'KDE': {
        'source_dir': 'kde',
        'target_dir': System.CONFIG_DIR,
        'config_function': lambda: print("Applying KDE configs..."),
    },
    'Hyprland': {
        'source_dir': 'hyprland',
        'target_dir': System.LOCAL_SHARE_DIR,
        'config_function': lambda: print("Applying Hyprland configs..."),
    },
}
 
##########################
#        FUNCTIONS       #
##########################
 
def enhanced_copy(src, dst):
    if isdir(src):
        copytree(src, dst, symlinks=True, ignore=None, copy_function=copy2, ignore_dangling_sinks=False, dirs_exist_ok=True)
    else:
        makedirs(dirname(dst), exist_ok=True)
        copy2(src, dst)
 
def apply_config(config_key):
    config = configs.get(config_key)
    if config:
        config['config_function']()
        dirs = glob(join(config['source_dir'], '*')) + glob(join(config['source_dir'], '.*'))
        print(dirs)
    else:
        print("Configuration not found.")
 
##########################
#         STARTUP        #
##########################
 
choice = input('Do you want to apply KDE config or Hyprland config?\n[1] KDE plasma\n[2] HyprlandWM\nChoose 1 or 2: ').strip()
system('clear')
 
if choice == '1':
    apply_config('KDE')
elif choice == '2':
    apply_config('Hyprland')
else:
    print('Unhandled input')