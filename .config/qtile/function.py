import subprocess
from libqtile.log_utils import logger

# Swap groups between screens
def swap_screens(qtile):
    groupName = qtile.screens[0].group
    qtile.screens[1].set_group(groupName)

# Navigate to app window or create it if it does not exist
def gotoapp_or_create(qtile, app, appName = None):

    if appName == None:
        appName = app

    for group in qtile.cmd_groups():
        windows = qtile.cmd_groups()[group]['windows']

        for windowName in windows:
            if appName.lower() in windowName.lower():

                if qtile.screens[0].group.name != group:
                    qtile.screens[0].cmd_toggle_group(group)

                screenWindows = qtile.screens[0].group.windows
                windowObj = list(filter(lambda x: (x.name == windowName), screenWindows))[0]
                windowObj.cmd_focus()
                return 1

    qtile.cmd_spawn(app)
    return 0

# Run cmd
def run_cmd(qtile, cmd):
    qtile.cmd_spawn(cmd, shell=True)

# Mute mic and speakers
def mute_all(qtile):
    # run_cmd(qtile, 'amixer -D pulse sset Capture toggle && amixer -D pulse sset Master toggle')
    run_cmd(qtile, 'pactl set-sink-mute @DEFAULT_SINK@ toggle && pactl set-source-mute @DEFAULT_SOURCE@ toggle')

def run_shell_command(cmd):
    return str(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0])[2:-3]

# Switch keyboard layout between [US, ES]
def switch_keyboard_layout(qtile):
    current_layout = run_shell_command('setxkbmap -query | grep layout | cut -d" " -f6')

    if current_layout == "us":
        run_cmd(qtile, 'setxkbmap -layout es && xset r rate 200 45')
    else:
        run_cmd(qtile, 'setxkbmap -layout us && xset r rate 200 45')

# Switch sound output (Headphones, Speakers)
def switch_sound_output(qtile):
    current_sink = run_shell_command('pacmd stat | grep "Default sink name" | cut -d" " -f4')

    if current_sink == "alsa_output.pci-0000_01_00.1.hdmi-stereo":
        run_cmd(qtile, 'pacmd set-default-sink alsa_output.usb-Corsair_Corsair_VOID_PRO_Wireless_Gaming_Headset-00.analog-stereo')
    else:
        run_cmd(qtile, 'pacmd set-default-sink alsa_output.pci-0000_01_00.1.hdmi-stereo')

# Switch redshift on and off
def switch_redshift(qtile):
    run_cmd(qtile, "pkill -USR1 redshift-gtk")

def open_help(qtile):
    run_cmd(qtile, 'md2pdf /home/david/.config/qtile/README.md')
    qtile.cmd_spawn('zathura /home/david/.config/qtile/README.pdf')

def fix_cli_app(app: str, args: str = "") -> str:
    """Quick fix of github.com/qtile/qtile/issues/2167 bug"""
    return f'alacritty --title {app.capitalize()} -e sh -c "sleep 0.2 && {app} {args}"'
