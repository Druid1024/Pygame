import pygame as py
py.init()

win = py.display.set_mode((640,480),py.RESIZABLE)

running = True
clk = py.time.Clock()
t=py.time.get_ticks()

while running:
    for event in py.event.get():
        if event.type == py.QUIT or \
           (event.type == py.KEYDOWN and event.key==py.K_ESCAPE):
            running = False
    py.display.flip()
    clk.tick()
    for i in range(win.get_width()):
        for j in range(win.get_height()):
            win.set_at((i,j), (255,0,0))
            
    if (py.time.get_ticks()-t>1000):
        t=py.time.get_ticks()
        print(clk.get_fps())    

py.quit()
