if status is-interactive

    # ALIAS

    if test -e ~/.alias.conf
        source ~/.alias.conf
    end
    thefuck --alias | source


    neofetch

    #FUNCTION

    function uninstallQuery
	sudo pacman -Rssn $(pacman -Q | grep "$argv[1]" | grep -oP '^\S+')
    end

end


