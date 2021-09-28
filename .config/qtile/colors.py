_colors = [
    '1b1c26',   # Icon, Bar color 1, widget font
    'ffffff',   # Unused
    'ffffff',   # Unused
    'e6901e',   # Bar color 2, unfocused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
    'ffffff',   # Unused
    'a8a885',   # Bar color 3, focused window border line
    'ffffff',   # Unused
    'ffffff',   # Unused
]

map_color = lambda c: [f'#{c}', f'#{c}']
colors = tuple(map(map_color, _colors))
