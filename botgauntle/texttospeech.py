#!/usr/bin/python
import pyglet
import time, os
from gtts import gTTS

pyglet.lib.load_library('avbin')
pyglet.have_avbin=True


tts = gTTS(text='Good morning Gladwin. We seem to have an error with Booysens', lang='en')
filename = 'hello.mp3'
tts.save(filename)

music = pyglet.media.load(filename, streaming=False)
music.play()

time.sleep(music.duration) #prevent from killing
os.remove(filename) #remove temperory file