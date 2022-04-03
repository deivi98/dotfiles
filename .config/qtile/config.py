# Import core functionality
from core.hooks import *
from core.keybindings import *
from core.layout.layouts import *
from core.layout.floating import *
from core.groups import *

# Import sticky window utils
from utils.sticky import *

# Import bar
from bars.minimal.themes.night import *

# from bar import init_screen, widget_default_values

# screens = [
# 	init_screen(),
# 	init_screen(secondary=True)
# ]

# # Default widget and extension settings
# widget_defaults = widget_default_values
# extension_defaults = widget_defaults.copy()

# Other Qtile config variables
dgroups_key_binder              = None
dgroups_app_rules               = []
follow_mouse_focus              = True
bring_front_click               = "floating_only"
cursor_warp                     = False
auto_fullscreen                 = True
focus_on_window_activation      = "smart"
reconfigure_screens             = True
auto_minimize                   = True
wmname                          = "Qtile" # X11 window manager name
