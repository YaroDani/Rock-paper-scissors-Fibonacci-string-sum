def suma_fibonachi(i):
    a, b = 0, 1
    total_sum = 0

    for _ in range(i):
        total_sum += a
        a, b = b, a + b

    return total_sum
i = 15
result = suma_fibonachi(i)
print(f"Сума перших {i} чисел Фібоначчі: {result}")