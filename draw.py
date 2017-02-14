from display import *

def draw_line1( screen, x0, y0, x1, y1, color ):
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

def draw_line2( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = a + 2*b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while y<=y1:
        plot(screen, color, x, y)
        if d<0:
            x+=1
            d+=a
        y+=1
        d+=b
 
def draw_line8( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = 2*a + b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while x<=x1:
        plot(screen, color, x, y)
        if d<0:
            y-=1
            d-=b
        x+=1
        d+=a

def draw_line7( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = a + 2*b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while y>=y1:
        plot(screen, color, x, y)
        if d>0:
            x+=1
            d+=a
        y-=1
        d-=b
 
def draw_line4( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = 2*a + b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while x>=x1:
        plot(screen, color, x, y)
        if d<0:
            y+=1
            d+=b
        x-=1
        d-=a

def draw_line3( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = a + 2*b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while y<=y1:
        plot(screen, color, x, y)
        if d>0:
            x-=1
            d-=a
        y+=1
        d+=b
 
def draw_line5( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = 2*a + b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while x>=x1:
        plot(screen, color, x, y)
        if d>0:
            y-=1
            d-=b
        x-=1
        d-=a

def draw_line6( screen, x0, y0, x1, y1, color ):
    b = x0-x1
    a = y1-y0
    d = a + 2*b
    x = x0
    y = y0
    a *= 2
    b *= 2
    while y>=y1:
        plot(screen, color, x, y)
        if d<0:
            x-=1
            d-=a
        y-=1
        d-=b
 
