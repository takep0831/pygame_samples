# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([400, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)

display1 = Seven_seg(screen)
display1.init_col(BLOCK_SIZE=7, BLOCK_INTV=5, COLOR_ON=YELLOW, COLOR_OFF=GRAY) #　大きさと色
display1.init_row(X_ORG=5, Y_ORG=50, COL_INTV=10)

display2 = Seven_seg(screen)
display2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
display2.init_row(X_ORG=2, Y_ORG=18, COL_INTV=6)

display3 = Seven_seg(screen)
display3.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=(120, 200, 250), COLOR_OFF=GRAY)
display3.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6) #座標


running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。
        
        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second * 1)

        display1.disp_num2(zfil=True, rjust=9, num=time_now, base=10)

        display2.update_col(col=0, num=count // (10 ** 4), base=10)

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second * 1)
        
        display3.disp_num2(zfil=True, rjust=6, num=time_now, base=10)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
