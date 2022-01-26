# Deivi's ~/.dotfiles

Hi there, these are my own dotfiles :)

## Table of contents

* [Installed Packages](#installed-packages)
  * [Essential](#essential)
  * [Cloud](#cloud)
  * [User Programs](#user-programs)
  * [Gaming](#gaming)
  * [Utils](#utils)

  * [Arch Linux](#arch-linux)
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

  * [Hardware](#hardware)
    * [Graphics](#graphics)
    * [Network](#network)
    * [Sound](#sound)
    * [Bluetooth](#bluetooth)
    * [Peripherals](#peripherals)

* [Cheatsheet](#cheatsheet)
## Cheatsheet

### Package management

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

## Installed packages

A list of all important packages installed on my machine.

### Shell

* bash
* zsh
* zsh-syntax-highlighting 
* zsh-autosuggestions
* zsh-history-substring-search 
* **[AUR]** bash-zsh-insulter

### WM

* qtile + python-dbus-next + python-psutil
* rofi + papirus-icon-theme --> https://github.com/adi1090x/rofi
* xscreensaver
* feh
* **[AUR]** picom (picom-ibhagwan-git for rounded corners)

### Hardware

#### Kernels
* linux-zen linux-zen-headers

### CPU & Sensors
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

### Video

* mpv
* ffmpegthubnailer (ranger preview)

### PDF

* zathura zathura-pdf-poppler

### Music

* **[AUR]** spotify

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

### Pacman

* pacman-contrib (pactree)
* multilib
* yay

### User Programs

* telegram-desktop
* discord
* **[AUR]** mailspring
* **[AUR]** plex-media-player
* **[AUR]** srain - IRC Client
* transmission-gtk
* **[AUR]** marktext-bin

### Gaming

* steam
* **[AUR]** proton
* **[AUR]** minecraft-launcher
* **[AUR]** spigot

### Fonts

* nerd-fonts-complete
* **[AUR]** ttf-font-awesome-4
* ttf-font-awesome
* **[AUR]** ttf-iosevka-fixed-ss18

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
