# myMovieApp.py
# 영화정보 입력, 출력, 검색, 삭제, 종료
import os # 운영체제 모듈
from Movie import Movie # 모듈 이름 Movie 의 Movie 클래스 가져옴

VERSION = 0.5

# 콘솔 화면 클리어
def clearScreen(): # os에 특화된 팁.
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command)

# 메인에서 제일 처음 실행되는 함수
def run():
    # movie = Movie.Movie() # 모듈 Movie. 클래스 Movie
    # movie = Movie('어벤져스: 인피니티 워', 2018, '디즈니', 8.6)
    # print(movie)
    # set_menu()
    clearScreen() # 최초에 화면 클리어 한번
    lst_movie = [] # 영화 리스트를 담는 변수 list타입
    load_movie(lst_movie)
    while True:
        try:
            sel_menu = set_menu()
            if sel_menu == 1:
                # print('영화 입력')
                # print('###################################')
                movie = set_movie()
                lst_movie.append(movie)
                
            elif sel_menu == 2:
                # print('영화 출력')
                # print('###################################')
                get_movie(lst_movie)
                
            elif sel_menu == 3:
                # print('영화 검색')
                title = input('검색할 영화명 입력 > ')
                # print('###################################')
                search_movie(lst_movie, title)                
                
            elif sel_menu == 4:
                # print('영화 삭제')
                title = input('삭제할 영화명 입력 > ')
                # print('###################################')
                del_movie(lst_movie, title)

            elif sel_menu == 5:
                # print('앱 종료')
                # 종료직전 DB생성하고 완료
                save_movie(lst_movie)
                break # 반복문 탈출
            else:
                # print('***** 다시 입력하세요(1 ~ 5) *****')
                pass    
            
            input() # 입력대기 : 엔터치면 넘어감
            clearScreen() # 메뉴 기능이 완료되면 화면 클리어
                    
        except Exception as e:
            pass
            # set_menu = 0


def set_movie():
    title, year, company, rate = input(f'영화입력[제목|개봉년도|제작사|평점 순] > ').split('|')
    year = int(year) # 년도는 정수
    rate = float(rate) # 평점은 실수
    # 입력 중 발생하는 예외 튜플값 변경X
    # print(title, year, company, rate)
    movie = Movie(title = title, year = year, company = company, rate = rate) # 데이터형 예외
   
    return movie

# lst변수는 list타입이라고 지정
def get_movie(items: list):
    for item in items:
        print(item) # Movie클래스 객체(print(movie))와 같음

# 영화검색 함수
def search_movie(items: list, title: str):
    for item in items: # item이 Movie 클래스인지 알 수 없음
        if item.isNameContain(title):
            print(item)

def del_movie(items: list, title: str):
    for i, item in enumerate(items): # enumerate 반복되는 번호 출력 '0' 인피니티 '1' 엔드게임 ..
        if item.isNameExist(title):
            del items[i] # 인덱스로 리스트에 요소하나를 삭제

# 폴더에 파일로 영화리스트 저장
def save_movie(items: list):
    f = open('movie_db.txt', mode='w', encoding='utf-8') # 파일쓰기로 오픈
    for item in items:
        f.write(f'{item.getTitle()}|')
        f.write(f'{item.getYear()}|')
        f.write(f'{item.getCompany()}|')
        f.write(f'{item.getRate()}\n')
        
    f.close()

def load_movie(items: list):
    f = open('movie_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replace('\n','') # 한줄 읽은 후 \n
        if not line: break  # 무한루프 탈출 조건
    
        lines = line.split('|') # 구분자로 잘라서 네개의 요소의 리스트 생성
        title = lines[0]
        year = int(lines[1])
        company = lines[2]
        rate = float(lines[3]) # '8.6\n' 으로 저장 후 한줄 개행됨 

        movie = Movie(title, year, company, rate)
        items.append(movie)
    f.close()


def set_menu():
    str_menu = (f'내 영화 앱 v{VERSION}\n'
                '1. 영화 입력\n'
                '2. 영화 출력\n'
                '3. 영화 검색\n'
                '4. 영화 삭제\n'
                '5. 앱 종료\n') 
    print(str_menu)
    sel_menu = int(input('메뉴 번호입력: ')) # 예외있음
    return sel_menu

def set_movie_input():
    title, year, company, rate = input(f'영화입력[제목|개봉년도|제작사|평점 순] > ').split('|')

if __name__ == '__main__': # 시작되는 모듈(entry point)
    # print('내 영화 앱 시작')
    run()



print('프로그램 종료')

