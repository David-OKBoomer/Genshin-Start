import vlc
import os
import ctypes
from ctypes import cast, POINTER, windll
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

#set program running location
path = os.path.abspath("Genshin Impact.exe")

#Set max volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)

#max screen brightness
sbc.set_brightness(100)

# Create VLC media player
instance = vlc.Instance('--no-xlib')
player = instance.media_player_new()

# Set volume and brightness to maximum
player.audio_set_volume(100)

# Play video in full screen
media = instance.media_new(os.path.abspath("Genshin_Start.mp4"))
media.get_mrl()
player.set_fullscreen(True)
player.set_media(media)
player.play()

# Wait for video to finish
while True:
    state = player.get_state()
    if state == vlc.State.Ended or state == vlc.State.Error:
        break
    player.set_fullscreen(True)
    sbc.set_brightness(100)
    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(0, None)

