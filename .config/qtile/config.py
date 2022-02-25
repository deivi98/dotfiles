#  ____           _           _
# |  _ \    ___  (_) __   __ (_)	David González (deivi)
# | | | |  / _ \ | | \ \ / / | |	https://deivii.es
# | |_| | |  __/ | |  \ V /  | |    https://github.com/deivi98
# |____/   \___| |_|   \_/   |_|
#

import os
import subprocess

from typing import List                             # noqa: F401
from libqtile import layout, hook, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar, Gap

# My functions
import function

### Global variables
mod = "mod1"
mod2 = "mod4"
terminal = "alacritty"                                      # My terminal of choice
browser = "chromium"                                        # My browser of choice
fileExplorer = "ranger"                                     # My file explorer of choice
editor = "lvim"                                             # My editor
home = "/home/david"                                        # My home directory
scripts = "/home/david/.config/qtile/scripts/"              # My scripts directory

### Autostart programs
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(scripts + "autostart")
    subprocess.call([home])

### Qtile keybindings
keys = [
    ### ESSENTIALS

    Key([mod], "Return",
        lazy.spawn(terminal),
        desc='Launches my terminal'
        ),
    Key([mod], "BackSpace",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "BackSpace",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key([mod, "control"], "r",
        lazy.spawn("reboot"),
        desc='Restart computer'
        ),
    Key([mod, "control"], "BackSpace",
        lazy.spawn("shutdown now"),
        desc='Shutdown computer'
        ),
    Key([mod], "slash",
        lazy.function(function.open_help),
        desc='Help'
        ),
    # Qtile config
    Key([mod], "q",
        lazy.function(function.terminal_app, editor, '/home/david/.config/qtile/config.py', windowName="Qtile config", sleep=0.1),
        desc='Qtile config'
        ),

    ### MY OWN KEYBINDINGS

    # Switch keyboard layouts
    Key([mod2], "space",
        lazy.spawn(scripts + "changelayout"),
        desc='Switch keyboard layout'
        ),
    # Launch Rofi
    Key([mod], "space",
        lazy.spawn('/home/david/.config/rofi/bin/launcher_misc'),
        desc='Run Launcher'
        ),

    ### APPLICATIONS QUICK ACCESS

    Key([mod], "b",
        lazy.function(function.gotoapp_or_create, browser, "Chromium"),
        desc='Chromium'
        ),
    Key([mod], "d",
        lazy.function(function.gotoapp_or_create, 'discord'),
        desc='Discord'
        ),
    Key([mod], "i",
        lazy.function(function.gotoapp_or_create, 'srain'),
        desc='Srain'
        ),
    Key([mod], "g",
        lazy.group[""].toscreen(toggle=False),
        desc='Game'
        ),
    Key([mod], "t",
        lazy.function(function.gotoapp_or_create, 'telegram-desktop', 'Telegram'),
        desc='Telegram'
        ),
    Key([mod], "s",
        lazy.function(function.gotoapp_or_create, 'steam'),
        desc='Steam'
        ),
    Key([mod], "m",
        lazy.function(function.terminal_app, 'spt', windowName="Spotify", sleep=0.1),
        desc='Spotify'
        ),
    Key([mod], "e",
        lazy.function(function.terminal_app, editor, windowName="LunarVim", sleep=0.1),
        desc='LunarVim'
        ),
    Key([mod], "c",
        lazy.function(function.gotoapp_or_create, 'mailspring'),
        desc='Mailspring'
        ),
    Key([mod], "f",
        lazy.function(function.terminal_app, fileExplorer, sleep=0.1),
        desc='Ranger'
        ),
    Key([mod], "n",
        lazy.function(function.terminal_app, fileExplorer, '/mnt/hdd/nextcloud', windowName="Nextcloud", sleep=0.1),
        desc='Nextcloud'
        ),

    ### ARCH INFO / CONTROLS

    # BTOP
    Key([mod], "p",
        lazy.function(function.terminal_app, 'btop', windowName="Btop"),
        desc='Btop'
        ),
    # Flameshot screenshot
    Key([mod, "shift"], "s",
        lazy.spawn(["flameshot", "gui"]),
        desc='Screenshot'
        ),
    # Switch audio output
    Key([mod, "shift"], "o",
        lazy.spawn(scripts + 'switch-output'),
        desc='Switch audio output'
        ),
    # Switch redshift
    Key([mod, "shift"], "n",
        lazy.function(function.switch_redshift),
        desc='Switch redshift'
        ),
    # Random background
    Key([mod, "shift"], "b",
        lazy.function(function.random_background),
        desc='Random background'
        ),
    # Update system
    Key([mod], "u",
        lazy.function(function.terminal_app, scripts + "up", windowName="System update"),
        desc='System update'
        ),
    # Update system (AUR)
    Key([mod, "shift"], "u",
        lazy.function(function.terminal_app, scripts + "up all", windowName="AUR system update"),
        desc='AUR system update'
        ),

    ### MONITORS

    # Swap monitors
    Key([mod], "y",
        lazy.function(function.swap_screens),
        desc='Swap group between monitors'
        ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.to_screen(0),  # lazy.next_screen()
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.to_screen(1),  # lazy.prev_screen()
        desc='Move focus to prev monitor'
        ),
    # Move windows to monitors
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

    ### WINDOW CONTROLS

    # Move through windows
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

    # Move windows
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

    # Resize windows
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

    # Switch layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),

    # Normalize sizes
    Key([mod, "control"], "n",
        lazy.layout.normalize(),
        desc='Normalize window size ratios'
        ),
    # Maximize / minimize
    Key([mod,"shift"], "m",
       lazy.window.toggle_minimize(),
       desc='Toggle window minimize'
       ),
    # Full screen
    Key([mod, "shift"], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),

    ### HARDWARE

    # Volume keys
    Key([], "XF86AudioMute",
        lazy.spawn(scripts + "changevolume mute"),
        desc='Mute audio'
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn(scripts + "changevolume down"),
        desc='Volume down'
        ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn(scripts + "changevolume up"),
        desc='Volume up'
        ),
    # Discord volume keys
    Key([mod], "XF86AudioLowerVolume",
        lazy.spawn(scripts + 'changevolume-discord down'),
        desc='Discord volume down'
        ),
    Key([mod], "XF86AudioRaiseVolume",
        lazy.spawn(scripts + 'changevolume-discord up'),
        desc='Discord volume up'
        ),
    # Spotify volume keys
    Key(["control"], "XF86AudioLowerVolume",
        lazy.spawn(scripts + 'changevolume-spotify down'),
        desc='Discord volume down'
        ),
    Key(["control"], "XF86AudioRaiseVolume",
        lazy.spawn(scripts + 'changevolume-spotify up'),
        desc='Discord volume up'
        ),

    # Media keys (Spotify)
    Key([], "XF86AudioPlay",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"),
        desc='Audio play'
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"),
        desc='Audio next'
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"),
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
    'e8942e',   # Bar color 2, focused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
    'ffffff',   # Unused
    '7b7b7b',   # Bar color 3, unfocused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
]

map_color = lambda c: [f'#{c}', f'#{c}']
colors = tuple(map(map_color, _colors))

### LAYOUTS

margin = 15

# Layout default settings
layout_theme = {
    "border_width": 2,
    "margin": [margin,margin,0,0],
    #"margin_on_single": [0,0,0,0],
    "border_on_single": True,
    "border_focus": _colors[3],
    "border_normal": _colors[7],
    "grow_amount": 5
}

stack_theme = {
    "border_width": 2,
    "border_focus": _colors[3],
    "margin": [margin,margin,0,0]
}

# Qtile active layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.Stack(num_stacks=1, name="tabs", **stack_theme)
]

### WORKSPACES

group_names = [
    ("", {'layout': 'tabs', 'matches': [                                               # Browser
        Match(wm_class='chromium'),
        Match(wm_class='firefox'),
        Match(wm_class='qutebrowser'),
        Match(wm_class='Mailspring')
    ]}),
    ("", {'layout': 'tabs', 'matches': [                                               # Files
        Match(wm_class='pcmanfm'),
        Match(title='Nextcloud'),
        Match(title='Ranger'),
        Match(title='Htop memory usage'),
        Match(title='Htop cpu usage')
    ]}),
    ("", {'layout': 'columns', 'matches': [                                            # Editor
        Match(wm_class='code'),
        Match(title='LunarVim'),
        Match(title='Qtile config')
    ]}),
    ("", {'layout': 'tabs', 'matches': [                                               # Discord
        Match(wm_class='discord'),
        Match(wm_class='srain'),
        Match(wm_class='telegram-desktop'),
        Match(title='Spotify')
    ]}),
    ("", {'layout': 'columns', 'matches': [                                            # Gaming
        Match(title='Steam'),
        Match(wm_class='csgo_linux64'),
        Match(title='Brawlhalla'),
        Match(title='Rocket League'),
        Match(wm_class='minecraft-launcher')
    ]})
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
# screen_width = int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"+" -f1 | cut -d"x" -f1', shell=True, stdout=subprocess.PIPE).communicate()[0])
screen_width = 2560
size_of_font = int(screen_width/120)
size_of_separator = int(screen_width/320)
size_of_padding = int(screen_width/960)
size_of_bar_height= int(screen_width/80)

# Default widget settings
widget_defaults = dict(
    font='Iosevka Nerd',
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
		'fontsize': 33
	}

def left_arrow(color1, color2):
	return widget.TextBox(
		# text = '\uE0B2',
		text = '\ue0be',
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
                text="",
                font="FontAwesome",
                fontsize=33,
                background=colors[3],
                foreground=colors[0],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('/home/david/.config/rofi/bin/launcher_misc')}
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
                highlight_method = 'line',
                highlight_color=colors[7],
                font="FontAwesome",
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
        widget.TextBox(
            text="pkgs ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Q')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Q')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Qqetn')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-installed-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Qqetn')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Qqetm')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-yay-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e pacman -Qqetm')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e ' + scripts + 'up')},
        ),
        widget.CheckUpdates(
                update_interval = 3600,
                distro = "Arch_checkupdates",
                display_format = "{updates} Updates",
                no_update_string = "No updates",
                colour_no_updates = colors[0],
                colour_have_updates = "df0000",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e ' + scripts + 'up')},
                background = colors[3]
        )
    ], 7, 3, first=True) + init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7])
    ], 3, 7) + init_right_section([
        widget.GenPollText(
            background=colors[3],
            func=function.exec_script('get-spotify-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome"
        ),
        widget.GenPollText(
            background=colors[3],
            func=function.exec_script('get-discord-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome"
        ),
        widget.GenPollText(
            background=colors[3],
            func=function.exec_script('get-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome"
        )
    ], 7, 3) + init_right_section([
        widget.Systray(background=colors[7], **icon_settings())
    ], 3, 7) + init_right_section([
        widget.TextBox(text=" ",font="FontAwesome",background=colors[3]),
        widget.Clock(background=colors[3],format= '%d-%m-%y %A %H:%M'),
    ], 7, 3)

def init_right_side_secondary():
    return init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.CurrentLayout(background=colors[3]),
        widget.WindowCount(text_format="[{num}]", background=colors[3])
    ], 7, 3, first=True) + init_right_section([
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[7],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop -s PERCENT_CPU')}
        ),
        widget.CPU(
            background=colors[7],
            format='{load_percent}%',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop -s PERCENT_CPU')}
        ),
        #widget.CPUGraph(
        #    background=colors[7],
        #    border_width=0,
        #    graph_color=colors[0],
        #    fill_color=colors[0],
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        #),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[7],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop -s PERCENT_MEM')}
        ),
        widget.Memory(
            background=colors[7],
            format='{MemUsed:5.0f}{mm}',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop -s PERCENT_MEM')}
        ),
        #widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        #widget.Net(background=colors[3], format = '{down:>7}  {up:>7}', font="Monospace"),
        #widget.NetGraph(
        #    background=colors[3],
        #    border_width=0,
        #    graph_color=colors[0],
        #    fill_color=colors[0],
        #    interface='enp0s31f6',
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        #)
    ], 3, 7) + init_right_section([
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
        ),
        widget.ThermalSensor(
            background=colors[3],
            foreground=colors[0],
            tag_sensor='Package id 0',
            # format='{MemUsed: 6.0f}/{MemTotal: 6.0f}{mm}',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
        ),
        widget.TextBox(
            text=" GPU ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
        ),
        widget.NvidiaSensors(
            background=colors[3],
            foreground=colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
        )
    ], 7, 3) + init_right_section([
        widget.GenPollText(
            background=colors[7],
            func=function.exec_script('get-spotify-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome"
        ),
        widget.GenPollText(
            background=colors[7],
            func=function.exec_script('get-discord-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome"
        ),
        widget.GenPollText(
            background=colors[7],
            func=function.exec_script('get-volume'),
            update_interval=0.2,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
            font="FontAwesome",
        )
    ], 3, 7) + init_right_section([
        widget.TextBox(text=" ",font="FontAwesome",background=colors[3]),
        widget.Clock(background=colors[3],format= '%H:%M'),
    ], 7, 3)

def init_top_bar(secondary=False):
    widgets = init_left_side()
    if secondary:
        widgets += init_right_side_secondary()
    else:
        widgets += init_right_side()
    return Bar(widgets=widgets, opacity=1.0, margin=[margin, margin, 0, margin], size=size_of_bar_height)

def init_screen(secondary=False):
    return Screen(
        top=init_top_bar(secondary),
        bottom=Gap(margin),
        left=Gap(margin)
    )

screens = [
	init_screen(),
	init_screen(secondary=True)
]

### OTHER CONFIG VALUES
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
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "Qtile" # X11 window manager name
