from settings import SCREEN_PRIMARY_WIDTH
from bars.minimal.body import build_screens

WIDGET_FONT                 = "Iosevka Fixed SS18"
WIDGET_FONT_SIZE            = int(SCREEN_PRIMARY_WIDTH / 120)
WIDGET_ICON_FONT            = "FontAwesome"
WIDGET_ICON_FONT_SIZE       = 20
WIGET_PADDING_SIZE          = int(SCREEN_PRIMARY_WIDTH / 960)

COLORS = [
    '1b1c26',   # Icon, Bar color 1, widget font
    'd7de59',   # Bar color 2, focused window border line
    '7b7b7b',   # Bar color 3, unfocused window border line
]

widget_defaults = dict(
    font                    = WIDGET_FONT,
    fontsize                = WIDGET_FONT_SIZE,
    padding                 = WIGET_PADDING_SIZE,
    background              = COLORS[0],
    foreground              = COLORS[1]
)

extension_defaults = widget_defaults.copy()

ICON_FONT_CONFIG = {
    'font': WIDGET_ICON_FONT,
    'fontsize': WIDGET_ICON_FONT_SIZE
}

screens = build_screens(COLORS, ICON_FONT_CONFIG)