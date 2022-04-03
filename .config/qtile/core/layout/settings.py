from settings import WINDOW_MARGIN

#################
### CONSTANTS ###
#################

BORDER_FOCUS_COLORS = [
    'd7de59',   # Focused window
    '7b7b7b',   # Unfocused window
]

#####################
### LAYOUT THEMES ###
#####################

# Columns
columns_theme = {
    "border_width": 1,
    "margin": [WINDOW_MARGIN, WINDOW_MARGIN, 0, 0],
    # "margin_on_single": [0, 0, 0, 0],
    "border_on_single": True,
    "border_focus": BORDER_FOCUS_COLORS[0],
    "border_normal": BORDER_FOCUS_COLORS[1],
    "grow_amount": 5
}

# Stack
stack_theme = {
    "border_width": 1,
    "border_focus": BORDER_FOCUS_COLORS[0],
    "margin": [WINDOW_MARGIN, WINDOW_MARGIN, 0, 0]
}
