from libqtile import layout

## LAYOUT THEMES
from core.layout.settings import columns_theme, stack_theme

# Qtile active layouts
layouts = [
    layout.Columns(**columns_theme),
    layout.Stack(num_stacks = 1, **stack_theme)
]