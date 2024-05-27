def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100, 0, 0, 0, 50, 0]

    sum = 0
    for i in range(1, 7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i - 1] + (count_i % 3) * scores_single[i - 1]

    return sum