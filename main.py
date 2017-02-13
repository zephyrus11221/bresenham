from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for i in range(200):
    color = [0, 255-i, i]
    draw_line1(screen, 0, 0, 500, 200-i, color)
    draw_line2(screen, 0, 0, 200-i, 500, color)
    draw_line8(screen, 0, 500, 500, 200-i, color)
    draw_line7(screen, 0, 500, 200-i, 0, color)
  
display(screen)
save_extension(screen, 'img.png')
