# py02_gemini_app.py

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key="AIzaSyANCLGU18CAYv0TMU_Pu1MDwlD8AtU2h68")
model = genai.GenerativeModel('gemini-1.5-flash')

class window(Tk): # 부모 클래스 Tk의 상속받음 (Tk는 파라미터 아님)
    def __init__(self): # 기본값(None, ...) 들어있는것 없어도 ok
        super().__init__() # 부모 객체도 같이 초기화
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')
        # 클래스로 작업할 때 self 키워드 확인
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow() # 윈도우 화면 초기화 멤버함수(메서드)

    def initWindow(self):   # root --> self 변경
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        self.inputFrame = Frame(self, width=730, height=30, bg='#DFDFDF', padx=10)
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=87, height=1, wrap=WORD, font=self.myFont)
        # 8. 입력창에서 엔터를 치면 keypress 이벤트처리함수 발생
        self.textMessage.bind('<Key>', self.keypress)
        self.textMessage.pack(side=LEFT)

        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white',
                    font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=8, pady=5)

        self.textResult = ScrolledText(self, wrap=WORD, bg='#333333', fg='white', font=self.myFont) # bg='black'
        self.textResult.pack(fill=BOTH, expand=True)

        # 10. 스크롤 텍스트에 나올 메시지 디자인
        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow') # 태그가 user인 것 폰트와 fg 변경
        self.textResult.tag_configure('ai', font=self.myFont, foreground='limegreen') #89F336
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        self.textMessage.focus_set()

    def keypress(self,event):
        if event.char == '\r':
            self.responseMessage()

    def responseMessage(self):
        # showinfo('동작', f'이제 API를 호출하면 됩니다!\n{self.textMessage.get("1.0", END)}')
        self.inputText = self.textMessage.get('1.0', END).replace('\n','').strip()
        print(self.inputText)
        self.textMessage.delete('1.0', END)

        if self.inputText:
            try:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{self.inputText}\n\n', 'user') # 'user' 텍스트 아규먼트(태그)

                ai_response = model.generate_content(self.inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 태그
            except Exception as e:
                self.textResult.insert(END, f'Error:{str(e)}\n\n','error') 
            finally:
                self.textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운

    def onClosing(self):
        if askyesno('종료 확인', '종료하시겠습니까?'):
            self.destroy() # 완전 종료



if __name__ == '__main__':
    print('Tkinter 클래스 시작!')
    app = window() # tkinter 클래스 객체 생성
    app.mainloop()

        
