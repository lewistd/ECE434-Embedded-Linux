#!/bin/sh
export FRAMEBUFFER=/dev/fb0

# Play a movie
SDL_VIDEODRIVER=fbcon 
SDL_FBDEV=/dev/fb0
mplayer -vf-add flip -framedrop RedsNightmare.mpg
