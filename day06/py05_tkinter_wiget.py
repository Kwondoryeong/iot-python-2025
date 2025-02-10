# py05_tkinter_wiget.py
# Tkinter 위젯 학습용
from tkinter import *
import tkinter.font as fnt
from PIL import Image, ImageTk
from tkinter.messagebox import *

def buttonClick():
    showinfo('위젯', '버튼을 클릭했습니다!') # 다일러로그(메세지)박스
    
# def buttonClicktb():
    # entry = Entry(root, text=)

root = Tk()
# 이미지 객체
img = PhotoImage(file='./day06/kitty.png')

# 레이블에 이미지 표시
label = Label(root, image=img)
label.pack()

# 버튼 위젯
button = Button(root, text='클릭',command=buttonClick)
button.pack()

# 엔트리 위젯 - 사용자 입력
entry = Entry(root)
entry.pack()


# 라디오버튼
Label(root, text='가장 선호하는 프로그래밍 언어 선택').pack()

choice = IntVar()
Radiobutton(root, text='C', value=1, variable=choice).pack(anchor=W)
Radiobutton(root, text='C#', value=2, variable=choice, state='disabled').pack(anchor=W)
Radiobutton(root, text='Python', value=3, variable=choice).pack(anchor=W)
Radiobutton(root, text='Java', value=4, variable=choice).pack(anchor=W)
# 체크박스
Label(root, text='좋아하는 과일을 모두 선택').pack()

orange = IntVar()
Checkbutton(root, text='오렌지', variable=orange).pack(anchor=W)
banana = IntVar()
Checkbutton(root, text='바나나', variable=banana).pack(anchor=W)
mango = IntVar()
Checkbutton(root, text='망고', variable=mango).pack(anchor=W)

# button1 = Button(root, text='텍스트박스 클릭',command=buttonClicktb)
# button1.pack()

# 리스트박스 위젯
lstBx = Listbox(root, height=4)
lstBx.pack()
lstBx.insert(END, 'Python')
lstBx.insert(END, 'Java')
lstBx.insert(END, 'Ruby')
lstBx.insert(END, 'Php')

# 컨테이너 위젯 중 프레임
frame = Frame(root, width=600, height=200, bg='gray')
frame.pack()
# 프레임에 들어갈 위젯
button2 = Button(frame, text='버튼2', width=20)
button2.pack(side=LEFT)
button3 = Button(frame, text='버튼3', width=20)
button3.pack(side=LEFT)
button4 = Button(frame, text='버튼4', width=20)
button4.pack(side=LEFT)
root.mainloop()