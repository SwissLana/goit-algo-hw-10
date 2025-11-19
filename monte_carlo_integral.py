import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та меж інтегрування
def f(x):
    return np.sin(x) + 2

a = 0          # нижня межа
b = np.pi      # верхня межа

# Створення діапазону значень для x (трохи ширший за [a, b] для краси)
x = np.linspace(-0.5, b + 0.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою на відрізку [a, b]
ix = np.linspace(a, b, 200)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування меж графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, np.max(y) + 0.2])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання вертикальних ліній для меж інтегрування
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

# Назва графіка
ax.set_title('Графік інтегрування f(x) = sin(x) + 2 від 0 до π')

plt.grid()
plt.show()



def monte_carlo_integral(num_points: int) -> float:
    """
    Метод Монте-Карло для обчислення інтеграла функції f(x)
    на відрізку [a, b].
    """
    # Максимальне значення функції на відрізку [a, b] (для побудови прямокутника) 
    f_max = np.max(f(np.linspace(a, b, num_points)))
    
    # Випадкові точки
    x_rand = np.random.uniform(a, b, num_points)
    y_rand = np.random.uniform(0, f_max, num_points)

    # Точки, що лежать під кривою
    under_curve = y_rand <= f(x_rand)

    # Частка потрапляння точок під криву
    p = np.mean(under_curve)

    # Площа прямокутника
    rect_area = (b - a) * f_max

    return rect_area * p


if __name__ == "__main__":
    # Monte Carlo для різної кількості точок
    for n in [1000, 10000, 100000]:
        value = monte_carlo_integral(n)
        print(f"\nКількість точок: {n}")
        print(f"Monte Carlo (N={n}): {value}")

    # Аналітичне значення інтеграла
    analytical = 2 + 2 * np.pi
    print("\nАналітичний інтеграл:", analytical)

    # Перевірка через quad
    quad_value, quad_error = spi.quad(f, a, b)
    print("За допомогою функції quad:", quad_value)
    print("Оцінка абсолютної помилки quad:", quad_error)

    # Детальніше порівняння для великої кількості точок 1000000 
    mc_last = monte_carlo_integral(1000000)
    print("\nДетальне порівняння для N=1'000'000:")
    print("\nMonte Carlo (1'000'000):", mc_last)
    print("Різниця з аналітичним:", abs(mc_last - analytical))
    print("Різниця з quad:", abs(mc_last - quad_value), "\n")
