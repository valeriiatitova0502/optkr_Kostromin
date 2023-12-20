import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x):
    return 2 * x**2 + 16 / x

# Производная функции
def df(x):
    return 4 * x - 16 / x**2

# Интервал для поиска экстремума
a, b = 0.000001, 5

# Точность поиска
tolerance = 1e-6

# Нахождение экстремума с использованием метода равномерного поиска
def uniform_search(f, a, b, tol):
    iterations = 0

    print("Итерация\tЛевая граница\tПравая граница\tКорень\t\tf(x)")

    while abs(b - a) > tol:
        x = (a + b) / 2
        f_x = f(x)

        x_plus_tol = x + tol
        x_minus_tol = x - tol

        if f(x_minus_tol) < f(x_plus_tol):
            b = x
        else:
            a = x

        print(f"{iterations}\t\t{a:.6f}\t\t{b:.6f}\t\t{x:.6f}\t\t{f(x):.6f}")
        iterations += 1

    return (a + b) / 2, f((a + b) / 2)

# Метод деления пополам с производной
def bisection_search(f, df, a, b, tol):
    iterations = 0

    print("Итерация\tЛевая граница\tПравая граница\tКорень\t\tf(x)")

    while abs(b - a) > tol:
        x = (a + b) / 2
        f_x = f(x)

        if df(x) > 0:
            b = x
        else:
            a = x

        print(f"{iterations}\t\t{a:.6f}\t\t{b:.6f}\t\t{x:.6f}\t\t{f(x):.6f}")
        iterations += 1

    return (a + b) / 2, f((a + b) / 2)

# Использование метода равномерного поиска
root_uniform, extremum_value_uniform = uniform_search(f, a, b, tolerance)
print(f'\nЭкстремум функции f(x) на интервале [0.000001, 5] методом равномерного поиска находится в точке {root_uniform:.6f} с f(x) = {extremum_value_uniform:.6f}')

# Использование метода деления пополам с производной
root_bisection, extremum_value_bisection = bisection_search(f, df, a, b, tolerance)
print(f'\nЭкстремум функции f(x) на интервале [0.00001, 5] методом деления пополам находится в точке {root_bisection:.6f} с f(x) = {extremum_value_bisection:.6f}')

# Построение графика функции
x_values = np.linspace(-1, 5, 1000)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = 2x^2 + 16/x', color='b')
plt.axhline(y=0, color='k', linestyle='--') # Добавление горизонтальной линии y=0
plt.axvline(x=0, color='k', linestyle='--')
plt.grid() # Добавление сетки
plt.xlabel('x')
plt.title('График функции')

# Отмечаем найденные экстремумы
plt.scatter(root_uniform, extremum_value_uniform, color='g', marker='o', label=f'Равномерный поиск ({root_uniform:.6f}, {extremum_value_uniform:.6f})')
plt.scatter(root_bisection, extremum_value_bisection, color='m', marker='o', label=f'Деление пополам ({root_bisection:.6f}, {extremum_value_bisection:.6f})')

plt.legend()
plt.grid(True)
plt.show()
