def find_missing(sequence):
    diff = (sequence[-1] - sequence[0]) // len(sequence)
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i - 1] != diff:
            return sequence[i - 1] + diff





print(find_missing([1, 3, 5, 9, 11]))# == 7