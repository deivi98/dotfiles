# Deivi's ~/.dotfiles

Hi there, these are my own dotfiles :)

## Table of contents

. [Installed Packages](#installed-packages)
  . [Arch Linux](#arch-linux)
    * [Boot](#boot)
    * [Pacman](#pacman)
    * [WM](#wm)
    * [Terminal emulator](#terminal-emulator)
    * [Shell](#shell)
    * [File Explorer](#file-explorer)
    * [Editor](#editor)
    * [Browser](#browser)
    * [Multimedia](#multimedia)
      * [Video](#video)
      * [Music](#music)
      * [PDF](#pdf)
    * [Appearance](#appearance)
      * [Fonts](#fonts)
  . [User](#user)
    * [Main](#main)
    * [Cloud](#cloud)
    * [Utils](#utils)
    * [Essential](#essential)
    * [Gaming](#gaming)
  . [Hardware](#hardware)
    * [Graphics](#graphics)
    * [Network](#network)
    * [Sound](#sound)
    * [Bluetooth](#bluetooth)
    * [Peripherals](#peripherals)
. [Cheatsheet](#cheatsheet)

## Installed packages
A list of all important packages installed on my machine.

------------------------------------------------------------------------------------------------

### Arch Linux
Main operative system packages. Software related.

#### Boot
* linux-zen linux-zen-headers

#### Pacman
* pacman-contrib (pactree)
* multilib
* yay

#### WM
* qtile + python-dbus-next + python-psutil
* rofi + papirus-icon-theme --> https://github.com/adi1090x/rofi
* xscreensaver
* feh
* **[AUR]** picom (picom-ibhagwan-git for rounded corners)

#### Terminal emulator
* alacritty

#### Shell
* bash
* zsh
* zsh-syntax-highlighting 
* zsh-autosuggestions
* zsh-history-substring-search 
* **[AUR]** bash-zsh-insulter

#### File explorer

* ranger
* pcmanfm

#### Editor

* nvim
  * neovim-symlinks
    * xclip
    * fzf, ripgrep, universal-ctags, the_silver_searcher, fd
    * nodejs
    * npm
* neovide
* emacs

#### Browser

* firefox
* qutebrowser

#### Multimedia
Multimedia packages.

##### Video
* mpv
* ffmpegthubnailer (ranger preview)

##### Music
* **[AUR]** spotify

##### PDF
* zathura zathura-pdf-poppler

#### Appearance
Appearance packages.

##### Graphical interfaces
* lxappearance
* qt5ct

##### Fonts
* nerd-fonts-complete
* **[AUR]** ttf-font-awesome-4
* ttf-font-awesome
* **[AUR]** ttf-iosevka-fixed-ss18

------------------------------------------------------------------------------------------------

### User
User custom packages.

#### Cloud
* nextcloud-client

#### Main
* telegram-desktop
* discord
* **[AUR]** mailspring
* **[AUR]** plex-media-player
* **[AUR]** srain - IRC Client
* transmission-gtk
* **[AUR]** marktext-bin

#### Utils
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
* **[AUR]** md2pdf
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

#### Essential
* git
* grub
* unzip / zip
* unrar / rar

#### Gaming
* steam
* **[AUR]** proton
* **[AUR]** minecraft-launcher
* **[AUR]** spigot

------------------------------------------------------------------------------------------------

### Hardware
List of hardware packages.

#### Sensors
* cpupower
* lm_sensors 

#### Graphics
* xorg
* xorg-xinit
* nvidia
* nvidia-utils
* nvidia-dkms
* lib32-nvidia-utils
* nvidia-settings
* redshift

#### Network
* NetworkManager

#### Sound
* alsa-utils
* pulseaudio
* pavucontrol (GUI)
* **[AUR]** headsetcontrol
* **[AUR]** noise-suppresion-for-voice

#### Bluetooth
* bluez
* bluez-utils

#### Peripherals
* libratbag
* piper

## Cheatsheet

* List of explicitly installed packages
> pacman -Qqetn

* List of explicitly installed AUR/other packages
> pacman -Qqetm

* List of unused packages
> pacman -Qtdq

* Package detailed information
> pacman -Qii

* List of modified /etc configurations
> sudo pacman -Qii | awk '/^MODIFIED/ {print $2}'

* Package tree dependencies
> pactree

* Package files in use
> pkgfile

* .pacsave & .pacnew files
> pacdiff

