from shutil import copytree, copy2, rmtree
from time import sleep
from os import makedirs, system
from os.path import join, isdir, dirname
from sys import exit
from tqdm import tqdm
from git import Repo
from glob import glob

import config as configFile

##########################
#        VARIABLES       #
##########################

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
    
def apply_config(key):
    config = configFile.configs.get(key)
    if config:
        config['msg']
        paths = config['path'] 
        
        rmtree(key, ignore_errors=True)
        makedirs(key, exist_ok=True)
        
        for path in paths:
            print(f"start saving {path} folder")
            
            with tqdm(total=len(paths[path])) as progressBar:
                for file in paths[path]:
                    enhanced_copy(f"{path}/{file}", f"{key}/{path[1:]}/{file}", key)
                    sleep(0.01)
                    progressBar.update(1)
            commit(key, f"update {path} folder in {key} dotfile")

def commit(src, msg):
    print("\nstart commit\n")
    with tqdm(total=len(glob(join(src, '.*')) + glob(join(src, '*')))) as progressBar:
        for i in glob(join(src, '.*')) + glob(join(src, '*')):
            repo.index.add(i)
            progressBar.update(1)   
            print(f'{i} folder added to local repository')
            repo.index.commit(msg)
    print("commits mades")
    
    
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