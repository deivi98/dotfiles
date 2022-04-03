from libqtile import hook, qtile
from libqtile.backend import base

sticky_win = None

# Stick focused window
def stick_win(qtile):
    global sticky_win

    if sticky_win:
        unstick_win(qtile)
    else:
        if not qtile.current_window:
            return

        if qtile.current_window:
            sticky_win = qtile.current_window
            sticky_win.cmd_static(0, -890 - 13, 535 + 57, 890, 500)

# Unstick window if exists
def unstick_win(qtile):
    global sticky_win
    if sticky_win:
        sticky_win.defunct = False
        sticky_win.cmd_toscreen(0)
        sticky_win.cmd_togroup(qtile.screens[0].group.name, True)
        sticky_win = None

# If sticky window is killed, remove
@hook.subscribe.client_killed
def kill_win(window):
    global sticky_win

    if not window:
        return

    if not sticky_win:
        return

    if window.name == sticky_win.name:
        sticky_win = None

# Keep Static windows on top
@hook.subscribe.client_focus
def _(_):
    for window in qtile.windows_map.values():
        if isinstance(window, base.Static):
            if hasattr(window, "cmd_bring_to_front"):
                window.cmd_bring_to_front()
