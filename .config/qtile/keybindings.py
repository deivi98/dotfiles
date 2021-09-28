import subprocess

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.log_utils import logger

# Global variables
mod = "mod1"
mod2 = "mod4"
terminal = "alacritty"      # My terminal of choice
browser = "firefox"         # My browser of choice
fileExplorer = "ranger"     # My file explorer of choice
home = "/home/david"        # My home directory

# Swap groups between screens
def swap_screens(qtile):
    groupName = qtile.screens[0].group
    qtile.screens[1].set_group(groupName)

# Run cmd
def run_cmd(qtile, cmd):
    qtile.cmd_spawn(cmd, shell=True)

# Mute mic and speakers
def mute_all(qtile):
    # run_cmd(qtile, 'amixer -D pulse sset Capture toggle && amixer -D pulse sset Master toggle')
    run_cmd(qtile, 'pactl set-sink-mute @DEFAULT_SINK@ toggle && pactl set-source-mute @DEFAULT_SOURCE@ toggle')

# Switch keyboard layout between [US, ES]
def switch_keyboard_layout(qtile):
    current_layout = str(subprocess.Popen('setxkbmap -query | grep layout | cut -d" " -f6', shell=True, stdout=subprocess.PIPE).communicate()[0])[2:-3]

    if current_layout == "us":
        run_cmd(qtile, 'setxkbmap -layout es && xset r rate 200 35')
    else:
        run_cmd(qtile, 'setxkbmap -layout us && xset r rate 200 35')

# Switch sound output (Headphones, Speakers)
def switch_sound_output(qtile):
    current_sink = str(subprocess.Popen('pacmd stat | grep "Default sink name" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0])[2:-3]

    if current_sink == "alsa_output.pci-0000_01_00.1.hdmi-stereo":
        run_cmd(qtile, 'pacmd set-default-sink alsa_output.usb-Corsair_Corsair_VOID_PRO_Wireless_Gaming_Headset-00.analog-stereo')
    else:
        run_cmd(qtile, 'pacmd set-default-sink alsa_output.pci-0000_01_00.1.hdmi-stereo')

def fix_cli_app(app: str, args: str = "") -> str:
    """Quick fix of github.com/qtile/qtile/issues/2167 bug"""
    return f'alacritty --title {app.capitalize()} -e sh -c "sleep 0.2 && {app} {args}"'

# Qtile keybindings
keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc='Launches my terminal'
        ),
    Key([mod], "space",
        lazy.spawn('rofi -combi-modi window,drun,ssh -font "hack 20" -show combi -icon-theme "Papirus" -show-icons'),
        desc='Run Launcher'
        ),
    Key([mod2], "space",
        lazy.function(switch_keyboard_layout),
        desc='Switch keyboard layout'
        ),
    Key([mod], "b",
        lazy.spawn(browser),
        desc='Firefox'
        ),
    Key([mod], "f",
        lazy.spawn(fix_cli_app('ranger')),
        desc='Ranger'
        ),
    Key([mod, "shift"], "u",
        lazy.spawn(fix_cli_app('htop')),
        desc='Htop'
        ),
    Key([mod], "c",
        lazy.spawn(fix_cli_app('ranger', '/mnt/hdd/nextcloud')),
        desc='Nextcloud'
        ),
    Key([mod, "shift"], "c",
        lazy.spawn(fix_cli_app('ranger', '/home/david/.config/qtile')),
        desc='Qtile config'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod], "BackSpace",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key([mod, "control"], "BackSpace",
        lazy.spawn("shutdown now"),
        desc='Shutdown computer'
        ),
    Key([mod, "control"], "r",
        lazy.spawn("reboot"),
        desc='Restart computer'
        ),
    ### Swap monitors
    Key([mod], "y",
        lazy.function(swap_screens),
        desc='Swap group between monitors'
        ),
    ### Switch focus of monitors
    Key([mod], "period",
        lazy.to_screen(0),  # lazy.next_screen()
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.to_screen(1),  # lazy.prev_screen()
        desc='Move focus to prev monitor'
        ),
    ### Move windows to monitors
    Key([mod, "shift"], "period",
        lazy.window.toscreen(0),
        lazy.to_screen(0),
        desc='Move window and focus to next monitor'
        ),
    Key([mod, "shift"], "comma",
        lazy.window.toscreen(1),
        lazy.to_screen(1),
        desc='Move window and focus to prev monitor'
        ),
    ### Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up'
        ),
    Key([mod], "h",
        lazy.layout.left(),
        desc='Move focus left'
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc='Move focus right'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc='Move window down'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc='Move window up'
        ),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc='Move window left'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc='Move window right'
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc='Move window down'
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc='Move window up'
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc='Move window left'
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc='Move window right'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='Normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='Toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    ### ------------ Hardware Configs ------------
    ### Volume
    Key([], "XF86AudioMute",
        lazy.function(mute_all),
        desc='Mute audio'
        ),
    Key([], "XF86AudioLowerVolume",
        # lazy.spawn("amixer -D pulse sset Master 2%-"),
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"),
        desc='Volume down'
        ),
    Key([], "XF86AudioRaiseVolume",
        # lazy.spawn("amixer -D pulse sset Master 2%+"),
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),
        desc='Volume up'
        ),
    Key([mod], "o",
        lazy.function(switch_sound_output),
        desc='Switch audio output'
        ),
    ### Media keys (Spotify)
    Key([], "XF86AudioPlay",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.PlayPause"),
        desc='Audio play'
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Next"),
        desc='Audio next'
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Previous"),
        desc='Audio previous'
        )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
