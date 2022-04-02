from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar, Gap
from libqtile import layout, hook, widget, qtile
import subprocess

from config import reload

# My functions
reload("function")
import function

screen_width = 2560 # int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"x" -f1', shell=True, stdout=subprocess.PIPE).communicate()[0])
screen_width_2 = 1080
screen_height_2 = 1920
size_of_font = int(screen_width/120)
size_of_separator = int(screen_width/320)
size_of_padding = int(screen_width/960)
size_of_bar_height= int(screen_width/80)

margin = 15

### Colors
_colors = [
    '1b1c26',   # Icon, Bar color 1, widget font
    'ffffff',   # Unused
    'ffffff',   # Unused
    'd7de59',   # Bar color 2, focused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
    'ffffff',   # Unused
    '7b7b7b',   # Bar color 3, unfocused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
]

map_color = lambda c: [f'#{c}', f'#{c}']
colors = tuple(map(map_color, _colors))

SCREEN_WIDTH = screen_width
DEFAULT_FONT = 'Iosevka Nerd'
WIDGET_FONT_SIZE = int(SCREEN_WIDTH/120)
PADDING_SIZE = int(SCREEN_WIDTH/960)

widget_default_values = dict(
    font = DEFAULT_FONT,
    fontsize = WIDGET_FONT_SIZE,
    padding = PADDING_SIZE,
    foreground = _colors[0],
    background = _colors[0]
)

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
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7])
    ], 3, 7, True) + init_right_section([
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
        widget.Clock(background=colors[3],format= '%H:%M'),
    ], 7, 3)

def init_right_side_secondary():
    return init_right_section([
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7])
    ], 3, 7, first=True) + init_right_section([
        widget.TextBox(
            text="pkgs ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Q')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Q')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Qqetn')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-installed-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Qqetn')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Qqetm')}
        ),
        widget.GenPollText(
            background = colors[3],
            update_interval = 600,
            func = function.exec_script('num-yay-pkgs'),
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Qqetm')}
        ),
        widget.TextBox(
            text=" ",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e ' + SCRIPTS_DIR + 'up')},
        ),
        widget.CheckUpdates(
                update_interval = 60,
                distro = "Arch_checkupdates",
                display_format = "{updates} Updates",
                no_update_string = "No updates",
                colour_no_updates = colors[0],
                colour_have_updates = "df0000",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e ' + SCRIPTS_DIR + 'up')},
                background = colors[3]
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
        widget.Clock(background=colors[3],format= '%d-%m-%y %A %H:%M'),
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