from random import shuffle, randint

from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget, QButtonGroup
app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Я получил по истории 5 ... я в шоке')
main_win.resize(600, 400)

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong3, wrong2):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

lbl = QLabel('КАКОЙ НАЦИОНАЛЬНОСТИ НЕ СУЩЕВСТВУЕТ ?')
btn_otv = QPushButton('ОТВЕЧАЙ')

box = QGroupBox('ОТВЕТИК :')

btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеулеты')

vlbox = QVBoxLayout()
hlbox1 = QHBoxLayout()
hlbox2 = QHBoxLayout()
hlbox1.addWidget(btn1)
hlbox2.addWidget(btn2)
hlbox1.addWidget(btn3)
hlbox2.addWidget(btn4)
vlbox.addLayout(hlbox1)
vlbox.addLayout(hlbox2)
box.setLayout(vlbox)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lbl)
layout_line2.addWidget(box)
layout_line3.addWidget(btn_otv)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

vl = QVBoxLayout()
vl.addLayout(layout_line1, stretch = 2)
vl.addLayout(layout_line2, stretch = 8)
vl.addStretch(stretch = 1)
vl.addLayout(layout_line3, stretch = 1)
vl.addStretch(stretch = 1)  

box2 = QGroupBox('Результаты теста')
a = QLabel('Правильный ответ :')
lbl2 = QLabel('Правельный ответ : Смурфы')
vlbox2 = QVBoxLayout()
hlbox4 = QHBoxLayout()
hlbox5 = QHBoxLayout()
hlbox4.addWidget(a)
hlbox5.addWidget(lbl2)
vlbox2.addLayout(hlbox4)
vlbox2.addLayout(hlbox5)
box2.setLayout(vlbox2)
layout_line2.addWidget(box2)
box2.hide()

main_win.setLayout(vl)

def show_result():
    box.hide()
    box2.show()
    btn_otv.setText('Следующий вопрос')

def show_question():
    box.show()
    box2.hide()
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)
    btn_otv.setText('ответить')

answers = [btn1, btn2, btn3, btn4]

def ask(q: Question):
    shuffle(answers)
    lbl.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong3)
    answers[3].setText(q.wrong2)
    lbl2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Что такое ')
        print('Всего вопросов - ', main_win.total)
        print('Правильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total * 100.0, '%')
    else:
        show_correct('Неправильно')
        print('Рейтинг:', main_win.score/main_win.total * 100.0, '%')

def show_correct(res):
    lbl.setText(res)
    show_result()

question_list = []
question_list.append(Question('X + 18 = 2x - 34', 'Х = 52', 'Х = 2', 'Х = 102', 'Х = -14'))
question_list.append(Question('X + 2 = 10', 'Х = 8', 'Х = 2', 'Х = 102', 'Х = -14'))


def next_question():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]    
    print('Статистика')
    print('Всего вопросов - ', main_win.total)
    print('Правильных ответов:', main_win.score)
 
    ask(q)

def click_OK():
    if btn_otv.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()

btn_otv.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0 

next_question()



main_win.show()
app.exec_()