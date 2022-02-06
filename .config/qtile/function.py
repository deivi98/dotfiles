import subprocess
from threading import Thread
from time import sleep
from libqtile.log_utils import logger

# Swap groups between screens
def swap_screens(qtile):
    groupName = qtile.screens[0].group
    qtile.screens[1].set_group(groupName)

def focusWindow(qtile, wName: str) -> bool:

    for group in qtile.cmd_groups():
        windows = qtile.cmd_groups()[group]['windows']

        for windowName in windows:
            if wName.lower() in windowName.lower() and ("chromium" not in windowName.lower() or "chromium" in wName.lower()):

                if qtile.screens[0].group.name != group:
                    qtile.screens[0].cmd_toggle_group(group)

                screenWindows = qtile.screens[0].group.windows
                windowObj = list(filter(lambda x: (x.name == windowName), screenWindows))[0]
                qtile.screens[0].group.focus(windowObj, True, True)
                return True

    return False

def waitAndFocus(qtile, wName: str):
    i = 0
    while not focusWindow(qtile, wName) and i < 100:
        sleep(0.05)
        i += 1

# Navigate to app window or create it if it does not exist
def gotoapp_or_create(qtile, app, wName = None):

    if wName == None:
        wName = app

    if not focusWindow(qtile, wName):
        qtile.cmd_spawn(app)
        thread = Thread(target = waitAndFocus, args = (qtile, wName, ))
        thread.start()

# Run cmd
def run_cmd(qtile, cmd):
    qtile.cmd_spawn(cmd, shell=True)

# Mute mic and speakers
def mute_all(qtile):
    # run_cmd(qtile, 'amixer -D pulse sset Capture toggle && amixer -D pulse sset Master toggle')
    run_cmd(qtile, 'pactl set-sink-mute @DEFAULT_SINK@ toggle && pactl set-source-mute @DEFAULT_SOURCE@ toggle')

def run_shell_command(cmd):
    return str(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0])[2:-3]

# Exec script
def exec_script(script):
    return lambda: subprocess.Popen('/home/david/.config/qtile/scripts/' + script, shell=True, stdout=subprocess.PIPE).communicate()[0].decode()

# Switch keyboard layout between [US, ES]
def switch_keyboard_layout(qtile):
    current_layout = run_shell_command('setxkbmap -query | grep layout | cut -d" " -f6')

    if current_layout == "us":
        run_cmd(qtile, 'setxkbmap -layout es')
    else:
        run_cmd(qtile, 'setxkbmap -layout us')

    run_cmd(qtile, "xset r rate 200 50 && setxkbmap -option 'caps:ctrl_modifier' && xcape -e 'Caps_Lock=Escape'")

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

# Random background
def random_background(qtile):
    run_cmd(qtile, "feh --recursive --no-fehbg --bg-fill --randomize ~/.config/wallpapers/nature")

def open_help(qtile):
    run_cmd(qtile, 'md2pdf /home/david/.config/qtile/README.md')
    qtile.cmd_spawn('zathura /home/david/.config/qtile/README.pdf')

# Quick fix of github.com/qtile/qtile/issues/2167 bug
def terminal_app(qtile, app: str, args: str = "", terminal: str = "alacritty", windowName: str = None, sleep: float = 0, goto: bool = True):
    if not windowName:
        windowName = app.capitalize()

    if args != "":
        args = " " + args

    func = f'{terminal} --title "{windowName}" -e sh -c "sleep {sleep} && {app}{args}"'

    if goto:
        gotoapp_or_create(qtile, func, windowName)
    else:
        qtile.cmd_spawn(func)
