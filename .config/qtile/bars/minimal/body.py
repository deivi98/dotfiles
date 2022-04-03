import sys
import os

from libqtile.bar import Bar, Gap
from libqtile.config import Screen
from libqtile import widget
from libqtile.log_utils import logger
from settings import WINDOW_MARGIN, SCREEN_PRIMARY_WIDTH

from bars.widgets import *

#################
### CONSTANTS ###
#################

BAR_MARGIN_TOP              = 15
BAR_MARGIN_RIGHT            = 15
BAR_MARGIN_DOWN             = 0
BAR_MARGIN_LEFT             = 15

BAR_PRIMARY_HEIGHT          = int(SCREEN_PRIMARY_WIDTH / 70)
BAR_SECONDARY_HEIGHT        = BAR_PRIMARY_HEIGHT

#######################
### PRIMARY SCREEN ####
#######################

def _build_primary_widgets(COLORS, ICON_FONT_CONFIG):
    return [
        padding(ICON_FONT_CONFIG),
        logo({'fontsize': 40}),
        padding(ICON_FONT_CONFIG),
        windowName(),

        spacer(),
        # text("", ICON_FONT_CONFIG),
        # spotify(),
        groupBox({
            'hide_unused':                          False,
            'rounded':                              True,
            'highlight_method':                     'line',     # Selected type of highlight
            'block_highlight_text_color':           COLORS[1],
            'this_current_screen_border':           COLORS[1],  # Highlight color of selected (in this screen)
            'other_current_screen_border':          COLORS[0],  # Highlight color of selected (in other screen)
            'this_screen_border':                   COLORS[1],  # Highlight color of other group selected (in other screen)
            'other_screen_border':                  COLORS[0],  # Highlight color of other group selected (in this screen)
            'highlight_color':                      COLORS[0],  # Highlight background of selected
            'active':                               COLORS[2],  # Groups with at least one window
            'inactive':                             COLORS[2],  # Groups with no windows
            'fontsize':                             33,
            'padding_x':                            5
        }),
        spacer(),

        systray(ICON_FONT_CONFIG),
        padding(ICON_FONT_CONFIG),
        text(" ", ICON_FONT_CONFIG),
        *currentLayout(),
        padding(ICON_FONT_CONFIG),
        volumeSpotifyIcon(ICON_FONT_CONFIG),
        volumeSpotify(),
        padding(ICON_FONT_CONFIG),
        volumeDiscordIcon(ICON_FONT_CONFIG),
        volumeDiscord(),
        padding(ICON_FONT_CONFIG),
        volumeIcon(ICON_FONT_CONFIG),
        volume(),
        padding(ICON_FONT_CONFIG),
        text(" ", ICON_FONT_CONFIG),
        shortClock(),
        padding(ICON_FONT_CONFIG)
    ]

#########################
### SECONDARY SCREEN ####
#########################

def _build_secondary_widgets(COLORS, ICON_FONT_CONFIG):
    return [
        padding(ICON_FONT_CONFIG),
        logo({'fontsize': 40}),
        padding(ICON_FONT_CONFIG),
        windowName(),
        
        spacer(),
        groupBox({
            'hide_unused':                          False,
            'rounded':                              True,
            'highlight_method':                     'line',     # Selected type of highlight
            'block_highlight_text_color':           COLORS[1],
            'this_current_screen_border':           COLORS[1],  # Highlight color of selected (in this screen)
            'other_current_screen_border':          COLORS[0],  # Highlight color of selected (in other screen)
            'this_screen_border':                   COLORS[1],  # Highlight color of other group selected (in other screen)
            'other_screen_border':                  COLORS[0],  # Highlight color of other group selected (in this screen)
            'highlight_color':                      COLORS[0],  # Highlight background of selected
            'active':                               COLORS[2],  # Groups with at least one window
            'inactive':                             COLORS[2],  # Groups with no windows
            'fontsize':                             33,
            'padding_x':                            5
        }),
        padding(ICON_FONT_CONFIG),
        text(" ", ICON_FONT_CONFIG),
        *currentLayout(),
        spacer(),

        checkUpdates(ICON_FONT_CONFIG),
        padding(ICON_FONT_CONFIG),
        text("pkgs"),
        text(" ", ICON_FONT_CONFIG),
        numPkgs(),
        text(" ", ICON_FONT_CONFIG),
        numInstalledPkgs(),
        text(" ", ICON_FONT_CONFIG),
        numYayPkgs(),
        
        spacer(),

        text(" ", ICON_FONT_CONFIG),
        clock(),
        padding(ICON_FONT_CONFIG)
    ]

def build_screens(COLORS, ICON_FONT_CONFIG):

    primaryWidgets = _build_primary_widgets(COLORS, ICON_FONT_CONFIG)
    secondaryWidgets = _build_secondary_widgets(COLORS, ICON_FONT_CONFIG)

    return [
        Screen(
            top = Bar(widgets = primaryWidgets, opacity = 1.0, margin = [BAR_MARGIN_TOP, BAR_MARGIN_RIGHT, BAR_MARGIN_DOWN, BAR_MARGIN_LEFT], size = BAR_PRIMARY_HEIGHT),
            bottom = Gap(WINDOW_MARGIN),
            left = Gap(WINDOW_MARGIN)
        ),
        Screen(
            top = Bar(widgets = secondaryWidgets, opacity = 1.0, margin = [BAR_MARGIN_TOP, BAR_MARGIN_RIGHT, BAR_MARGIN_DOWN, BAR_MARGIN_LEFT], size = BAR_SECONDARY_HEIGHT),
            bottom = Gap(WINDOW_MARGIN),
            left = Gap(WINDOW_MARGIN)
        )
    ]
