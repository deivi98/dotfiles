from libqtile import layout
from colors import _colors

# Layout default settings
layout_theme = {
    "border_width": 4,
    "margin": 12,
    "border_focus": _colors[3],
    "border_normal": _colors[7]
}

# Qtile active layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.Stack(num_stacks=1, name="tabs", **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
