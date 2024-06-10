if status is-interactive
	
	# ALIAS
	
	if test -e ~/.alias.conf
		source ~/.alias.conf
	end
	
	#APPLICATION
	thefuck --alias | source
	albafetch
  uptime-record -s 
  set fish_greeting

  #THEME
  # fish_config theme save "TokyoNight Moon"

  #FUNCTIONS
  function vim
    
    if test -e $argv[1]
      if test -f $argv[1]
        cd (dirname $argv[1])
        nvim (basename $argv[1])
      else if test -d $argv[1]
        cd $argv[1]
        nvim $argv[1]
      end
    else 
      nvim $arv[1]
    end
    prevd

  end

  function __fish_math
    echo (math "$argv")
  end 

  function __fish_math
    if test (count $argv) -gt 0
      echo (math "$argv")
    else
      __fish_git_prompt
    end
  end

end

function unzip
  7z x $argv[1]
end
