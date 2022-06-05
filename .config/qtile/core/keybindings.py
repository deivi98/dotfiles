from libqtile.lazy import lazy
from libqtile.config import Key
from settings import SCRIPTS_DIR, HOME, TERMINAL, MOD, EDITOR, MOD2, BROWSER, FILE_EXPLORER

# My functions
import utils.functions as functions

# My sticky window
from utils.sticky import stick_win

keys = [
    ### ESSENTIALS

    Key([MOD],              "Return",           lazy.spawn(TERMINAL),                                                                                                           desc='Launches my terminal'),
    Key([MOD],              "BackSpace",        lazy.window.kill(),                                                                                                             desc='Kill active window'),
    Key([MOD, "shift"],     "r",                lazy.restart(),                                                                                                                 desc='Restart Qtile'),
    Key([MOD, "shift"],     "BackSpace",        lazy.shutdown(),                                                                                                                desc='Shutdown Qtile'),
    Key([MOD, "control"],   "r",                lazy.spawn("reboot"),                                                                                                           desc='Restart computer'),
    Key([MOD, "control"],   "BackSpace",        lazy.spawn("shutdown now"),                                                                                                     desc='Shutdown computer'),

    # Qtile config  
    Key([MOD],              "q",                lazy.function(functions.terminal_app, EDITOR, HOME + '/.config/qtile/config.py', windowName="Qtile config", sleep=0.1),         desc='Qtile config'),

    ### MY OWN KEYBINDINGS  

    # Switch keyboard layouts   
    Key([MOD2],             "space",            lazy.spawn(SCRIPTS_DIR + "changelayout"),                                                                                       desc='Switch keyboard layout'),

    # Launch Rofi   
    Key([MOD],              "space",            lazy.spawn(HOME + '/.config/rofi/bin/launcher_misc'),                                                                           desc='Run Launcher'),

    # Rofi twitch selector  
    Key([MOD, "shift"],     "t",                lazy.spawn(SCRIPTS_DIR + 'rofi-ttv'),                                                                                           desc='Run Twitch Launcher'),

    ### APPLICATIONS QUICK ACCESS   
    Key([MOD],              "b",                lazy.function(functions.gotoapp_or_create, BROWSER, "Chromium"),                                                                desc='Chromium'),
    Key([MOD],              "d",                lazy.function(functions.gotoapp_or_create, 'discord'),                                                                          desc='Discord'),
    Key([MOD],              "i",                lazy.function(functions.gotoapp_or_create, 'srain'),                                                                            desc='Srain'),
    Key([MOD],              "g",                lazy.to_screen(0), lazy.group["5"].toscreen(toggle=False),                                                                      desc='Game'),
    Key([MOD],              "t",                lazy.function(functions.gotoapp_or_create, 'telegram-desktop', 'Telegram'),                                                     desc='Telegram'),
    Key([MOD],              "s",                lazy.function(functions.gotoapp_or_create, 'steam'),                                                                            desc='Steam'),
    Key([MOD],              "m",                lazy.function(functions.terminal_app, 'spt', windowName="Spotify", sleep=0.1),                                                  desc='Spotify'),
    Key([MOD],              "e",                lazy.function(functions.terminal_app, EDITOR, windowName="LunarVim", sleep=0.1),                                                desc='LunarVim'),
    Key([MOD],              "c",                lazy.function(functions.gotoapp_or_create, 'mailspring'),                                                                       desc='Mailspring'),
    Key([MOD],              "f",                lazy.function(functions.terminal_app, FILE_EXPLORER, sleep=0.1),                                                                desc='Ranger'),
    Key([MOD],              "n",                lazy.function(functions.terminal_app, FILE_EXPLORER, '/home/david/cloud', windowName="Nextcloud", sleep=0.1),                   desc='Nextcloud'),

    ### ARCH INFO / CONTROLS    

    # BTOP  
    Key([MOD],              "p",                lazy.function(functions.terminal_app, 'btop', windowName="Btop"),                                                               desc='Btop'),
    # Flameshot screenshot      
    Key([MOD, "shift"],     "s",                lazy.spawn(["flameshot", "gui"]),                                                                                               desc='Screenshot'),
    # Switch audio output       
    Key([MOD, "shift"],     "o",                lazy.spawn(SCRIPTS_DIR + 'switch-output'),                                                                                      desc='Switch audio output'),
    # Switch redshift       
    Key([MOD, "shift"],     "n",                lazy.function(functions.switch_redshift),                                                                                       desc='Switch redshift'),
    # Random background     
    Key([MOD, "shift"],     "b",                lazy.function(functions.random_background),                                                                                     desc='Random background'),
    # Update system     
    Key([MOD],              "u",                lazy.function(functions.terminal_app, SCRIPTS_DIR + "up", windowName="System update"),                                          desc='System update'),
    # Update system (AUR)       
    Key([MOD, "shift"],     "u",                lazy.function(functions.terminal_app, SCRIPTS_DIR + "up all", windowName="AUR system update"),                                  desc='AUR system update'),

    ### MONITORS    

    # Swap monitors 
    Key([MOD],              "y",                lazy.function(functions.swap_screens),                                                                                          desc='Swap group between monitors'),
    # Switch focus of monitors  
    Key([MOD],              "period",           lazy.to_screen(0),                                                                                                              desc='Move focus to next monitor'),
    Key([MOD],              "comma",            lazy.to_screen(1),                                                                                                              desc='Move focus to prev monitor'),
    # Move windows to monitors  
    Key([MOD, "shift"],     "period",           lazy.window.toscreen(0), lazy.to_screen(0),                                                                                     desc='Move window and focus to next monitor'),
    Key([MOD, "shift"],     "comma",            lazy.window.toscreen(1), lazy.to_screen(1),                                                                                     desc='Move window and focus to prev monitor'),

    ### WINDOW CONTROLS 

    # Move through windows  
    Key([MOD],              "j",                lazy.layout.down(),                                                                                                             desc='Move focus down'),
    Key([MOD],              "k",                lazy.layout.up(),                                                                                                               desc='Move focus up'),
    Key([MOD],              "h",                lazy.layout.left(),                                                                                                             desc='Move focus left'),
    Key([MOD],              "l",                lazy.layout.right(),                                                                                                            desc='Move focus right'),

    # Move windows                                                                                              
    Key([MOD, "shift"],     "j",                lazy.layout.flip_down(),                                                                                                        desc='Move window down'),
    Key([MOD, "shift"],     "k",                lazy.layout.flip_up(),                                                                                                          desc='Move window up'),
    Key([MOD, "shift"],     "h",                lazy.layout.swap_column_left(),                                                                                                 desc='Move window left'),
    Key([MOD, "shift"],     "l",                lazy.layout.swap_column_right(),                                                                                                desc='Move window right'),

    # Resize windows                                                                                                
    Key([MOD, "control"],   "j",                lazy.layout.grow_down(),                                                                                                        desc='Move window down'),
    Key([MOD, "control"],   "k",                lazy.layout.grow_up(),                                                                                                          desc='Move window up'),
    Key([MOD, "control"],   "h",                lazy.layout.grow_left(),                                                                                                        desc='Move window left'),
    Key([MOD, "control"],   "l",                lazy.layout.grow_right(),                                                                                                       desc='Move window right'),

    # Stick windows                                                                                             
    Key([MOD],              "w",                lazy.function(stick_win),                                                                                                       desc='Stick win'),

    # Switch layouts                                                                                                
    Key([MOD],              "Tab",              lazy.next_layout(),                                                                                                             desc='Toggle through layouts'),
    # Normalize sizes                                                                                               
    Key([MOD, "control"],   "n",                lazy.layout.normalize(),                                                                                                        desc='Normalize window size ratios'),
    # Maximize / minimize                                                                                               
    Key([MOD, "shift"],     "m",                lazy.window.toggle_minimize(),                                                                                                  desc='Toggle window minimize'),
    # Full screen                                                                                               
    Key([MOD, "shift"],     "f",                lazy.window.toggle_fullscreen(),                                                                                                desc='toggle fullscreen'),

    ### HARDWARE

    # Volume keys
    Key([], "XF86AudioMute",                    lazy.spawn(SCRIPTS_DIR + "changevolume mute"),                                                                                  desc='Mute audio'),
    Key([], "XF86AudioLowerVolume",             lazy.spawn(SCRIPTS_DIR + "changevolume down"),                                                                                  desc='Volume down'),
    Key([], "XF86AudioRaiseVolume",             lazy.spawn(SCRIPTS_DIR + "changevolume up"),                                                                                    desc='Volume up'),
    # Discord volume keys
    Key([MOD], "XF86AudioLowerVolume",          lazy.spawn(SCRIPTS_DIR + 'changevolume-discord down'),                                                                          desc='Discord volume down'),
    Key([MOD], "XF86AudioRaiseVolume",          lazy.spawn(SCRIPTS_DIR + 'changevolume-discord up'),                                                                            desc='Discord volume up'),
    # Spotify volume keys
    Key(["control"], "XF86AudioLowerVolume",    lazy.spawn(SCRIPTS_DIR + 'changevolume-spotify down'),                                                                          desc='Spotify volume down'),
    Key(["control"], "XF86AudioRaiseVolume",    lazy.spawn(SCRIPTS_DIR + 'changevolume-spotify up'),                                                                            desc='Spotify volume up'),

    # Media keys (Spotify)
    Key([], "XF86AudioPlay",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"),           desc='Audio play'),
    Key([], "XF86AudioNext",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"),                desc='Audio next'),
    Key([], "XF86AudioPrev",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"),            desc='Audio previous')
]
