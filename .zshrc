#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)  David González (deivi)
# | | | |  / _ \ | | \ \ / / | |  github.com/deivi98
# | |_| | |  __/ | |  \ V /  | |  
# |____/   \___| |_|   \_/   |_|
#

######################################
#             ENV CONFIG             #
######################################

# Exports

## Dotfiles organization
export XDG_CONFIG_HOME="$HOME/.config"                            # Sets default .config directory
export XDG_CACHE_HOME="$HOME/.cache"                              # Sets default .cache directory
export XDG_DATA_HOME="$HOME/.local/share"                         # Sets default .local/share directory
export XDG_STATE_HOME="$HOME/.local/state"                        # Sets default .local/state directory
export GNUPGHOME="$XDG_CONFIG_HOME"
export GTK2_RC_FILES="$HOME/.config/gtk-2.0/gtkrc-2.0"
export npm_config_prefix="$HOME/.local"

## Env variables

### General
export EDITOR=lvim
export VISUAL=lvim
export BROWSER=chromium

### TERMINAL
export TERM="xterm-256color"                                      # Getting proper colors

### LESS
export LESSHISTFILE=/dev/null                                     # Ignore .lesshst

# -----------------------------------------------

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# -----------------------------------------------

# Adding binaries to PATH
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/Applications" ] ;
  then PATH="$HOME/Applications:$PATH"
fi

if [ -d "$HOME/.config/scripts" ] ;
  then PATH=$PATH$( find $HOME/.config/scripts/ -type d -printf ":%p" )
fi

# -----------------------------------------------

# Shell insulter
if [ -f /etc/bash.command-not-found ]; then
	. /etc/bash.command-not-found
fi

# -----------------------------------------------

# Change title of terminals
case ${TERM} in
  xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|alacritty|st|konsole*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
        ;;
  screen*)
    PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
    ;;
esac

######################################
#             ZSH CONFIG             #
######################################

# Vim keys
bindkey -v
KEYTIMEOUT=1

# Zsh completion
zstyle ':completion:*' completer _complete _ignored
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
# zstyle ':completion:*' matcher-list 'm:{[:lower:]}={[:upper:]}'
zstyle :compinstall filename "$HOME/.zshrc"
autoload -Uz compinit
compinit -d ~/.cache/zsh/.zcompdump

## Zsh suggestions and highlighting
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# bindkey '^I' autosuggest-accept

## History search
export HISTORY_SUBSTRING_SEARCH_PREFIXED="true"
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
bindkey -M vicmd 'k' history-substring-search-up
bindkey -M vicmd 'j' history-substring-search-down

## History
HISTFILE=~/.cache/zsh/zsh_history
HISTSIZE=1000
SAVEHIST=1000

# Auto cd & more
setopt autocd beep extendedglob notify

# Cursor style
echo -ne '\e[5 q' # Use beam shape cursor on startup.
precmd() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select

######################################
#          PERSONAL CONFIG           #
######################################

# |==> ALIASES <==| #

## SSH hosts
alias cloud='ssh cloud'
alias deivi='ssh deivii'

## Programs & Utilities
alias vim="$EDITOR"
alias cat='bat'

## Changing "ls" to "exa"
alias ls='exa -al --color=always --group-directories-first'     # My preferred listing
alias la='exa -a --color=always --group-directories-first'      # All files and dirs
alias ll='exa -l --color=always --group-directories-first'      # Long format
alias lt='exa -aT --color=always --group-directories-first'     # Tree listing
alias l.='exa -a | egrep "^\."'

## Pacman and Yay
alias pacsyu='sudo pacman -Syyu --noconfirm'                    # Update only standard pkgs
alias yaysua='yay -Sua --noconfirm'                             # Update only AUR pkgs (yay)
alias yaysyu='yay -Syu --noconfirm'                             # Update standard pkgs and AUR pkgs (yay)
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'                # Remove orphaned packages
alias cu='checkupdates'

alias pacdiff="sudo DIFFPROG=$EDITOR pacdiff"

## Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

## Top
alias top='btop'

## Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

## Adding flags
alias df='df -h'                                                # Human-readable sizes
alias free='free -m'                                            # Show sizes in MB

## Dotfiles git
alias dots='/usr/bin/git --git-dir=$HOME/.config/dotfiles/ --work-tree=$HOME'
alias dotsup='dots add -u && dots commit -m "Dotfiles update" && dots push'

# -----------------------------------------------

# Init X session when logging in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
	exec startx
fi

# -----------------------------------------------

# Neofetch
neofetch

# -----------------------------------------------

# Starship prompt
eval "$(starship init zsh)"
