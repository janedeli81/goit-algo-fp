import numpy as np
import matplotlib.pyplot as plt

# Кількість кидків
num_throws = 1000000

# Генеруємо кидки
throws = np.random.randint(1, 7, size=(num_throws, 2))
sums = throws.sum(axis=1)

# Підраховуємо кількість кожної суми
sum_counts = np.bincount(sums)[2:]  # Індекси 0 та 1 не використовуються

# Обчислюємо ймовірності
probabilities = sum_counts / num_throws * 100

# Візуалізація
sums_range = range(2, 13)
plt.bar(sums_range, probabilities)
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірність суми чисел на двох кубиках')
plt.xticks(sums_range)
plt.grid(axis='y')

plt.show()

# Виводимо отримані ймовірності
probabilities_dict = {sum_val: prob for sum_val, prob in zip(sums_range, probabilities)}
probabilities_dict
