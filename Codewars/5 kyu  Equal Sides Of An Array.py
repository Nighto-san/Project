def find_even_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == total_sum - left_sum - arr[i]:
            return i
        left_sum += arr[i]

    return -1




print(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
print(find_even_index([1, 100, 50, -51, 1, 1]), 1, )
print(find_even_index([1, 2, 3, 4, 5, 6]), -1)
print(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
print(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)