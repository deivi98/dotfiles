import os
import subprocess

from libqtile import hook, qtile
from libqtile.log_utils import logger

from settings import SCRIPTS_DIR

### Autostart programs
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(SCRIPTS_DIR + "autostart")
    subprocess.call([home])

# Auto float dialog
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

# Bring all floating windows to front
@hook.subscribe.focus_change
def float_to_front():
    for screen in qtile.screens:
        for window in screen.group.windows:
            if window.floating:
                window.cmd_bring_to_front()
