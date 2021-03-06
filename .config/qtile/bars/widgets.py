from libqtile import qtile, widget
from settings import HOME, TERMINAL, SCRIPTS_DIR

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
            **args,
            update_interval             = 60,
            distro                      = "Arch_checkupdates",
            display_format              = " {updates}",
            no_update_string            = " up-to-date",
            colour_no_updates           = "1bc700",
            colour_have_updates         = "d60000",
            mouse_callbacks             = { 'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e ' + SCRIPTS_DIR + 'up') }
    )

# It does NOT work
def spotify(args = {}):
    return widget.Mpris2(
        **args,
        name = 'spotifyd',
        objname = 'org.mpris.MediaPlayer2.spotify',
        display_metadata = ['xesam:title'],
        max_chars = 41,
        padding = 0,
        scroll_chars = None,
        scroll_interval = 0.5,
        stop_pause_text = 'Paused'
    )

def text(text, args = {}):
    return widget.TextBox(**args, text=text)

###############
### SCRIPTS ###
###############

def volumeIcon(args = {}, script = 'get-volume-icon'):
    return widget.GenPollText(
        **args,
        func                    = functions.exec_script(script),
        update_interval         = 0.2,
        mouse_callbacks         = { 'Button1': lambda: qtile.cmd_spawn('pavucontrol') }
    )

def volume(args = {}, script = 'get-volume'):
    return widget.GenPollText(
        **args,
        func                    = functions.exec_script(script),
        update_interval         = 0.2,
        mouse_callbacks         = { 'Button1': lambda: qtile.cmd_spawn('pavucontrol') }
    )

def volumeDiscordIcon(args = {}):
    return volumeIcon(args, 'get-discord-volume-icon')

def volumeDiscord(args = {}):
    return volume(args, 'get-discord-volume')

def volumeSpotifyIcon(args = {}):
    return volumeIcon(args, 'get-spotify-volume-icon')

def volumeSpotify(args = {}):
    return volume(args, 'get-spotify-volume')

def headsetBatteryIcon(args = {}, script = 'get-headset-battery-icon'):
    return widget.GenPollText(
        **args,
        func                    = functions.exec_script(script),
        update_interval         = 10,
    )

def headsetBattery(args = {}, script = 'get-headset-battery'):
    return widget.GenPollText(
        **args,
        func                    = functions.exec_script(script),
        update_interval         = 10,
    )

def numPkgs(args = {}, script = 'num-pkgs', cmd = 'pacman -Q'):
    return widget.GenPollText(
        **args,
        update_interval         = 60,
        func                    = functions.exec_script(script),
        mouse_callbacks         = { 'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e ' + cmd)}
    )

def numInstalledPkgs(args = {}):
    return numPkgs(args, 'num-installed-pkgs', 'pacman -Qqetn')

def numYayPkgs(args = {}):
    return numPkgs(args, 'num-yay-pkgs', 'pacman -Qqetm')

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
