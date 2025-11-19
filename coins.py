import timeit

def find_coins_greedy(amount, coins=None):
    """
    Жадібний алгоритм розбиття суми на монети.
    Повертає словник {номінал: кількість}.
    """
    if coins is None:
        # Набір монет за умовою задачі
        coins = [50, 25, 10, 5, 2, 1]

    coins_count = {}
    rest = amount  # решта, яку ще потрібно видати

    # Проходимося по монетах від найбільшої до найменшої
    for coin in coins:
        if rest <= 0:
            break

        # скільки монет такого номіналу можемо використати
        count = rest // coin
        if count > 0:
            coins_count[coin] = count
            rest -= coin * count  # зменшуємо залишок суми

    return coins_count


def find_min_coins(amount, coins=None):
    """
    Алгоритм динамічного програмування для пошуку
    мінімальної кількості монет.
    Повертає словник {номінал: кількість}.
    """
    if coins is None:
        coins = [50, 25, 10, 5, 2, 1]

    # min_coins[i] – мінімальна кількість монет для суми i
    min_coins = [0] + [float("inf")] * amount
    # last_coin[i] – який номінал монети використовували останнім для суми i
    last_coin = [0] * (amount + 1)

    for sub_sum in range(1, amount + 1):
        for coin in coins:
            if coin <= sub_sum and min_coins[sub_sum - coin] + 1 < min_coins[sub_sum]:
                min_coins[sub_sum] = min_coins[sub_sum - coin] + 1
                last_coin[sub_sum] = coin

    # якщо сума недосяжна (теоретично, у нас є монета 1, тому такого не буде)
    if min_coins[amount] == float("inf"):
        return {}

    # Відновлюємо набір монет з таблиці last_coin
    res = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin[current_sum]
        res[coin] = res.get(coin, 0) + 1
        current_sum -= coin

    return res


if __name__ == "__main__":
    # Тест з умови
    test_amount = 113
    print(f"\nСума: {test_amount}")
    print("Жадібний алгоритм:", find_coins_greedy(test_amount))
    print("Динамічне програмування:", find_min_coins(test_amount))

    # Декілька сум для порівняння
    amounts = [113, 999, 5000]

    print("\nПорівняння часу виконання:\n")
    for a in amounts:
        greedy_time = timeit.timeit(lambda: find_coins_greedy(a), number=1000)
        dp_time = timeit.timeit(lambda: find_min_coins(a), number=100)

        print(f"Сума: {a}")
        print(f"find_coins_greedy: {greedy_time:.6f} сек (1000 запусків)")
        print(f"find_min_coins:   {dp_time:.6f} сек (100 запусків)\n")