from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for i in range(250):
    color = [i, i, i]
    draw_line1(screen, 0, 0, 500, 500-i, color)
    draw_line3(screen, 500, 0, 250-i, 500, color)
    draw_line5(screen, 500, 500, 0, 250+i, color)
    draw_line7(screen, 0, 500, 500-i, 0, color)
for i in range(200):
    color = [i/2, 0, 200-i/2]
    draw_line2(screen, 250+i, 50, 450, 450, color)
    draw_line4(screen, 450, 250+i, 50, 450, color)
    draw_line6(screen, 250-i, 450, 50, 50, color)
    draw_line8(screen, 50, 250-i, 450, 50, color)
for i in range(200):
    color = [0, 255-i, 200-i]
    draw_line1(screen, 0, 0, 500, 200-i, color)
    draw_line3(screen, 500, 0, 300+i, 500, color)
    draw_line5(screen, 500, 500, 0, 300+i, color)
    draw_line7(screen, 0, 500, 200-i, 0, color)
    
display(screen)
save_extension(screen, 'img.png')
