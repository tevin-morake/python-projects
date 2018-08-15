import pyglet

music = pyglet.resource.media('hello2.mp3')
music.play()

pyglet.app.run()