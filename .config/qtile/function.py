import subprocess
from threading import Thread
from time import sleep
from libqtile.log_utils import logger

# Swap groups between screens
def swap_screens(qtile):
    groupName = qtile.screens[0].group
    qtile.screens[1].set_group(groupName)

def focusWindow(qtile, wName: str) -> bool:

    # For every existing group / workspace
    for group in qtile.cmd_groups():
        windows = qtile.cmd_groups()[group]['windows']
        # For every existing window in each group / workspace

        for windowName in windows:

            # Match window if title contains regex but it's not chromium
            if wName.lower() in windowName.lower() and ("chromium" not in windowName.lower() or "chromium" in wName.lower()):

                presentIn = -1;

                # Find group in any screen
                for i in range(len(qtile.screens)):
                    if qtile.screens[i].group.name == group:
                        presentIn = i;
                        break;

                # If group is not selected in any screen, set it to primary screen
                if presentIn < 0:
                    qtile.screens[0].cmd_toggle_group(group);
                    presentIn = 0;

                # Make sure screen is focused
                qtile.cmd_to_screen(presentIn);

                # Make sure window is focused
                screenWindows = qtile.screens[presentIn].group.windows;
                windowObj = list(filter(lambda x: (x.name == windowName), screenWindows))[0];
                qtile.screens[presentIn].group.focus(windowObj, True, True);

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

# Exec script
def exec_script(script):
    return lambda: subprocess.Popen('/home/david/.config/scripts/' + script, shell=True, stdout=subprocess.PIPE).communicate()[0].decode()

# Switch redshift on and off
def switch_redshift(qtile):
    run_cmd(qtile, "pkill -USR1 redshift-gtk")

# Random background
def random_background(qtile):
    run_cmd(qtile, "feh --recursive --no-fehbg --bg-fill --randomize ~/.local/share/wallpapers/nature")

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
