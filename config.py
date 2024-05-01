from os.path import expanduser


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