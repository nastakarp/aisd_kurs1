from concurrent.futures import ThreadPoolExecutor


def sieve_of_eratosthenes(limit):
    """
    Реализация решета Эратосфена для нахождения всех простых чисел до заданного предела.
    Аргументы:
        limit (int): Верхний предел для поиска простых чисел.
    Возвращает:
        list: Список всех простых чисел до 'limit'.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [x for x in range(limit + 1) if is_prime[x]]


def lucas_lehmer_test(p):
    """
    Тест Люка-Лемера для проверки числа Мерсенна.
    Аргументы:
        p (int): Простое число, используемое для генерации числа Мерсенна (2^p - 1).
    Возвращает:
        bool: True, если число Мерсенна простое, иначе False.
    """
    if p == 2:
        return True  # M_2 = 3, простое

    # Шаг 1: Вычисляем число Мерсенна
    M_p = 2 ** p - 1

    # Шаг 2: Инициализируем последовательность Люка-Лемера
    s = 4

    # Шаг 3: Вычисляем последовательность (p-2) раз
    for _ in range(p - 2):
        s = (s ** 2 - 2) % M_p

    # Шаг 4: Если результат равен 0, то M_p простое
    return s == 0


def check_mersenne_prime(p):
    """
    Проверка числа Мерсенна на простоту.
    Возвращает строку с результатом проверки.
    """
    is_mersenne_prime = lucas_lehmer_test(p)
    return f"M_{p} = 2^{p} - 1: {'Простое' if is_mersenne_prime else 'Составное'}"

"""
Основная функция для проверки чисел Мерсенна.
"""

# Генерация простых чисел с помощью решета Эратосфена
limit = 1000  # Задайте предел для поиска простых чисел
primes = sieve_of_eratosthenes(limit)

# Используем ThreadPoolExecutor для многопоточности
with ThreadPoolExecutor() as executor:
    results = executor.map(check_mersenne_prime, primes)

# Вывод результатов
for result in results:
    print(result)


