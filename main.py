def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми числами

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # Добавим оставшиеся простые числа
    for i in range(int(n**0.5) + 1, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

# Пример использования
upper_limit = int(input("Введите верхнюю границу поиска простых чисел: "))
result = sieve_of_eratosthenes(upper_limit)

print(f"Простые числа до {upper_limit}: {result}")