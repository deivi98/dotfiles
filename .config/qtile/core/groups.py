from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from libqtile import hook, qtile

from settings import MOD
from core.keybindings import keys

# Set initial groups
@hook.subscribe.startup
def _():
    if len(qtile.screens) > 1:
        qtile.groups_map['1'].cmd_toscreen(0, toggle=False)
        qtile.groups_map['4'].cmd_toscreen(1, toggle=False)


# numbers = [i for i in range(5)]
circles = ['●'] * 5

label = circles

group_names = [
    ("1", {'label': circles[0], 'layout': 'columns', 'matches': [    # Browser
        Match(wm_class='chromium'),
        Match(wm_class='firefox'),
        Match(wm_class='qutebrowser')
    ]}),
    ("2", {'label': circles[1], 'layout': 'columns', 'matches': [    # Files
        Match(wm_class='pcmanfm'),
        Match(title='Nextcloud'),
        Match(title='Ranger'),
        Match(title='Htop memory usage'),
        Match(title='Htop cpu usage')
    ]}),
    ("3", {'label': circles[2], 'layout': 'columns', 'matches': [    # Editor
        Match(wm_class='code'),
        Match(title='LunarVim'),
        Match(title='Qtile config')
    ]}),
    ("4", {'label': circles[3], 'layout': 'stack', 'matches': [       # Discord
        Match(wm_class='discord'),
        Match(wm_class='srain'),
        Match(wm_class='telegram-desktop'),
        Match(title='Spotify'),
        Match(wm_class='Mailspring')
    ]}),
    ("5", {'label': circles[4], 'layout': 'stack', 'matches': [       # Gaming
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
    keys.append(Key([MOD], str(i), lazy.to_screen(0), lazy.group[name].toscreen(toggle=False)))
    # Send current window to another group
    keys.append(Key([MOD, "shift"], str(i), lazy.window.togroup(name)))
