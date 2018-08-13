#!/usr/bin/env python
from pychromecast import get_chromecasts
from time import sleep

DEVICE_NAME = 'Quarto'
LINK = 'http://10.0.0.2:9000/disk/DLNA-PNMP3-OP01-FLAGS01700000/O0$1$8I257.mp3'
# LINK = 'http://10.0.0.2:9000/disk/DLNA-PNMP3-OP01-FLAGS01700000/O0$1$8I513.mp3' # SHORT

cast = next(c for c in get_chromecasts() if c.device.friendly_name == DEVICE_NAME)

mc = cast.media_controller

try:
    mc.play_media(LINK, 'audio/mp3')
    mc.block_until_active()
    sleep(5)
    
    while mc.is_playing:
        sleep(1)
finally:
    cast.quit_app()
