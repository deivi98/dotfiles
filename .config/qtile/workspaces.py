from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from keybindings import mod, keys

# Group names (icons taken from https://fontawesome.com/v4.7/cheatsheet/)
group_names = [
    ("", {'layout': 'tabs', 'matches': [Match(wm_class='firefox')]}),                   # Firefox
    ("", {'layout': 'monadtall'}),                                                     # Terminal
    ("", {'layout': 'monadtall', 'matches': [Match(wm_class='code')]}),                # Code
    ("", {'layout': 'tabs', 'matches': [                                               # Game
        Match(title='Counter-Strike'),
        Match(title='Brawlhalla'),
        Match(title='Rocket League')
    ]}),
    ("", {'layout': 'tabs', 'matches': [Match(title='Steam')]}),                       # Steam
    ("", {'layout': 'monadtall', 'matches': [Match(wm_class='discord')]}),             # Discord
    ("", {'layout': 'monadtall', 'matches': [Match(wm_class='telegram-desktop')]}),    # Telegram
    ("", {'layout': 'monadtall', 'matches': [Match(wm_class='mailspring')]}),          # Mail client
    ("", {'layout': 'monadtall', 'matches': [Match(title='Spotify')]})                 # Spotify
]

# Qtile groups
groups = [Group(name, **kwargs) for name, kwargs in group_names]

# Adds keybindings for each group
for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.to_screen(0), lazy.group[name].toscreen(toggle=False)))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))
