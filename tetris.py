import pygame as pg 

BREITE, SPALTEN, ZEILEN = 400, 10, 20
ABSTAND = BREITE // SPALTEN
HÖHE = ABSTAND * ZEILEN

pg.init()
screen = pg.display.set_mode((BREITE, HÖHE))

weitermachen = True
while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False


pg.quit()
