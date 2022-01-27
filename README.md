# Deivi's ~/.dotfiles

Hi there, these are my own dotfiles :)

![Rice](https://i.imgur.com/LunUaax.jpg)

## Table of contents

* [Installed Packages](#installed-packages)
  * [Arch Linux](#arch-linux)
    * [Boot](#boot)
    * [Package managing](#package-managing)
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
  * [User](#user)
    * [Apps](#apps)
    * [Cloud](#cloud)
    * [Utils](#utils)
    * [Essential](#essential)
    * [Gaming](#gaming)
  * [Hardware](#hardware)
    * [Graphics](#graphics)
    * [Network](#network)
    * [Sound](#sound)
    * [Bluetooth](#bluetooth)
    * [Peripherals](#peripherals)
* [Cheatsheet](#cheatsheet)

## Installed packages
A list of all important packages installed on my machine.

------------------------------------------------------------------------------------------------

### Arch Linux
Main operative system packages. Software related.

#### Boot
* `linux linux-headers`
* `linux-zen linux-zen-headers` for gaming

#### Package managing
* `pacman-contrib` includes pactree, pacdiff
* `multilib` for 32bit apps
* `yay` for AUR packages

#### WM
* `qtile python-dbus-next python-psutil` as window manager
* `rofi papirus-icon-theme` as window run dialog
* `xscreensaver` as screen saver
* `feh` as background changer
* **[AUR]** `picom-ibhagwan-git` as compositor

#### Terminal emulator
* `alacritty`

#### Shell
* `zsh zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search`
* **[AUR]** `bash-zsh-insulter`
* `exa bat ripgrep fd starship neofetch screen tmux htop bashtop`

#### File explorer
* `ranger ffmpegthubnailer` command line
* `pcmanfm` as gui

#### Editor
* `lvim`

#### Browser
* `firefox`

#### Multimedia
Multimedia packages.

##### Video
* `mpv` as video player

##### Music
* **[AUR]** `spotify`

##### PDF
* `zathura zathura-pdf-poppler`

#### Appearance
Appearance packages.

##### Graphical interfaces
* `lxappearance` as GTK manager
* `qt5ct` as Qt manager

##### Fonts
* `nerd-fonts-complete ttf-font-awesome` 
* **[AUR]** `ttf-font-awesome-4 ttf-iosevka-fixed-ss18`

------------------------------------------------------------------------------------------------

### User
User custom packages.

#### Cloud
* `nextcloud-client`

#### Apps
* `telegram-desktop discord transmission-gtk virtualbox virtual-host-dkms`
 **[AUR]** `mailspring plex-media-player srain marktext-bin`

#### Utils
* `os-prober base-devel python-setuptools gnome-keyring openssh xbindkeys xcape docker docker-compose flameshot`
* **[AUR]** `md2pdf`

#### Essential
* `git grub unzip zip unrar rar`

#### Gaming
* `steam`
* **[AUR]** `proton minecraft-launcher spigot`

------------------------------------------------------------------------------------------------

### Hardware
List of hardware packages.

#### Sensors
* `cpupower lm_sensors`

#### Graphics
* `xorg xorg-xinit nvidia nvidia-utils nvidia-dkms lib32-nvidia-utils nvidia-settings redshift`

#### Network
* `NetworkManager`

#### Sound
* `alsa-utils pulseaudio pavucontrol`
* **[AUR]** `headsetcontrol noise-suppresion-for-voice`

#### Bluetooth
* `bluez bluez-utils`

#### Peripherals
* `libratbag piper`

## Cheatsheet
* `pacman Qqetn` List of explicitly installed packages
* `pacman -Qqetm` List of explicitly installed AUR/other packages
* `pacman -Qtdq` List of unused packages
* `pacman -Qii` Package detailed information
* `sudo pacman -Qii | awk '/^MODIFIED/ {print $2}'` List of modified /etc configurations
* `pactree` Package tree dependencies
* `pkgfile` Package files in use
* `pacdiff` .pacsave & .pacnew files
