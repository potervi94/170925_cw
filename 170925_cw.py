# -*- coding: utf-8 -*-
# Курс: AI+Python
# Модуль 12. Структури даних
# Тема: Стеки. Частина 2
#  Завдання 1
# Використовуючи стек створіть клас WebHistory
# Атрибути:
#  history – стек з історією відвідування веб сторінок
#  forward_history – стек з веб сторінками, для повернення
# «вперед»
# Методи:
#  add(page) – перейти на нову сторінку
#  undo() – повернутись на попередню сторінку
#  redo() – перейти вперед
#  get_current_page() – повернути поточну сторінку

from queue import  LifoQueue

class WebHistory:
    def __init__(self):
        self.history = LifoQueue()
        self.forward_history = LifoQueue()

    def add(self, page):
        self.history.put(page)
        self.forward_history = LifoQueue() #!!!
        print(f"Перейшли на {page}\n")

    def undo(self):
        if self.history.empty():
            print("Немає записів в історії!!!")
            return

        page = self.history.get()
        self.forward_history.put(page)

        if self.history.empty():
            print("Немає записів в історії!!!")
            return

        page = self.history.queue[-1]
        print(f"Повернулися на {page}\n")

    def redo(self):
        if self.forward_history.empty():
            print("Немає записів в redoісторії!!!")
            return

        page = self.forward_history.get()
        self.history.put(page)

        if self.forward_history.empty():
            print("Немає записів в redoісторії!!!")
            return

        page = self.forward_history.queue[-1]
        print(f"Повернулися на {page}\n")

wh=WebHistory()
wh.add("google")
wh.add("chat-gpt")
wh.undo()

wh.add("youtube")
wh.undo()
wh.undo()
wh.undo()

wh.redo()
wh.redo()
wh.redo()




# Завдання 2
# Використовуючи стек створіть клас EnterNumber для
# введення числа в рядку
# Атрибути:
#  digits – стек з введеними цифрами
# Методи:
#  add(digit) – додати нову цифру, вивести помилку якщо
# не цифра
#  undo() – видалити останню цифру
#  get_number() – повернути число
#  clear() – очистити стек
# Завдання 3
# Використовуючи стек створіть клас Calculator
# Атрибути:
#  operation – тип операції(за замовчуванням None)
#  answers – стек з результатами(за замовчуванням там
# один 0)
# Методи:
#  read() – читає текст введений користувачем, далі
# виконує наступні дії, в залежності від тексту
# o операція(+-*/) – змінює operation
# o число – дістати останнє число з answers(не
# видаляючи) та виконати дію operation, результат
# вивести на екран та добавити в answers
# o слово “show” – показати останній
