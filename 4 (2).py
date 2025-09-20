from tkinter import *
import cmath
from decimal import Decimal, getcontext
import math

# создаем окно для программы
window = Tk()
window.title('Вывод корня')
window.resizable(None, None)
window.geometry("1200x800")
window.configure(background='#100873')  # голубой фон

label_open_bar = Label(
    text='Добро пожаловать! Введите число или выражение ниже, и вы получите квадратный корень',
    fg='#fff', font=('Arial', 14), bg='#100873')
label_open_bar.place(x=10, y=10)

label_hotline_bar=Text(window,width=1000,height=10000, fg='#fff', font=('Arial', 12))
label_hotline_bar.place(x=0, y=700)
label_hotline_bar.insert(1.0,'     При возникновении ошибок или вопросов обращайтесь к нам по почте: karnyjlin@gmail.com')
label_hotline_bar.configure(background='#100873')

def long_num(num, accuracy):
    """Корень из большого числа с заданной точностью"""
    getcontext().prec = accuracy + 1
    num = Decimal(num)
    return num**(Decimal(1)/Decimal(2))


def sqrt_complex(z: complex, precision: int = 10):
    """Квадратный корень из комплексного числа с заданной точностью"""
    getcontext().prec = precision + 5
    r, phi = cmath.polar(z)
    r_sqrt = Decimal(r).sqrt()
    phi_half = Decimal(phi) / 2
    root = complex(
        float(r_sqrt) * cmath.cos(float(phi_half)),
        float(r_sqrt) * cmath.sin(float(phi_half))
    )
    return complex(
        round(root.real, precision),
        round(root.imag, precision)
    )


# поле для задания точности
entry_accuracy = Entry(window, bg='white', borderwidth=3, font=3, width=10)
entry_accuracy.place(x= 700, y=90)
entry_accuracy.insert(0, "10")  # по умолчанию 10 знаков

# поле для ввода выражения
entry_bar = Entry(window, bg="white", borderwidth=3, width=60, font=2)
entry_bar.place(x=10, y=50)

# поле для вывода результата
entry_result = Entry(window, bg="lightyellow", borderwidth=3, width=60, font=2)
entry_result.place(x=10, y=90)

# текстовое поле для истории
history_label = Label(window, text="История вычислений:", bg='#100873', fg='#fff', font=('Arial', 12, 'bold'))
history_label.place(x=10, y=500)

history_box = Listbox(window, width=80, height=8, font=('Arial', 12))
history_box.configure(bg='#8370D8')
history_box.place(x=10, y=530)

accuracy_label = Label(window, text='Введите желаемое количество знаков после запятой:', width=44, height=1, font=('Arial',12), fg='#fff',background='#100873')
accuracy_label.place(x=700, y=50)

def clear():
    entry_bar.delete(0, END)
    entry_result.delete(0, END)


def input_entry(symbol):
    entry_bar.insert(END, symbol)


def add_to_history(expr, res):
    """Добавляем запись в историю"""
    history_box.insert(0, f"{expr} → {res}")
    if history_box.size() > 10:  # храним только 10 последних
        history_box.delete(10, END)


def clear_history():
    """Очищаем историю вычислений"""
    history_box.delete(0, END)


def count_result():
    formula = entry_bar.get()
    entry_result.delete(0, END)

    # читаем точность из поля
    try:
        precision = int(entry_accuracy.get())
        if precision < 1:
            precision = 10
    except:
        precision = 10

    try:
        if '*j' in formula:
            formula=formula.replace('*j','j' )
        if 'j' in formula:
            result = str(sqrt_complex(complex(formula), precision))
            entry_result.insert(0, result)
            add_to_history(formula, result)
        elif len(formula) > 100:
            result = str(long_num(float(eval(formula)), precision))
            entry_result.insert(0, f"+-({result})")
            add_to_history(formula, f"+-({result})")
        elif eval(formula) < 0:
            result = str(sqrt_complex(complex(eval(formula)), precision))
            entry_result.insert(0, result)
            add_to_history(formula, result)
        elif eval(formula) == 0:
            result = "0"
            entry_result.insert(0, result)
            add_to_history(formula, result)
        else:
            result = str(round((eval(formula))**0.5, precision))
            entry_result.insert(0, f"+-({result})")
            add_to_history(formula, f"+-({result})")

    except Exception as e:
        error_msg = f"Ошибка: {e}"
        entry_result.insert(0, error_msg)
        add_to_history(formula, error_msg)


# создание кнопок и их подключение к функциям
btn_CE = Button(window, bg='black', fg='white', text='CE', font=20, command=clear)
btn_CE.place(x=18, y=150, width=50, height=50)

btn_result = Button(window, bg='#fff', fg='#000', font=20, text='Показать результат', command=count_result)
btn_result.place(x=290, y=233, width=200, height=50)

btn_xpnt = Button(window, bg='black', fg='white', font=20, text='^', command=lambda: input_entry('**'))
btn_xpnt.place(x=124, y=150, width=50, height=50)

btn_divide = Button(window, bg='black', fg='white', text='/', font=20, command=lambda: input_entry('/'))
btn_divide.place(x=177, y=150, width=50, height=50)

btn_1 = Button(window, bg='black', fg='white', text='1', font=20, command=lambda: input_entry('1'))
btn_1.place(x=18, y=205, width=50, height=50)

btn_2 = Button(window, bg='black', fg='white', font=20,text='2', command=lambda: input_entry('2'))
btn_2.place(x=71, y=205, width=50, height=50)

btn_3 = Button(window, bg='black', fg='white', font=20, text='3', command=lambda: input_entry('3'))
btn_3.place(x=124, y=205, width=50, height=50)

btn_mltpl = Button(window, bg='black', fg='white', font=20, text='*', command=lambda: input_entry('*'))
btn_mltpl.place(x=177, y=205, width=50, height=50)

btn_4 = Button(window, bg='black', fg='white', font=20, text='4', command=lambda: input_entry('4'))
btn_4.place(x=18, y=260, width=50, height=50)

btn_5 = Button(window, bg='black', fg='white', font=20, text='5', command=lambda: input_entry('5'))
btn_5.place(x=71, y=260, width=50, height=50)

btn_6 = Button(window, bg='black', fg='white', font=20, text='6', command=lambda: input_entry('6'))
btn_6.place(x=124, y=260, width=50, height=50)

btn_minus = Button(window, bg='black', fg='white', font=20, text='-', command=lambda: input_entry('-'))
btn_minus.place(x=177, y=260, width=50, height=50)

btn_7 = Button(window, bg='black', fg='white', font=20, text='7', command=lambda: input_entry('7'))
btn_7.place(x=18, y=315, width=50, height=50)

btn_8 = Button(window, bg='black', fg='white', font=20, text='8', command=lambda: input_entry('8'))
btn_8.place(x=71, y=315, width=50, height=50)

btn_9 = Button(window, bg='black', fg='white', font=20, text='9', command=lambda: input_entry('9'))
btn_9.place(x=124, y=315, width=50, height=50)

btn_plus = Button(window, bg='black', fg='white', font=20, text='+', command=lambda: input_entry('+'))
btn_plus.place(x=177, y=315, width=50, height=50)

btn_dot = Button(window, bg='black', fg='white', font=20, text='.', command=lambda: input_entry('.'))
btn_dot.place(x=230, y=150, width=50, height=50)

btn_bracket_open = Button(window, bg='black', fg='white', font=20, text='(', command=lambda: input_entry('('))
btn_bracket_open.place(x=230, y=205, width=50, height=50)

btn_bracket_close = Button(window, bg='black', fg='white', font=20, text=')', command=lambda: input_entry(')'))
btn_bracket_close.place(x=230, y=260, width=50, height=50)

btn_complex = Button(window, bg='black', fg='white', font=20, text='j', command=lambda: input_entry('j'))
btn_complex.place(x=230, y=315, width=50, height=50)

btn_0 =Button(window, bg='black', fg='white', font=20, text='0', command=lambda: input_entry('0'))
btn_0.place(x=71, y=150, width=50, height=50)

# кнопка очистки истории
btn_clear_history = Button(window, bg='red', fg='white', font=15, text='Очистить историю', command=clear_history)
btn_clear_history.place(x=750, y=530, width=200, height=40)

window.mainloop()
