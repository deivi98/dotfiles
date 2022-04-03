import os

################
### SETTINGS ###
################

# Qtile
MOD                         = "mod1"                                            # ALT
MOD2                        = "mod4"                                            # WIN KEY

# Default programs
TERMINAL                    = "alacritty"                                       # My terminal of choice
BROWSER                     = "chromium"                                        # My browser of choice
FILE_EXPLORER               = "ranger"                                          # My file explorer of choice
EDITOR                      = "lvim"                                            # My editor

# Default paths
HOME                        = os.path.expanduser('~')                           # My home
SCRIPTS_DIR                 = HOME + "/.config/scripts/"                        # My scripts directory

# Layout
WINDOW_MARGIN = 15

# Screen
SCREEN_PRIMARY_WIDTH        = 2560
SCREEN_PRIMARY_HEIGHT       = 1440
SCREEN_SECONDARY_WIDTH      = 1920
SCREEN_SECONDARY_HEIGHT     = 1080