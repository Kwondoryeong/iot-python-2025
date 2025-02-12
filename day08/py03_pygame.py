# py03_pygame.py
# 이벤트 처리

import pygame 
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_UP, K_RIGHT, K_DOWN
import sys  


pygame.init()
Surface = pygame.display.set_mode((640, 400))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Event')
pygame.key.set_repeat(10,10) # 키보드 연속 움직임 풀링1초에 10번 입력 가능

def main():
    xpos = 50
    ypos = 50
    while True:
        Surface.fill((12,34,56)) # Surface.fill((0,0,0))
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()   
                sys.exit()
            elif event.type == KEYDOWN: # 키보드 입력이 시작되었으면
                if event.key == K_LEFT:  # xpos - num 
                    if( xpos <= 20):
                        xpos = 20
                    xpos -= 5
                if event.key == K_RIGHT: # xpos + num
                    if( xpos >= 620):
                        xpos = 620
                    xpos += 5
                if event.key == K_UP: # ypos + num
                    if( ypos <= 20):
                        ypos = 20
                    ypos -= 5
                if event.key == K_DOWN: # ypos - num
                    if( ypos >= 380):
                        ypos = 380
                    ypos += 5

        pygame.draw.circle(Surface, (0,222,0), (xpos, ypos), 20) # 반지름 20
        pygame.display.update() 
        FPSCLOCK.tick(60) 

if __name__ == '__main__':
    main()