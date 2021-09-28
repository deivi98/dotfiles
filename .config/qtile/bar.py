import subprocess

from libqtile.config import Screen
from libqtile.bar import Bar
from libqtile import widget, qtile
from libqtile.log_utils import logger

from keybindings import terminal
from colors import colors

screen_width = int(subprocess.Popen('xrandr | grep primary | cut -d" " -f4 | cut -d"+" -f1 | cut -d"x" -f1', shell=True, stdout=subprocess.PIPE).communicate()[0])

size_of_font = int(screen_width/120)
size_of_separator = int(screen_width/320)
size_of_padding = int(screen_width/960)
size_of_bar_height= int(screen_width/80)

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
