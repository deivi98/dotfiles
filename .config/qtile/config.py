import importlib
import sys
import os

#################
### CONSTANTS ###
#################

# General
MOD                     = "mod1"
MOD2                    = "mod4"
TERMINAL                = "alacritty"                                       # My terminal of choice
BROWSER                 = "chromium"                                        # My browser of choice
FILE_EXPLORER           = "ranger"                                          # My file explorer of choice
EDITOR                  = "lvim"                                            # My editor
HOME                    = os.path.expanduser('~')                           # My home
SCRIPTS_DIR             = HOME + "/.config/scripts/"                        # My scripts directory

#####################
### GENERAL UTILS ###
#####################

### Config imports
def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])

### Import my hooks
reload("hooks")
import hooks

### Import my sticky window utils
reload("sticky")
import sticky

###################
### KEYBINDINGS ###
###################

reload("keybindings")
from keybindings import key_bindings
keys = key_bindings

###############
### LAYOUTS ###
###############

reload("layouts")
from layouts import layout_list
layouts = layout_list

# Floating layout
reload("floating")
from floating import layout_float, mouse_controls
floating_layout = layout_float
mouse = mouse_controls

##################
### WORKSPACES ###
##################

reload("groups")
from groups import workspaces, add_workspace_keybindings
groups = workspaces
keys = add_workspace_keybindings(keys)

###########
### BAR ###
###########

reload("bar")
from bar import init_screen, widget_default_values

screens = [
	init_screen(),
	init_screen(secondary=True)
]

# Default widget and extension settings
widget_defaults = widget_default_values
extension_defaults = widget_defaults.copy()

#############################
### OTHER QTILE VARIABLES ###
#############################

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
