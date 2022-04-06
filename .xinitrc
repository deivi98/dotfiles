#!/bin/sh
#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |  github.com/deivi98
# | |_| | |  __/ | |  \ V /  | |  
# |____/   \___| |_|   \_/   |_|
#

######################################
#             XINIT CONFIG           #
######################################

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# Merge in defaults and keymaps
if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# Start some nice programs
if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

######################################
#              MY CONFIG             #
######################################

# Change key delay and repeat
xset r rate 200 50

# Set Caps Lock as CTRL modifier and ESC when alone
setxkbmap -option 'caps:ctrl_modifier'
xcape -e 'Caps_Lock=Escape'

# Increasing mouse wheel speed
# imwheel -b 45

# Sets random wallpaper (add --no-fehbg to not generate ~/.fehbg)
feh --recursive --no-fehbg --bg-fill --randomize ~/.local/share/wallpapers/nature &

# Starts compositor process in the background
picom --experimental-backends --backend glx --xrender-sync-fence &

# Start Dunst
dunst &

# Starts qtile
exec qtile start 
