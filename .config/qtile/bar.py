import subprocess

from libqtile.config import Screen
from libqtile.bar import Bar
from libqtile import widget, qtile

from keybindings import terminal
from colors import colors

screen_width = int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"+" -f1 | cut -d"x" -f1',shell=True, stdout=subprocess.PIPE).communicate()[0])
# screen_height = int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"+" -f1 | cut -d"x" -f2',shell=True, stdout=subprocess.PIPE).communicate()[0])

size_of_font = int(screen_width/120)
size_of_separator = int(screen_width/320)
size_of_padding = int(screen_width/960)
size_of_bar_height=int(screen_width/80)

widget_defaults = dict(
    font='Iosevka Fixed',
    fontsize=size_of_font,
    padding=size_of_padding,
    foreground = colors[0],
    background=colors[0]
)

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

def init_widget_list(primaryScreen):
    left = [
        widget.Sep(padding=size_of_separator, linewidth=0, background=colors[3]),
        widget.TextBox(
            text="",
            font="FontAwesome",
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
        ),
        right_arrow(colors[7],colors[3]),
        widget.Sep(padding=size_of_separator, linewidth=0, background=colors[7]),
        widget.GroupBox(
                background=colors[7],
                this_current_screen_border = colors[3],
                this_screen_border = colors[3],
                other_current_screen_border=colors[7],
                other_screen_border=colors[7],
                hide_unused = False,
                rounded = True,
                highlight_method = 'block',
                fontsize = size_of_font,
                font='FontAwesome',
                padding_y=size_of_padding*2,
                active=colors[0],
                inactive=colors[0],
        ),
        right_arrow(colors[0],colors[7]),
        widget.Sep(padding=size_of_separator, linewidth=0, background=colors[0]),
        widget.WindowName(background=colors[0], foreground=colors[3],format='{state}{name}'),
        #right_arrow(colors[3],colors[7]),
    ]
    systray = []
    if (primaryScreen):
        systray = [
            left_arrow(colors[0],colors[3]),
            widget.TextBox(text="",background=colors[3]),
            widget.Systray(background=colors[3], **icon_settings()),
            widget.Sep(padding=size_of_separator,linewidth=0,background=colors[3],),
            left_arrow(colors[3],colors[7]),
        ]
    else:
        systray = [
            left_arrow(colors[0],colors[7]),
        ]
    right = [
        widget.Sep(padding=size_of_separator, linewidth=0, background=colors[7]),
        widget.KeyboardLayout(background=colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.CurrentLayout(background=colors[7]),
        widget.WindowCount(text_format="[{num}]", background=colors[7]),
        widget.Sep(padding=size_of_separator, linewidth=0, background=colors[7]),
        left_arrow(colors[7],colors[3]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.CheckUpdates(
                update_interval = 1800,
                distro = "Arch_yay",
                display_format = "{updates} Updates",
                no_update_string = "No updates",
                colour_no_updates = colors[0],
                colour_have_updates = "bd0f0f",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
                background = colors[3]
        ),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[3],),
        left_arrow(colors[3],colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Memory(
            background=colors[7],
            format='{MemUsed: 6.0f} / {MemTotal: 6.0f}{mm}',
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        ),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[7],),
        left_arrow(colors[7],colors[3]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.CPUGraph(
            background=colors[3],
            border_width=0,
            graph_color=colors[0],
            fill_color=colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        ),
        # widget.CPU(background=colors[3],format='{load_percent:>7.2f}%'),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[3],),
        left_arrow(colors[3],colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        # widget.Net(background=colors[7],format = '{down:>20} ↓↑ {up:>20}'),
        widget.NetGraph(
            background=colors[7],
            border_width=0,
            graph_color=colors[0],
            fill_color=colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}
        ),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[7],),

        left_arrow(colors[7], colors[3]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.PulseVolume(
            background=colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e pacmixer')}
        ),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[3],),
        left_arrow(colors[3], colors[7]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[7]),
        widget.Clock(background=colors[7],format= '%H:%M'),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[7],),
        left_arrow(colors[7], colors[3]),
        widget.TextBox(text="  ",font="FontAwesome",background=colors[3]),
        widget.Clock(background=colors[3], format= '%d %b, %A'),
        widget.Sep(padding=size_of_separator,linewidth=0,background=colors[3],),
        # widget.Bluetooth(background=colors[3]),
    ]
    return left+systray+right

def init_screen(primaryScreen):
    return Screen(top=Bar(widgets=init_widget_list(primaryScreen), opacity=1.0, size=size_of_bar_height))

screens = [
	init_screen(True),
	init_screen(False)
]
