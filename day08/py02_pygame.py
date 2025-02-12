# py02_pygame.py
# PyGame 그래픽표현(선, 사각형, 원...)

import pygame 
from pygame.locals import QUIT 
from pygame.draw import *
import pygame.image as image
import sys  

pygame.init()
Surface = pygame.display.set_mode((400, 400))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic') 

def main():
    # 이미지 로드
    snake = image.load('./image/snake.png')
    # 텍스트 변수
    myfont = pygame.font.SysFont('NamuGothic', 50)
    message1 = myfont.render('This is my message', True, (255, 150, 255))
    message2 = myfont.render('This is PyGame', False, (255, 150, 255))

    while True:
        Surface.fill((0, 0, 0)) # Surface.fill((0,0,0))
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()   
                sys.exit()   

        # 화면 표현, start_pos(x,y)
        
        for x in range(10, 400, 10):
            line(Surface, 'white', (x,0), (x, 400))
        for y in range(10, 400, 10):
            line(Surface, 'white', (0, y), (400, y))    
        # 선
        pygame.draw.line(Surface, color=(255,0,0), start_pos=(30, 30), end_pos=(150,30), width=3)
        line(Surface, (0,255,0), (30, 60), (150, 60), 5)
        line(Surface, (0,0,255), (30, 90), (150, 150), 7)

        # 사각형
        pygame.draw.rect(Surface, color='white', rect=(200, 30, 50, 50)) # rect=(x축,y축,가로,세로)
        rect(Surface, (255,0,0), (260, 30, 50, 100), 5) # 두께

        # 원, 타원 (중심을 시작점으로)
        pygame.draw.circle(Surface, (255,255,0), (40, 160), 10)
        circle(Surface, (255,255,255), (80, 180), 20)
        circle(Surface, (255, 112, 20), (280, 170), 30, 10)
        rect(Surface, (255,0,0), (320, 30, 40, 80), border_radius=50)
        
        # 타원
        pygame.draw.ellipse(Surface, color=(255,255,255), rect=(280, 190, 100, 50))
        ellipse(Surface, (123,222,123), (260, 320, 80, 40), 7)

        # polygon 다각형(별 ...)

        # 이미지 flaticon.com
        Surface.blit(snake, (336,336))
        Surface.blit(snake, (0,336), (0,0,64,32))

        # 텍스트
        Surface.blit(message1, (30, 240))
        Surface.blit(message2, (30, 280))

        pygame.display.update() 
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()