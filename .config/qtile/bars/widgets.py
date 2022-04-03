from libqtile import qtile, widget
from settings import HOME

# My functions
import utils.functions as functions

#######################
### DEFAULT WIDGETS ###
#######################

def logo(args = {}):
    return widget.TextBox(
        **args,
        text                = "",
        mouse_callbacks     = { 'Button1': lambda: qtile.cmd_spawn(HOME + '/.config/rofi/bin/launcher_misc') }
    )

def groupBox(args = {}):
    return widget.GroupBox(**args)

def windowName(args = {}):
    return widget.WindowName(
        **args,
        format      = '{state}{name}'
    )

def currentLayout(args = {}):
    return [
        # widget.CurrentLayoutIcon(**args),
        text("", args),
        widget.CurrentLayout(**args),
        widget.WindowCount(
            **args,
            text_format = "[{num}]",
            show_zero = True
        )
    ]

def systray(args = {}):
    return widget.Systray(**args)

def clock(args = {}):
    return widget.Clock(format = '%A, %b %-d, %H:%M')

def shortClock(args = {}):
    return widget.Clock(format = '%H:%M')

def checkUpdates(args = {}):
    return widget.CheckUpdates(
            update_interval             = 60,
            distro                      = "Arch_checkupdates",
            display_format              = " {updates}",
            no_update_string            = "",
            colour_no_updates           = "1bc700",
            colour_have_updates         = "d60000",
            mouse_callbacks             = { 'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e ' + SCRIPTS_DIR + 'up') }
    )

def text(text, args = {}):
    return widget.TextBox(**args, text=text)

###############
### SCRIPTS ###
###############

def volume(args = {}, script = 'get-volume'):
    return widget.GenPollText(
        **args,
        func                    = functions.exec_script(script),
        update_interval         = 0.2,
        mouse_callbacks         = { 'Button1': lambda: qtile.cmd_spawn('pavucontrol') }
    )

def volumeDiscord(args = {}):
    return volume(args, 'get-discord-volume')

def volumeSpotify(args = {}):
    return volume(args, 'get-spotify-volume')

def numPkgs(args = {}, script = 'num-pkgs'):
    return widget.GenPollText(
        **args,
        update_interval         = 60,
        func                    = functions.exec_script(script),
        mouse_callbacks         = { 'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e pacman -Q' )}
    )

def numInstalledPkgs(args = {}):
    return numPkgs(args, 'num-installed-pkgs')

def numYayPkgs(args = {}):
    return numPkgs(args, 'num-yay-pkgs')

##################
### SEPARATORS ###
##################

def padding(args = {}):
    return widget.TextBox(
        **args,
        padding = 1,
        text = ' '
    )

def spacer(args = {}):
    return widget.Spacer(**args)