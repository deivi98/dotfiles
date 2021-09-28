#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |    	https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#

### EXPORTS

# Getting proper colors
export TERM="xterm-256color"                      
export HISTCONTROL=ignoredups
export EDITOR=vim

### VIM KEYS
set -o vi

### If not running interactively, don't do anything
[[ $- != *i* ]] && return

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

### ALIASES

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

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

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

### PROMPT
PS1='[\u@\h \W]\$ '

# Enable powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh

### X SESSION

# Init X session when logging in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
	exec startx
fi
