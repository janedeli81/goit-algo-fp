def greedy_algorithm(items, budget):
    # Сортуємо елементи за співвідношенням калорійності до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    chosen_items = []

    for item, values in sorted_items:
        if budget >= values['cost']:
            budget -= values['cost']
            total_calories += values['calories']
            chosen_items.append(item)
        if budget <= 0:
            break

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    # Створення таблиці динамічного програмування
    dp = [[0 for x in range(budget + 1)] for x in range(len(items) + 1)]
    item_list = list(items.keys())

    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_list[i - 1]]['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - items[item_list[i - 1]]['cost']] + items[item_list[i - 1]]['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних предметів
    chosen_items = []
    total_calories = dp[len(items)][budget]
    w = budget
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_list[i - 1])
            w -= items[item_list[i - 1]]['cost']

    chosen_items.reverse()
    return chosen_items, total_calories


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Використання алгоритмів
budget = 100
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

greedy_result, dynamic_result
