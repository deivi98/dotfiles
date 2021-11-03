#  ____           _           _ 
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |    	https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#

#!/bin/sh
userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps
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

# start some nice programs
if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Change key delay and repeat
xset r rate 200 45
# Sets random wallpaper
feh --recursive --no-fehbg --bg-fill --randomize ~/.config/wallpapers/nature
# Starts screensaver process in the background
xscreensaver -no-splash &
# Starts compositor process in the background
picom --experimental-backends --backend glx --xrender-sync-fence &
# Starts Qtile
exec qtile start 
