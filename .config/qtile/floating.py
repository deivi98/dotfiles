from libqtile import layout
from libqtile.lazy import lazy
from libqtile.config import Match, Drag, Click
from config import MOD

layout_float = layout.Floating(float_rules = [
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),         # gitk
    Match(wm_class='makebranch'),           # gitk
    Match(wm_class='maketag'),              # gitk
    Match(wm_class='ssh-askpass'),          # ssh-askpass
    Match(title='branchdialog'),            # gitk
    Match(title='pinentry'),                # GPG key password entry
])

mouse_controls = [
    Drag([MOD],             "Button1",          lazy.window.set_position_floating(),    start=lazy.window.get_position()),
    Drag([MOD],             "Button3",          lazy.window.set_size_floating(),        start=lazy.window.get_size()),
    Click([MOD],            "Button2",          lazy.window.bring_to_front())
]