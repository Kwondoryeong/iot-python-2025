# py01_pygame.py

import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT  # 종료처리 변수
import sys    # 운영체제 시스템 명령 sys.executable(경로확인)

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((640, 400)) ## tkinter == root.geometry('640x400')
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic') # 제목

def main():
    while True:
        Surface.fill((255, 255, 255)) # #FFFFFF = WHITE  #00FFFFFF = '00'alpha(투명도)
        # Surface.fill('#123456') or Surface.fill(color='crimson')
        for event in pygame.event.get(): # 키보드, 마우스, 이벤트 체크
            if event.type == QUIT: # WM_DELETE_WINDOW (닫기버튼)
                pygame.quit()   # Pygame을 종료
                sys.exit()      # 윈도우앱 탈출


        pygame.display.update() # 지금까지 작성 코드를 윈도우창에 표시
        FPSCLOCK.tick(30) # 30 FPS 지정

if __name__ == '__main__':
    main()