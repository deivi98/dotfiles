from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from libqtile import hook, qtile

from config import MOD

# Set initial groups
@hook.subscribe.startup
def _():
    if len(qtile.screens) > 1:
        qtile.groups_map[''].cmd_toscreen(0, toggle=False)
        qtile.groups_map[''].cmd_toscreen(1, toggle=False)

group_names = [
    ("", {'layout': 'columns', 'matches': [    # Browser
        Match(wm_class='chromium'),
        Match(wm_class='firefox'),
        Match(wm_class='qutebrowser')
    ]}),
    ("", {'layout': 'columns', 'matches': [    # Files
        Match(wm_class='pcmanfm'),
        Match(title='Nextcloud'),
        Match(title='Ranger'),
        Match(title='Htop memory usage'),
        Match(title='Htop cpu usage')
    ]}),
    ("", {'layout': 'columns', 'matches': [    # Editor
        Match(wm_class='code'),
        Match(title='LunarVim'),
        Match(title='Qtile config')
    ]}),
    ("", {'layout': 'tabs', 'matches': [       # Discord
        Match(wm_class='discord'),
        Match(wm_class='srain'),
        Match(wm_class='telegram-desktop'),
        Match(title='Spotify'),
        Match(wm_class='Mailspring')
    ]}),
    ("", {'layout': 'tabs', 'matches': [       # Gaming
        Match(title='Steam'),
        Match(wm_class='csgo_linux64'),
        Match(title='Brawlhalla'),
        Match(title='Rocket League'),
        Match(wm_class='minecraft-launcher')
    ]})
]

# Qtile groups
workspaces = [Group(name, **kwargs) for name, kwargs in group_names]

def add_workspace_keybindings(keys):
    # Adds keybindings for each group
    for i, (name, kwargs) in enumerate(group_names, 1):
        # Switch to another group
        keys.append(Key([MOD], str(i), lazy.to_screen(0), lazy.group[name].toscreen(toggle=False)))
        # Send current window to another group
        keys.append(Key([MOD, "shift"], str(i), lazy.window.togroup(name)))

    return keys
