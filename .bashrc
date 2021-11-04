#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |  https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#

### EXPORTS
export XDG_CONFIG_HOME="$HOME/.config"        # Sets default .config directory
export XDG_CACHE_HOME="$HOME/.cache"          # Sets default .cache directory
export XDG_DATA_HOME="$HOME/.local/share"     # Sets default .local/share directory
export XDG_STATE_HOME="$HOME/.local/state"    # Sets default .local/state directory
export GNUPGHOME="$XDG_CONFIG_HOME"
export TERM="xterm-256color"                  # Getting proper colors
export HISTCONTROL=ignoredups                 # Ignore duplicates in .bash_history
export LESSHISTFILE=/dev/null                 # Ignore .lesshst
export EDITOR="nvim"
export VISUAL="nvim"
export BROWSER="firefox"

### VIM KEYS
set -o vi

### Clear screen
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'

### If not running interactively, don't do anything
[[ $- != *i* ]] && return

### PATH
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/Applications" ] ;
  then PATH="$HOME/Applications:$PATH"
fi

### BASH INSULTER

if [ -f /etc/bash.command-not-found ]; then
	. /etc/bash.command-not-found
fi

### CHANGE TITLE OF TERMINALS
case ${TERM} in
  xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|alacritty|st|konsole*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
        ;;
  screen*)
    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
    ;;
esac

### SHOPT
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize # checks term size when bash regains control

### BASH COMPLETION

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

source /usr/share/fzf/key-bindings.bash
source /usr/share/fzf/completion.bash 

# If there are multiple matches for completion, Tab should cycle through them
bind 'TAB':menu-complete

# Display a list of the matching files
bind "set show-all-if-ambiguous on"

# Perform partial completion on the first Tab press,
# only start cycling full results on the second Tab press
bind "set menu-complete-display-prefix on"

# Colour autocomplete suggestions
bind "set colored-stats on"

### ALIASES

# SSH hosts
alias cloud='ssh cloud'
alias deivi='ssh deivii'

# Programs
alias vim='nvim'
alias cat='bat'

# Changing "ls" to "exa"
alias ls='exa -al --color=always --group-directories-first' # my preferred listing
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | egrep "^\."'

# Pacman and Yay
alias pacsyu='sudo pacman -Syyu'                 # update only standard pkgs
alias yaysua='yay -Sua --noconfirm'              # update only AUR pkgs (yay)
alias yaysyu='yay -Syu --noconfirm'              # update standard pkgs and AUR pkgs (yay)
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'  # remove orphaned packages
alias cu='checkupdates'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Top
alias top='bashtop'

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

# VIM
alias svim="HOME=/home/david && sudo vim -u $HOME/.vimrc"

# Dotfiles git
alias dotgit='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

### X SESSION

# Init X session when logging in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
	exec startx
fi

neofetch

### STARSHIP PROMPT
eval "$(starship init bash)"
