from libqtile.lazy import lazy
from libqtile.config import Key
from config import reload, MOD, MOD2, TERMINAL, BROWSER, FILE_EXPLORER, EDITOR, SCRIPTS_DIR, HOME

# My functions
reload("function")
import function

# My sticky window
reload("sticky")
from sticky import stick_win

key_bindings = [
    ### ESSENTIALS

    Key([MOD],              "Return",           lazy.spawn(TERMINAL),                                                                                                           'Launches my terminal'),
    Key([MOD],              "BackSpace",        lazy.window.kill(),                                                                                                             'Kill active window'),
    Key([MOD, "shift"],     "r",                lazy.restart(),                                                                                                                 'Restart Qtile'),
    Key([MOD, "shift"],     "BackSpace",        lazy.shutdown(),                                                                                                                'Shutdown Qtile'),
    Key([MOD, "control"],   "r",                lazy.spawn("reboot"),                                                                                                           'Restart computer'),
    Key([MOD, "control"],   "BackSpace",        lazy.spawn("shutdown now"),                                                                                                     'Shutdown computer'),

    # Qtile config  
    Key([MOD],              "q",                lazy.function(function.terminal_app, EDITOR, HOME + '/.config/qtile/config.py', windowName="Qtile config", sleep=0.1),      'Qtile config'),

    ### MY OWN KEYBINDINGS  

    # Switch keyboard layouts   
    Key([MOD2],             "space",            lazy.spawn(SCRIPTS_DIR + "changelayout"),                                                                                       'Switch keyboard layout'),

    # Launch Rofi   
    Key([MOD],              "space",            lazy.spawn(HOME + '/.config/rofi/bin/launcher_misc'),                                                                       'Run Launcher'),

    # Rofi twitch selector  
    Key([MOD, "shift"],     "t",                lazy.spawn(SCRIPTS_DIR + 'rofi-ttv'),                                                                                           'Run Twitch Launcher'),

    ### APPLICATIONS QUICK ACCESS   
    Key([MOD],              "b",                lazy.function(function.gotoapp_or_create, BROWSER, "Chromium"),                                                                 'Chromium'),
    Key([MOD],              "d",                lazy.function(function.gotoapp_or_create, 'discord'),                                                                           'Discord'),
    Key([MOD],              "i",                lazy.function(function.gotoapp_or_create, 'srain'),                                                                             'Srain'),
    Key([MOD],              "g",                lazy.group[""].toscreen(toggle=False),                                                                                         'Game'),
    Key([MOD],              "t",                lazy.function(function.gotoapp_or_create, 'telegram-desktop', 'Telegram'),                                                      'Telegram'),
    Key([MOD],              "s",                lazy.function(function.gotoapp_or_create, 'steam'),                                                                             'Steam'),
    Key([MOD],              "m",                lazy.function(function.terminal_app, 'spt', windowName="Spotify", sleep=0.1),                                                   'Spotify'),
    Key([MOD],              "e",                lazy.function(function.terminal_app, EDITOR, windowName="LunarVim", sleep=0.1),                                                 'LunarVim'),
    Key([MOD],              "c",                lazy.function(function.gotoapp_or_create, 'mailspring'),                                                                        'Mailspring'),
    Key([MOD],              "f",                lazy.function(function.terminal_app, FILE_EXPLORER, sleep=0.1),                                                                 'Ranger'),
    Key([MOD],              "n",                lazy.function(function.terminal_app, FILE_EXPLORER, '/mnt/hdd/nextcloud', windowName="Nextcloud", sleep=0.1),                   'Nextcloud'),

    ### ARCH INFO / CONTROLS    

    # BTOP  
    Key([MOD],              "p",                lazy.function(function.terminal_app, 'btop', windowName="Btop"),                                                                'Btop'),
    # Flameshot screenshot      
    Key([MOD, "shift"],     "s",                lazy.spawn(["flameshot", "gui"]),                                                                                               'Screenshot'),
    # Switch audio output       
    Key([MOD, "shift"],     "o",                lazy.spawn(SCRIPTS_DIR + 'switch-output'),                                                                                      'Switch audio output'),
    # Switch redshift       
    Key([MOD, "shift"],     "n",                lazy.function(function.switch_redshift),                                                                                        'Switch redshift'),
    # Random background     
    Key([MOD, "shift"],     "b",                lazy.function(function.random_background),                                                                                      'Random background'),
    # Update system     
    Key([MOD],              "u",                lazy.function(function.terminal_app, SCRIPTS_DIR + "up", windowName="System update"),                                           'System update'),
    # Update system (AUR)       
    Key([MOD, "shift"],     "u",                lazy.function(function.terminal_app, SCRIPTS_DIR + "up all", windowName="AUR system update"),                                   'AUR system update'),

    ### MONITORS    

    # Swap monitors 
    Key([MOD],              "y",                lazy.function(function.swap_screens),                                                                                           'Swap group between monitors'),
    # Switch focus of monitors  
    Key([MOD],              "period",           lazy.to_screen(0),                                                                                                              'Move focus to next monitor'),
    Key([MOD],              "comma",            lazy.to_screen(1),                                                                                                              'Move focus to prev monitor'),
    # Move windows to monitors  
    Key([MOD, "shift"],     "period",           lazy.window.toscreen(0), lazy.to_screen(0),                                                                                     'Move window and focus to next monitor'),
    Key([MOD, "shift"],     "comma",            lazy.window.toscreen(1), lazy.to_screen(1),                                                                                     'Move window and focus to prev monitor'),

    ### WINDOW CONTROLS 

    # Move through windows  
    Key([MOD],              "j",                lazy.layout.down(),                                                                                                             'Move focus down'),
    Key([MOD],              "k",                lazy.layout.up(),                                                                                                               'Move focus up'),
    Key([MOD],              "h",                lazy.layout.left(),                                                                                                             'Move focus left'),
    Key([MOD],              "l",                lazy.layout.right(),                                                                                                            'Move focus right'),

    # Move windows                                                                                              
    Key([MOD, "shift"],     "j",                lazy.layout.flip_down(),                                                                                                        'Move window down'),
    Key([MOD, "shift"],     "k",                lazy.layout.flip_up(),                                                                                                          'Move window up'),
    Key([MOD, "shift"],     "h",                lazy.layout.swap_column_left(),                                                                                                 'Move window left'),
    Key([MOD, "shift"],     "l",                lazy.layout.swap_column_right(),                                                                                                'Move window right'),

    # Resize windows                                                                                                
    Key([MOD, "control"],   "j",                lazy.layout.grow_down(),                                                                                                        'Move window down'),
    Key([MOD, "control"],   "k",                lazy.layout.grow_up(),                                                                                                          'Move window up'),
    Key([MOD, "control"],   "h",                lazy.layout.grow_left(),                                                                                                        'Move window left'),
    Key([MOD, "control"],   "l",                lazy.layout.grow_right(),                                                                                                       'Move window right'),

    # Stick windows                                                                                             
    Key([MOD],              "w",                lazy.function(stick_win),                                                                                                       'Stick win'),

    # Switch layouts                                                                                                
    Key([MOD],              "Tab",              lazy.next_layout(),                                                                                                             'Toggle through layouts'),
    # Normalize sizes                                                                                               
    Key([MOD, "control"],   "n",                lazy.layout.normalize(),                                                                                                        'Normalize window size ratios'),
    # Maximize / minimize                                                                                               
    Key([MOD, "shift"],     "m",                lazy.window.toggle_minimize(),                                                                                                  'Toggle window minimize'),
    # Full screen                                                                                               
    Key([MOD, "shift"],     "f",                lazy.window.toggle_fullscreen(),                                                                                                'toggle fullscreen'),

    ### HARDWARE

    # Volume keys
    Key([], "XF86AudioMute",                    lazy.spawn(SCRIPTS_DIR + "changevolume mute"),                                                                                  'Mute audio'),
    Key([], "XF86AudioLowerVolume",             lazy.spawn(SCRIPTS_DIR + "changevolume down"),                                                                                  'Volume down'),
    Key([], "XF86AudioRaiseVolume",             lazy.spawn(SCRIPTS_DIR + "changevolume up"),                                                                                    'Volume up'),
    # Discord volume keys
    Key([MOD], "XF86AudioLowerVolume",          lazy.spawn(SCRIPTS_DIR + 'changevolume-discord down'),                                                                          'Discord volume down'),
    Key([MOD], "XF86AudioRaiseVolume",          lazy.spawn(SCRIPTS_DIR + 'changevolume-discord up'),                                                                            'Discord volume up'),
    # Spotify volume keys
    Key(["control"], "XF86AudioLowerVolume",    lazy.spawn(SCRIPTS_DIR + 'changevolume-spotify down'),                                                                          'Spotify volume down'),
    Key(["control"], "XF86AudioRaiseVolume",    lazy.spawn(SCRIPTS_DIR + 'changevolume-spotify up'),                                                                            'Spotify volume up'),

    # Media keys (Spotify)
    Key([], "XF86AudioPlay",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"),           'Audio play'),
    Key([], "XF86AudioNext",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"),                'Audio next'),
    Key([], "XF86AudioPrev",                    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotifyd /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"),            'Audio previous')
]