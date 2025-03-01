# pygame_samples
## demo_01.py

### ステップ２
 ウィンドウの大きさ
>~~~
>screen = pygame.display.set_mode([700, 500])
>~~~

ウィンドウの名前
>~~~
>pygame.display.set_caption("pygame demo - Let's play!")
>~~~

ウィンドウの背景の色
>~~~
> screen.fill((255, 255, 0))  # back ground color
>~~~

図形の色、座標、大きさ
>~~~
>pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
    pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
    pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
    pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))
>~~~
