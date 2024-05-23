def max_sequence(arr):
    if not arr or max(arr) < 0:
        print("Пустой массив или все числа отрицательные. Возвращаем 0")
        return 0
    m_sum = c_sum = 0
    for num in arr:
        print("Текущее число:", num)
        c_sum = max(0, c_sum + num)
        print("Текущая сумма:", c_sum)
        m_sum = max(m_sum, c_sum)
        print("Максимальная сумма:", m_sum)
    return m_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# should be 6: [4, -1, 2, 1]
