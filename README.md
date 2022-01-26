# Deivi's ~/.dotfiles

Hi there, these are my own dotfiles :)

## Table of contents

* [Cheatsheet](#cheatsheet)
* [Installed Packages](#installed-packages)
  * [Kernels](#kernels)
  * [Graphics](#graphics)
  * [Shell](#shell)
  * [WM](#wm)
  * [Network](#network)
  * [Bluetooth](#bluetooth)
  * [Peripherals](#peripherals)
  * [Hardware](#hardware)
  * [Video](#video)
  * [PDF](#pdf)
  * [Sound](#sound)
  * [Music](#music)
  * [Browser](#browser)
  * [Editor](#editor)
  * [Appearance](#appearance)
  * [File Explorer](#file-explorer)
  * [Terminal emulator](#terminal-emulator)
  * [Essential](#essential)
  * [Cloud](#cloud)
  * [Package Manager](#package-manager)
  * [User Programs](#user-programs)
  * [Gaming](#gaming)
  * [Fonts](#fonts)
  * [Utils](#utils)

## Cheatsheet

#### Package management

- List of explicitly installed packages
  
  > pacman -Qqetn

- List of explicitly installed AUR/other packages
  
  > pacman -Qqetm

- List of unused packages
  
  > pacman -Qtdq

- Package detailed information
  
  > pacman -Qii

- List of modified /etc configurations
  
  > sudo pacman -Qii | awk '/^MODIFIED/ {print $2}'

- Package tree dependencies
  
  > pactree

- Package files in use
  
  > pkgfile

- .pacsave & .pacnew files
  
  > pacdiff

## Installed packages

### Kernels

* linux-zen linux-zen-headers

### Graphics

* xorg
* xorg-xinit
* nvidia
* nvidia-utils
* nvidia-dkms
* lib32-nvidia-utils
* nvidia-settings

### Shell

* bash
* zsh
* zsh-syntax-highlighting 
* zsh-autosuggestions 
* zsh-history-substring-search 
* [AUR] <mark>bash-zsh-insulter</mark>

### WM

* qtile + python-dbus-next + python-psutil
* rofi + papirus-icon-theme --> https://github.com/adi1090x/rofi
* xscreensaver
* feh
* _[_**AUR**_]_ picom (picom-ibhagwan-git for rounded corners)

### Network

* NetworkManager

### Bluetooth

* bluez
* bluez-utils

### Peripherals

* libratbag
* piper

### Hardware

* lm_sensors 
* cpupower
* _[_**AUR**_]_ headsetcontrol
* redshift

### Video

* mpv
* ffmpegthubnailer (ranger preview)

### PDF

* zathura zathura-pdf-poppler

### Sound

* alsa-utils
* pulseaudio
* pavucontrol (GUI)
* _[_**AUR**_]_ noise-suppresion-for-voice

### Music

* _[_**AUR**_]_ spotify

### Browser

* firefox
* qutebrowser

### Editor

* nvim
  * neovim-symlinks
    * xclip
    * fzf, ripgrep, universal-ctags, the_silver_searcher, fd
    * nodejs
    * npm
* neovide
* emacs

### Appearance

* lxappearance
* qt5ct

### File explorer

* ranger
* pcmanfm

### Terminal emulator

* alacritty

### Essential

* git
* grub
* unzip / zip
* unrar / rar

### Cloud

* nextcloud-client

### Package manager

* pacman-contrib (pactree)
* multilib
* yay

### User Programs

* telegram-desktop
* discord
* _[_**AUR**_]_ mailspring
* _[_**AUR**_]_ plex-media-player
* _[_**AUR**_]_ srain - IRC Client
* transmission-gtk
* _[_**AUR**_]_ marktext-bin

### Gaming

* steam
* _[_**AUR**_]_ proton
* _[_**AUR**_]_ minecraft-launcher
* _[_**AUR**_]_ spigot

### Fonts

* nerd-fonts-complete
* _[_**AUR**_]_ ttf-font-awesome-4
* ttf-font-awesome
* _[_**AUR**_]_ ttf-iosevka-fixed-ss18

### Utils

* screen
* tmux
* os-prober
* base-devel
* python-setuptools
* gnome-keyring
* openssh
* xbindkeys -mk
* xcape
* exa
* _[_**AUR**_]_ md2pdf
* bat
* ripgrep
* fd
* starship
* neofetch
* htop
* bashtop
* flameshot
* docker
* docker-compose
* virtualbox
* virtualbox-host-dkms
