import matplotlib.pyplot as plt
import numpy as np


def draw_pythagoras_tree(x, y, angle, depth, max_depth):
    if depth > max_depth:
        return

    # Визначаємо довжину гілки залежно від глибини рекурсії
    branch_length = 10 * (0.8 ** depth)

    # Обчислюємо нові координати кінця гілки
    x_end = x + branch_length * np.cos(np.radians(angle))
    y_end = y + branch_length * np.sin(np.radians(angle))

    # Малюємо лінію (гілку)
    plt.plot([x, x_end], [y, y_end], 'k-', lw=2)

    # Рекурсивні виклики для лівої та правої гілки
    new_depth = depth + 1
    draw_pythagoras_tree(x_end, y_end, angle - 45, new_depth, max_depth)
    draw_pythagoras_tree(x_end, y_end, angle + 45, new_depth, max_depth)


# Налаштування графіку
plt.figure(figsize=(10, 8))
plt.axis('equal')
plt.axis('off')

# Виклик функції для відображення "Дерева Піфагора"
max_depth = 10  # Максимальна глибина рекурсії, може бути змінена користувачем
draw_pythagoras_tree(0, 0, 90, 0, max_depth)

plt.show()
