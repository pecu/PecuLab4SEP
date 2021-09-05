import pygame as pg
pg.init()

#設定視窗
width, height = 640, 480                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Sean's game")         
#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#繪製幾何圖形
pg.draw.rect(bg, (0,0,255),[70, 70, 500, 60], 4)
pg.draw.rect(bg, (0,0,255),[70, 150, 500, 60], 0)            #線寬0為實心
pg.draw.circle(bg, (0,0,255),(100,300), 50, 4)
pg.draw.ellipse(bg, (0,0,255),[200,250, 150, 80], 4)
pg.draw.arc(bg, (0,0,255),[400, 250, 70, 150] ,5 ,1.5 , 4)
pg.draw.line(bg, (0,0,255),(550,250), (550, 400), 4)
#要在這兩條程式碼上面喔!!
screen.blit(bg, (0,0))
pg.display.update()


#關閉程式的程式碼
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()   