from tkinter import *
import cmath
from decimal import Decimal, getcontext
import math
from math import pi, e, sin, cos, tan
from sympy import sympify,symbols,sqrt

# Словарь с переводами
translations = {
    'ru': {
        'welcome': 'Добро пожаловать! Введите число или выражение ниже, и вы получите квадратный корень',
        'hotline': 'При возникновении ошибок или вопросов обращайтесь к нам по почте: karnyjlin@gmail.com',
        'history': 'История вычислений:',
        'accuracy': 'Введите желаемое количество знаков после запятой:',
        'result': 'Показать результат',
        'clear_history': 'Очистить историю',
        'error': 'Ошибка: введено не допустимое число',
        'error_general': 'Ошибка: {}',
        'btn_lang':'Переключение языков:',
        'entry':'Строка ввода',
        'exit':'Строка ответа'
    },
    'en': {
        'welcome': 'Welcome! Enter a number or expression below to get the square root',
        'hotline': 'For errors or questions, contact us at: karnyjlin@gmail.com',
        'history': 'Calculation History:',
        'accuracy': 'Enter the desired number of decimal places:',
        'result': 'Show Result',
        'clear_history': 'Clear History',
        'error': 'Error: invalid number entered',
        'error_general': 'Error: {}',
        'btn_lang':'Switching languages:',
        'entry':'Input line',
        'exit': 'Response line'
    },
    'china':{
        'welcome': '欢迎！ 输入下面的数字或表达式，您将获得平方根。',
        'hotline': '如有任何错误或疑问，请与我们联络:karnyjlin@gmail.com',
        'history': '计算历史:',
        'accuracy': '输入所需的小数位数:',
        'result': '显示结果',
        'clear_history': '清除历史记录',
        'error': '错误：输入的数字无效',
        'error_general': '错误：{}',
        'btn_lang':'切换语言:',
        'entry':'输入线',
        'exit': '响应字符串'
    },
    'france':{
        'welcome': 'Bienvenue! Entrez un nombre ou une expression ci-dessous pour obtenir la racine carrée',
        'hotline': 'Pour des erreurs ou des questions, contactez-nous au: karnyjlin@gmail.com',
        'history': 'Historique des Calculs:',
        'accuracy': 'Entrez le nombre de décimales souhaité:',
        'result': 'Afficher le Résultat',
        'clear_history': "Effacer l'Historique",
        'error': 'Erreur: numéro non valide entré',
        'error_general': 'Erreur: {}',
        'btn_lang':'Changer de langue:',
        'entry':"Ligne d'entrée",
        'exit': "Ligne d'réponse"
    },
    'espanol':{
        'welcome': '¡Bienvenidos! Ingrese un número o expresión a continuación para obtener la raíz cuadrada',
        'hotline': 'Para errores o preguntas, contáctenos en: karnyjlin@gmail.com',
        'history': 'Historial de Cálculo:',
        'accuracy': 'Ingrese el número deseado de decimales:',
        'result': 'Mostrar Resultado',
        'clear_history': 'Borrar Historial',
        'error': 'Error: número no válido ingresado',
        'error_general': 'Error: {}',
        'btn_lang': 'Cambio de idiomas:',
        'entry':"Cadena d'entrada",
        'exit': "Cadena d'respuesta"
    }
}

# Текущий язык
current_language = 'ru'

# Создаем окно для программы
window = Tk()
window.title('Sqrt.Calculate')
window.resizable(None, None)
window.geometry("1200x800")
window.configure(background='#100873')  # голубой фон

# Определяем виджеты
label_open_bar = Label(text=translations[current_language]['welcome'],fg='#fff', font=('Arial', 14), bg='#100873')
label_open_bar.place(x=10, y=10)

label_change_lang=Label(text=translations[current_language]['btn_lang'],fg='#fff', font=('Arial', 25), bg='#100873')
label_change_lang.place(x=700, y=150)

label_entry_bar = Label(text=translations[current_language]['entry'],fg='#fff',font=('Arial', 11), bg='#100873')
label_entry_bar.place(x=2, y=50)

label_exit_bar = Label(text=translations[current_language]['exit'], fg='#fff', font=('Arial',11), bg='#100873')
label_exit_bar.place(x=2,y=90)


label_hotline_bar = Text(window, width=1000, height=10000, fg='#fff', font=('Arial', 12))
label_hotline_bar.place(x=0, y=700)
label_hotline_bar.insert(1.0, f"{translations[current_language]['hotline']}")
label_hotline_bar.configure(background='#100873')

# Поле для задания точности
entry_accuracy = Entry(window, bg='white', borderwidth=3, font=3, width=10)
entry_accuracy.place(x=700, y=90)
entry_accuracy.insert(0, "10")  # по умолчанию 10 знаков

# Поле для ввода выражения
entry_bar = Entry(window, bg="white", borderwidth=3, width=60, font=2)
entry_bar.place(x=124, y=50)

# Поле для вывода результата
entry_result = Entry(window, bg="lightyellow", borderwidth=3, width=60, font=2)
entry_result.place(x=124, y=90)

# Текстовое поле для истории
history_label = Label(window, text=translations[current_language]['history'], bg='#100873', fg='#fff', font=('Arial', 12, 'bold'))
history_label.place(x=10, y=500)

history_box = Listbox(window, width=80, height=8, font=('Arial', 12))
history_box.configure(bg='#8370D8')
history_box.place(x=10, y=530)

accuracy_label = Label(window, text=translations[current_language]['accuracy'], width=44, height=1, font=('Arial', 12,'bold'), fg='#fff', background='#100873')
accuracy_label.place(x=700, y=50)

# Кнопка очистки истории
btn_clear_history = Button(window, bg='red', fg='white', font=15, text=translations[current_language]['clear_history'], command=lambda: clear_history())
btn_clear_history.place(x=750, y=530, width=200, height=40)

# Кнопки для переключения языка
btn_lang_ru = Button(window, bg='#408AD2', fg='white', font=25, text='Русский', command=lambda: switch_language('ru'))
btn_lang_ru.place(x=700, y=205, width=150, height=60)

btn_lang_en = Button(window, bg='#408AD2', fg='white', font=25, text='English', command=lambda: switch_language('en'))
btn_lang_en.place(x=853, y=205, width=150, height=60)

btn_lang_china = Button(window, bg='#408AD2', fg='white', font=25, text='中文', command=lambda: switch_language('china'))
btn_lang_china.place(x=700, y=268, width=150, height=60)

btn_lang_francais = Button(window, bg='#408AD2', fg='white', font=25, text='Français', command=lambda: switch_language('france'))
btn_lang_francais.place(x=853, y=268, width=150, height=60)

btn_lang_spanish=Button(window, bg='#408AD2', fg='white', font=25, text='Español', command=lambda: switch_language('espanol'))
btn_lang_spanish.place(x=1006, y=205, width=150, height=60)

btn_analityc=Button(window, bg='#408AD2', fg='white', font=10, text='Аналитечский вид числа',command= lambda :handle_analytic_root())
btn_analityc.place(x=338, y=315, width=200, height=49)


# число, которое преобразуем в вид a√b
def sqrt_symbolic(expression_str, precision=10):
    """
    Вычисляет символьный квадратный корень с использованием sympy.
    Пытается обработать как действительные, так и комплексные числа.
    """
    try:
        x = symbols('x')
        # Пытаемся преобразовать строку в символьное выражение sympy
        # sympify пытается преобразовать числа в Decimal для большей точности
        expr = sympify(expression_str, rational=True, evaluate=False) # evaluate=False чтобы не вычислять сразу

        # Проверяем, является ли выражение числом или может быть вычислено до числа
        try:
            # Пробуем оценить выражение до числа.
            # Если оно комплексное, sympify может вернуть комплексное число.
            # Если оно действительное, но отрицательное, sqrt(expr) вызовет ошибку.
            evaluated_expr = expr.evalf()

            if isinstance(evaluated_expr, complex):
                # Если результат комплексный, используем sqrt_complex
                result_complex = sqrt_complex(complex(evaluated_expr), precision)
                return str(result_complex)
            elif isinstance(evaluated_expr, (int, float, Decimal)):
                # Если результат действительный
                if evaluated_expr < 0:
                    # Для отрицательных действительных чисел, sympy sqrt может дать NaN или ошибку
                    # Преобразуем в комплексное число для дальнейшей обработки
                    complex_val = complex(evaluated_expr, 0)
                    result_complex = sqrt_complex(complex_val, precision)
                    result_complex=str(result_complex)
                    result_complex=result_complex.replace('i','j')
                    return result_complex
                else:
                    # Для положительных действительных чисел
                    result_decimal = Decimal(evaluated_expr).sqrt()
                    # Форматируем с учетом точности
                    return f"+-({result_decimal:.{precision}f})"
            else:
                # Если оценка не дала число (например, осталось символьное выражение)
                # Пытаемся взять символьный корень
                symbolic_root = sqrt(expr)
                symbolic_root = str(symbolic_root)
                symbolic_root = symbolic_root.replace('sqrt', '√')
                return symbolic_root

        except (TypeError, ValueError, AttributeError):
            # Если evalf() не сработало или вернуло что-то неожиданное
            # Пробуем взять символьный корень напрямую
            symbolic_root = sqrt(expr)
            symbolic_root=str(symbolic_root)
            symbolic_root=symbolic_root.replace('sqrt','√')
            return symbolic_root

    except (SyntaxError, TypeError, ValueError, NameError, AttributeError) as e:
        # Если sympy не смог разобрать выражение
        return translations[current_language]['error_general'].format(f"Symbolic parsing error: {e}")
    except Exception as e:
        return translations[current_language]['error_general'].format(f"Unexpected symbolic error: {e}")


# Обработчик для кнопки btn_analytic
def handle_analytic_root():
    """Обрабатывает нажатие кнопки символьного корня."""
    formula = entry_bar.get()
    entry_result.delete(0, END)

    try:
        # Пытаемся получить точность, но для символьных вычислений она может быть не применима
        # или использоваться иначе (например, для evalf)
        precision = int(entry_accuracy.get())
        if precision < 1:
            precision = int(translations[current_language].get('entry_accuracy_default', 10))
    except ValueError:
        precision = int(translations[current_language].get('entry_accuracy_default', 10))

    # Вызываем функцию символьного корня
    result = sqrt_symbolic(formula, precision)
    entry_result.insert(0, result)
    add_to_history(formula, result)
def switch_language(lang):
    """Переключает язык интерфейса"""
    global current_language
    current_language = lang
    update_ui()

def update_ui():
    """Обновляет текст всех виджетов в зависимости от текущего языка"""
    label_open_bar.config(text=translations[current_language]['welcome'])
    label_hotline_bar.delete(1.0, END)
    label_hotline_bar.insert(1.0, f"     {translations[current_language]['hotline']}")
    label_change_lang.config(text=translations[current_language]['btn_lang'])
    label_entry_bar.config(text=translations[current_language]['entry'])
    label_exit_bar.config(text=translations[current_language]['exit'])
    history_label.config(text=translations[current_language]['history'])
    accuracy_label.config(text=translations[current_language]['accuracy'])
    btn_clear_history.config(text=translations[current_language]['clear_history'])
    btn_result.config(text=translations[current_language]['result'])


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

    # Читаем точность из поля
    try:
        precision = int(entry_accuracy.get())
        if precision < 1:
            precision = 10
    except:
        precision = 10

    try:
        if '0**0' in formula:
            error_msg = translations[current_language]['error']
            entry_result.insert(0, error_msg)
            add_to_history(formula, error_msg)
        elif '*j' in formula:
            formula = formula.replace('*j', 'j')
            result = str(sqrt_complex(complex(formula), precision))
            entry_result.insert(0, result)
            add_to_history(formula, result)
        elif 'j' in formula:
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
            result = str(round((eval(formula)) ** 0.5, precision))
            entry_result.insert(0, f"+-({result})")
            add_to_history(formula, f"+-({result})")
    except Exception as e:
        error_msg = translations[current_language]['error_general'].format(e)
        if len(error_msg) > 1:
            entry_result.insert(0, f"+-√({formula})")
            add_to_history(0, error_msg)

# Создание остальных кнопок
btn_CE = Button(window, bg='black', fg='white', text='CE', font=20, command=clear)
btn_CE.place(x=18, y=150, width=50, height=50)

btn_result = Button(window, bg='#fff', fg='#000', font=20, text=translations[current_language]['result'], command=count_result)
btn_result.place(x=338, y=206, width=200, height=103)

btn_xpnt = Button(window, bg='black', fg='white', font=20, text='^', command=lambda: input_entry('**'))
btn_xpnt.place(x=124, y=150, width=50, height=50)

btn_divide = Button(window, bg='black', fg='white', text='/', font=20, command=lambda: input_entry('/'))
btn_divide.place(x=177, y=150, width=50, height=50)

btn_1 = Button(window, bg='black', fg='white', text='1', font=20, command=lambda: input_entry('1'))
btn_1.place(x=18, y=205, width=50, height=50)

btn_2 = Button(window, bg='black', fg='white', font=20, text='2', command=lambda: input_entry('2'))
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

btn_0 = Button(window, bg='black', fg='white', font=20, text='0', command=lambda: input_entry('0'))
btn_0.place(x=71, y=150, width=50, height=50)

btn_pi = Button(window, bg='black', fg='white', font=20, text='π', command=lambda: input_entry('pi'))
btn_pi.place(x=283, y=150, width=50, height=50)

btn_e = Button(window, bg='black', fg='white', font=20, text='e', command=lambda: input_entry('e'))
btn_e.place(x=283, y=205, width=50, height=50)

btn_sin = Button(window, bg='black', fg='white', font=20, text='sin', command=lambda: input_entry('sin('))
btn_sin.place(x=283, y=260, width=50, height=50)

btn_cos = Button(window, bg='black', fg='white', font=20, text='cos', command=lambda: input_entry('cos('))
btn_cos.place(x=283, y=315, width=50, height=50)

btn_tg = Button(window, bg='black', fg='white', font=20, text='tg', command=lambda: input_entry('tan('))
btn_tg.place(x=336, y=150, width=50, height=50)

window.mainloop()

