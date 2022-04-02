from libqtile import layout
from config import reload

## LAYOUT THEMES
reload("themes")
from themes import columns_theme, stack_theme

# Qtile active layouts
layout_list = [
    layout.Columns(**columns_theme),
    layout.Stack(num_stacks = 1, name = "tabs", **stack_theme)
]