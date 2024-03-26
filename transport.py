# decompyle3 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\transport.py
# Compiled at: 2024-01-31 17:08:32
# Size of source mod 2**32: 465 bytes
from __future__ import absolute_import, print_function, unicode_literals
from novation.transport import TransportComponent as TransportComponentBase
from ableton.v2.control_surface.control import ButtonControl, ToggleButtonControl


class TransportComponent(TransportComponentBase):
    alt_stop_button = ButtonControl()
    play_button = ToggleButtonControl(toggled_color="Transport.PlayOn",
                                      untoggled_color="Transport.PlayOff")
    @play_button.toggled
    def _on_play_button_toggled(self, is_toggled, _):
        self.song.is_playing = is_toggled

    @alt_stop_button.pressed
    def alt_stop_button(self, _):
        self.song.is_playing = False

# okay decompiling ./MIDIRemoteScripts/Launchkey_MK3/transport.pyc
