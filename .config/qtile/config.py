#  ____           _           _
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |    https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#

import os
import subprocess

from typing import List                             # noqa: F401
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile import layout, hook
from libqtile.lazy import lazy
from libqtile.bar import Bar
from libqtile import widget, qtile
from libqtile.log_utils import logger

# My functions
from functions import swap_screens, run_cmd, mute_all, switch_keyboard_layout, switch_sound_output, fix_cli_app

### Autostart programs
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

### Global variables
mod = "mod1"
mod2 = "mod4"
terminal = "alacritty"      # My terminal of choice
browser = "firefox"         # My browser of choice
fileExplorer = "ranger"     # My file explorer of choice
home = "/home/david"        # My home directory

### Qtile keybindings
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

### Colors
_colors = [
    '1b1c26',   # Icon, Bar color 1, widget font
    'ffffff',   # Unused
    'ffffff',   # Unused
    '78dd5a',   # Bar color 2, focused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
    'ffffff',   # Unused
    'a8a885',   # Bar color 3, unfocused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
]

map_color = lambda c: [f'#{c}', f'#{c}']
colors = tuple(map(map_color, _colors))

### LAYOUTS

# Layout default settings
layout_theme = {
    "border_width": 4,
    "margin": 12,
    "border_focus": _colors[3],
    "border_normal": _colors[7]
}

# Qtile active layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.Stack(num_stacks=1, name="tabs", **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

### WORKSPACES

# Group names (icons taken from https://fontawesome.com/v4.7/cheatsheet/)
group_names = [
    ("", {'layout': 'tabs', 'matches': [Match(wm_class='firefox')]}),                   # Firefox
    ("", {'layout': 'columns'}),                                                       # Terminal
    ("", {'layout': 'columns', 'matches': [Match(wm_class='code')]}),                  # Code
    ("", {'layout': 'tabs', 'matches': [                                               # Game
        Match(title='Counter-Strike'),
        Match(title='Brawlhalla'),
        Match(title='Rocket League')
    ]}),
    ("", {'layout': 'tabs', 'matches': [Match(title='Steam')]}),                       # Steam
    ("", {'layout': 'columns', 'matches': [Match(wm_class='discord')]}),               # Discord
    ("", {'layout': 'columns', 'matches': [Match(wm_class='telegram-desktop')]}),      # Telegram
    ("", {'layout': 'columns', 'matches': [Match(wm_class='mailspring')]}),            # Mail client
    ("", {'layout': 'columns', 'matches': [Match(title='Spotify')]})                   # Spotify
]

# Qtile groups
groups = [Group(name, **kwargs) for name, kwargs in group_names]

# Adds keybindings for each group
for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.to_screen(0), lazy.group[name].toscreen(toggle=False)))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

### WIDGETS

# Sizes
screen_width = int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"+" -f1 | cut -d"x" -f1', shell=True, stdout=subprocess.PIPE).communicate()[0])
size_of_font = int(screen_width/120)
size_of_separator = int(screen_width/320)
size_of_padding = int(screen_width/960)
size_of_bar_height= int(screen_width/80)

# Default widget settings
widget_defaults = dict(
    font='Iosevka Fixed',
    fontsize=size_of_font,
    padding=size_of_padding,
    foreground = colors[0],
    background=colors[0]
)

# Default extension settings
extension_defaults = widget_defaults.copy()

# Widget inits

def icon_settings():
	return {
		'padding': 0,
		'fontsize': 28
	}

def left_arrow(color1, color2):
	return widget.TextBox(
		text = '\uE0B2',
		background = color1,
		foreground = color2,
		**icon_settings()
	)

def right_arrow(color1, color2):
	return widget.TextBox(
		text = '\uE0B0',
		background = color1,
		foreground = color2,
		**icon_settings()
	)

def init_left_section(widgets, backgroundColor, foregroundColor, arrow=True):
    section = [widget.Sep(padding=size_of_separator, linewidth=0, background=colors[foregroundColor])] + widgets
    if arrow:
        section += [right_arrow(colors[backgroundColor], colors[foregroundColor])]
    return section

def init_right_section(widgets, backgroundColor, foregroundColor, first=False):
    arrowBackground = backgroundColor
    if first:
        arrowBackground = 0
    section = [left_arrow(colors[arrowBackground], colors[foregroundColor])]
    return section + widgets + [widget.Sep(padding=size_of_separator, linewidth=0, background=colors[foregroundColor])]

def init_left_side():
    return init_left_section([
            widget.TextBox(
                text="",
                font="FontAwesome",
                background=colors[3],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
            )
        ], 7, 3) + init_left_section([
            widget.GroupBox(
                background=colors[7],
                this_current_screen_border = colors[3],
                this_screen_border = colors[3],
                other_current_screen_border=colors[7],
                other_screen_border=colors[7],
                hide_unused = False,
                rounded = True,
                highlight_method = 'block',
                font='FontAwesome',
                padding_y=size_of_padding*2,
                active=colors[0],
                inactive=colors[0],
            )
        ], 0, 7) + init_left_section([
            widget.WindowName(
                background=colors[0],
                foreground=colors[3],
                format='{state}{name}'
            )
        ], 3, 0, arrow=False)

def init_right_side():
    return init_right_section([
        widget.Mpris2(
            background=colors[7],
            fmt='  {}...',
            scroll_chars=50,
            scroll_wait_intervals=40000,
            objname='org.mpris.MediaPlayer2.spotify'
        )
    ], 3, 7, first=True) + init_right_section([
        widget.TextBox(text="", background=colors[3]),
        widget.Systray(background=colors[3], **icon_settings())
    ], 7, 3) + init_right_section([
        widget.KeyboardLayout(background=colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7])
    ], 3, 7) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.CheckUpdates(
                update_interval = 600,
                distro = "Arch_yay",
                display_format = "{updates} Updates",
                no_update_string = "No updates",
                colour_no_updates = colors[0],
                colour_have_updates = "bd0f0f",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
                background = colors[3]
        )
    ], 7, 3) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Volume(
            background=colors[7],
            get_volume_command=['/home/david/.config/qtile/scripts/getVolume.sh', 'alsa_output.usb-Corsair_Corsair_VOID_PRO_Wireless_Gaming_Headset-00.analog-stereo']
        ),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Volume(
            background=colors[7],
            get_volume_command=['/home/david/.config/qtile/scripts/getVolume.sh', 'alsa_output.pci-0000_01_00.1.hdmi-stereo']
        )
    ], 3, 7) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.Clock(background=colors[3],format= '%H:%M')
    ], 7, 3) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Clock(background=colors[7], format= '%d %b, %A'),
    ], 3, 7)

def init_right_side_secondary():
    return init_right_section([
        widget.KeyboardLayout(background=colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7])
    ], 3, 7, first=True) + init_right_section([
        widget.TextBox(text=" GPU ",font="FontAwesome",background=colors[3]),
        widget.NvidiaSensors(
            background=colors[3],
            foreground=colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        )
    ], 7, 3) + init_right_section([
        widget.TextBox(text=" ",font="FontAwesome",background=colors[7]),
        widget.Memory(
            background=colors[7],
            format='{MemUsed:6.0f}/{MemTotal:6.0f}{mm}',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        )
    ], 3, 7) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.HDDGraph(
            background=colors[3],
            border_width=0,
            graph_color=colors[0],
            fill_color=colors[0],
            path='/mnt/hdd',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        )
    ], 7, 3) + init_right_section([
        # widget.CPU(background=colors[3],format='{load_percent:>7.2f}%'),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.ThermalSensor(
            background=colors[7],
            foreground=colors[0],
            tag_sensor='Package id 0',
            # format='{MemUsed: 6.0f}/{MemTotal: 6.0f}{mm}',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        ),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CPUGraph(
            background=colors[7],
            border_width=0,
            graph_color=colors[0],
            fill_color=colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        )
    ], 3, 7) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        # widget.Net(background=colors[7],format = '{down:>20} ↓↑ {up:>20}'),
        widget.NetGraph(
            background=colors[3],
            border_width=0,
            graph_color=colors[0],
            fill_color=colors[0],
            interface='enp0s31f6',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        )
    ], 7, 3) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Volume(
            background=colors[7],
            get_volume_command=['/home/david/.config/qtile/scripts/getVolume.sh', 'alsa_output.usb-Corsair_Corsair_VOID_PRO_Wireless_Gaming_Headset-00.analog-stereo']
        ),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Volume(
            background=colors[7],
            get_volume_command=['/home/david/.config/qtile/scripts/getVolume.sh', 'alsa_output.pci-0000_01_00.1.hdmi-stereo']
        )
    ], 3, 7) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.Clock(background=colors[3],format= '%H:%M')
    ], 7, 3)

def init_top_bar(secondary=False):
    widgets = init_left_side()
    if secondary:
        widgets += init_right_side_secondary()
    else:
        widgets += init_right_side()
    return Bar(widgets=widgets, opacity=1.0, size=size_of_bar_height)

def init_screen(secondary=False):
    return Screen(top=init_top_bar(secondary))

screens = [
	init_screen(),
	init_screen(secondary=True)
]

### OTHER CONFIG VALUES

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),         # gitk
    Match(wm_class='makebranch'),           # gitk
    Match(wm_class='maketag'),              # gitk
    Match(wm_class='ssh-askpass'),          # ssh-askpass
    Match(title='branchdialog'),            # gitk
    Match(title='pinentry'),                # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
