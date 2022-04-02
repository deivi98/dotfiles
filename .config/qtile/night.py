from libqtile.bar import Bar, Gap
from libqtile.config import Screen
from libqtile import widget
from libqtile.log_utils import logger

SCREEN_PRIMARY_WIDTH = 2560 # FUERA
SCREEN_PRIMARY_HEIGHT = 1440 # FUERA
SCREEN_SECONDARY_WIDTH = 1920 # FUERA
SCREEN_SECONDARY_HEIGHT = 1080 # FUERA

WINDOW_MARGIN = 15 # FUERA

BAR_MARGIN_TOP = 15
BAR_MARGIN_RIGHT = 15
BAR_MARGIN_DOWN = 0
BAR_MARGIN_LEFT = 15
BAR_PRIMARY_HEIGHT = SCREEN_PRIMARY_WIDTH / 80
BAR_SECONDARY_HEIGHT = SCREEN_SECONDARY_WIDTH / 80

BAR_COLORS = [
    '1b1c26',   # Icon, Bar color 1, widget font
    'd7de59',   # Bar color 2, focused window border line
    '7b7b7b',   # Bar color 3, unfocused window border line
]

widgets = [
    widget.WindowName(
        background=BAR_COLORS[0],
        foreground=BAR_COLORS[1],
        format='{state}{name}'
    ),
    widget.GroupBox(
        background=BAR_COLORS[2],
        this_current_screen_border = BAR_COLORS[1],
        this_screen_border = BAR_COLORS[1],
        other_current_screen_border=BAR_COLORS[2],
        other_screen_border=BAR_COLORS[2],
        hide_unused = False,
        rounded = True,
        highlight_method = 'line',
        highlight_color=BAR_COLORS[2],
        font="FontAwesome",
        active=BAR_COLORS[0],
        inactive=BAR_COLORS[0],
    )
]

def _build_primary_bar():
    return Bar(widgets=widgets, opacity=1.0, margin=[BAR_MARGIN_TOP, BAR_MARGIN_RIGHT, BAR_MARGIN_DOWN, BAR_MARGIN_LEFT], size = BAR_PRIMARY_HEIGHT)

def _build_secondary_bar():
    return Bar(widgets=widgets, opacity=1.0, margin=[BAR_MARGIN_TOP, BAR_MARGIN_RIGHT, BAR_MARGIN_DOWN, BAR_MARGIN_LEFT], size = BAR_SECONDARY_HEIGHT)

def build_screens():
    return [
        Screen(
            top=_build_primary_bar(),
            bottom=Gap(WINDOW_MARGIN),
            left=Gap(WINDOW_MARGIN)
        ),
        Screen(
            top=_build_secondary_bar(),
            bottom=Gap(WINDOW_MARGIN),
            left=Gap(WINDOW_MARGIN)
        )
    ]
