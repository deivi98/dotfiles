# Deivi's dotfiles

![Rice](https://i.imgur.com/LunUaax.jpg)

## Summary
| My system  	                                  | Info - Package/s  	                        |
|---------------------------------------------- |-------------------------------------------- |
| _OS_  	                                      | Arch Linux  	                              |
| _Kernel_   	                                  | `linux-zen`  	                              |
| _Package Manager_  	                          | `pacman`  	                                |
| _AUR package manager_  	                      | `yay`  	                                    |
| _Shell_  	                                    | `zsh`  	                                    |
| _Terminal emulator_  	                        | `alacritty`  	                              |
| _Browser_                                     | `chromium`  	                              |
| _Editor_  	                                  | `editor`  	                                |
| _File explorer (terminal)_  	                | `ranger`  	                                |
| _File explorer (gui)_  	                      | `pcmanfm`  	                                |
| _Compositor_  	                              | `picom-ibhagwan-git`  	                    |
| _WM_  	                                      | `qtile`  	                                  |
| _Display manager_  	                          | n/a  	                                      |
| _Launcher_  	                                | `rofi`  	                                  |
| _Screen saver_  	                            | `xscreensaver`  	                          |
| _Background_  	                              | `feh`  	                                    |
| _Notification daemon_  	                      | `dunst`  	                                  |
| _Music daemon_  	                            | `spotifyd`  	                              |
| _Music client_  	                            | `spotify-tui`  	                            |
| _Screenshots_  	                              | `flameshot`  	                              |
| _Eye care_  	                                | `redshift`  	                              |
| _Video player_  	                            | `mpv`  	                                    |
| _PDF reader_  	                              | `zathura`  	                                |

## Installation
1. Clone this repo `git clone https://github.com/deivi98/dotfiles`
2. Go into directory `cd dotfiles`
3. Remove git directory `rm -rf .git`
3. Copy config files into your $HOME `cp -Rf . ~ && cd -`
4. Remove installation folder `rm -rf dotfiles`

## Warning
By following the steps above you could delete/overwrite your personal dotfiles. I am not responsible for this. Please use at your own risk.

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
* `yay` for AUR packages

#### WM
* `qtile python-dbus-next python-psutil` as window manager
* `rofi rofi-emoji rofi-calc papirus-icon-theme` as window run dialog
* `xscreensaver` as screen saver
* `feh` as background changer
* [NOT] `conky-lua-nv` as background monitor
* `dunst` as notification daemon
* **[AUR]** `picom-ibhagwan-git` as compositor

#### Terminal emulator
* `alacritty`

#### Shell
* `zsh zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search`
* **[AUR]** `bash-zsh-insulter`
* `exa bat ripgrep fd starship neofetch screen tmux btop`

#### File explorer
* `ranger ffmpegthubnailer` command line
* `pcmanfm` as gui

#### Editor
* `neovim nodejs npm cargo lvim`

#### Browser
* `chromium`

#### Multimedia
Multimedia packages.

##### Video
* `mpv youtube-dl streamlink` as video player
* **[AUR]** `ytfzf` as youtube player
* `https://github.com/mrxdst/webtorrent-mpv-hook`

##### Music
* `spotifyd`
* **[AUR]** `spotify-tui`

##### PDF
* `zathura zathura-pdf-poppler`

#### Appearance
Appearance packages.

##### Graphical interfaces
* `lxappearance` as GTK manager
* `qt5ct` as Qt manager

##### Fonts
* `ttf-font-awesome` 
* **[AUR]** `nerd-fonts-complete ttf-font-awesome-4 ttf-iosevka-fixed-ss18`

------------------------------------------------------------------------------------------------

### User
User custom packages.

#### Cloud
* `nextcloud-client`

#### Apps
* `telegram-desktop discord transmission-gtk virtualbox virtual-host-dkms flameshot`
* **[AUR]** `mailspring plex-media-player srain marktext-bin`

#### Utils
* `os-prober base-devel python-setuptools gnome-keyring openssh xbindkeys xcape docker docker-compose`

#### Essential
* `git grub unzip zip unrar`

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
* `networkmanager`

#### Sound
* `alsa-utils pulseaudio pavucontrol`
* **[AUR]** `headsetcontrol noise-suppresion-for-voice`

#### Bluetooth
* `bluez bluez-utils`

#### Peripherals
* `libratbag piper imwheel`

## Cheatsheet
* `pacman Qqetn` List of explicitly installed packages
* `pacman -Qqetm` List of explicitly installed AUR/other packages
* `pacman -Qtdq` List of unused packages
* `pacman -Qii` Package detailed information
* `sudo pacman -Qii | awk '/^MODIFIED/ {print $2}'` List of modified /etc configurations
* `pactree` Package tree dependencies
* `pkgfile` Package files in use
* `pacdiff` .pacsave & .pacnew files
