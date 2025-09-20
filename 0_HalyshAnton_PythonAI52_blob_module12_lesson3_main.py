# https://github.com/HalyshAnton/PythonAI52/blob/module12_lesson3/main.py
# стеки

# def func1():
#     func2()
#
#
# def func2():
#     func3()
#
# def func3():
#     print()
#
#     return
#
#
# func1()


from queue import LifoQueue
#
#
# stack = LifoQueue()  # стек
#
# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(4)
#
# print(stack.get())  # останній улемент який був доданий до стека
# print(stack.get())
# print(stack.get())
# print(stack.get())


# перевірка правильності дужок у виразі

# наївний
def naive(expr):
    counts = {
        '(': 0,
        '[': 0,
        '{': 0
    }

    reversed_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expr:
        if char in "([{":
            counts[char] += 1
        elif char in ")]}":
            reversed_bracket = reversed_brackets[char]

            if counts[reversed_bracket] == 0:
                print('Дужки неправильні')
                return
            counts[reversed_bracket] -= 1

    # перевірка чи залишились відкриті дужки
    for bracket in counts:
        if counts[bracket] > 0:
            print('Забагато відкритих дужок')
            return

    print('Дужки правильні')


def correct_method(expr):
    RED = "\033[91m"  # червоний колір
    RESET = "\033[0m"

    stack = LifoQueue()

    for i, char in enumerate(expr):
        if char in "([{":
            stack.put((i, char))
        elif char in ")]}":
            if stack.empty():
                print(expr[:i] + f"{RED}{char}{RESET}" + expr[i+1:])
                print('Дужки неправильні')
                return

            j, last_bracket = stack.get()

            if last_bracket + char not in ['()', '{}', '[]']:
                print(expr[:j] + f"{RED}{last_bracket}{RESET}" + expr[j + 1:i] + f"{RED}{char}{RESET}" + expr[i+1:])
                print('Дужки неправильні')
                return

    if not stack.empty():
        i, char = stack.get()
        print(expr[:i] + f"{RED}{char}{RESET}" + expr[i + 1:])
        print('Забагато відкритих дужок')
        return

    print('Дужки правильні')


expr = "num = [func(1 * )(2 - 3)), func2({'John', 'Mike})]"
#expr = "([)]"
correct_method(expr)