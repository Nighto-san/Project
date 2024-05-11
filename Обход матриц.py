import random

# Создаем переменные
n = 14
символы = ['*', '$']

# Создаем матрицу размером n на n, каждая ячейка инициализирована пробелом
m = [[' ' for i in range(n)] for j in range(n)]

# Заполняем матрицу случайными символами
for строка in range(n):
    for столбец in range(n):
        m[строка][столбец] = random.choice(символы)

# Выводим соседей каждой ячейки
for строка in range(n):
    for столбец in range(n):
        print(f'Соседи для ячейки {строка},{столбец}:')
        for смещение_по_строке in [-1, 0, 1]:
            for смещение_по_столбцу in [-1, 0, 1]:
                новая_строка = строка + смещение_по_строке
                новый_столбец = столбец + смещение_по_столбцу

                if 0 <= новая_строка < n and 0 <= новый_столбец < n and (смещение_по_строке, смещение_по_столбцу) != (
                0, 0):
                    print(m[новая_строка][новый_столбец], end=' ')
        print()



from collections import defaultdict

def dfs(v, visited, graph):
    visited.add(v)
    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs(neighbour, visited, graph)


def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)


    for _ in range(m):
        # добавляем ребра в граф
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        print(graph)

    # множество для хранения посещенных вершин
    visited = set()

    # запускаем dfs из вершины 1
    dfs(1, visited, graph)

    # выводим результат
    print(len(visited))
    print(' '.join(map(str, sorted(visited))))


# запуск функции
solve()


