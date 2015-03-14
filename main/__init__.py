import pyglet
import os

#set res path
respath = os.path.join(os.path.abspath('.'),'..','res')
pyglet.resource.path = [respath]
pyglet.resource.reindex()
print(pyglet.resource.image)



####
platform = pyglet.window.get_platform()
display = platform.get_default_display()

screen = display.get_default_screen()
proportion = screen.height/screen.width #h/w

winw = screen.width//2
winh = screen.height//2
#resources
width = winw//2
height = winh//2
label = pyglet.text.Label('Just and Just As',
                          font_name='Times New Roman',
                          font_size=36,
                          x=width, y=height,
                          anchor_x='center', anchor_y='center')

image = pyglet.resource.image('BasicCube.png')
image.width = 200
image.height = 200

#note: streaming=False, when the sound is short and is used rapidly
music = pyglet.resource.media('mm1.mp3') #cant have music with a sample rate of 0
music.play()


#window
window = pyglet.window.Window(winw,winh,resizable=True)
window.push_handlers(pyglet.window.event.WindowEventLogger())

@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == pyglet.window.mouse.LEFT:
        print('Left was clicked')

@window.event
def on_key_press(symbol,modifiers):
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    label.draw()

pyglet.app.run()