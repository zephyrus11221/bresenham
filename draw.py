from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = 2*a + b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while x<=x1:
        plot(screen, color, x, y)
        if d>0:
            y+=1
            d+=b
        x+=1
        d+=a
    pass
