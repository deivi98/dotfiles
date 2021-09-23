#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |    https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#
# My bash config

#!/bin/sh

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# Init X session when logging in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
	exec startx
fi

# Enable vim keys
set -o vi

# Enable powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh

export EDITOR=vim
alias dotgit='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias svim="HOME=/home/david && sudo vim -u $HOME/.vimrc"
