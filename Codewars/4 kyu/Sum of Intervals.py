def sum_of_intervals(intervals):
    res = 0
    top = float("-inf")
    for start,end in sorted(intervals):
        if top < start:
            top = start
        if top < end:
            res = res+end-top
            top =  end
    return res






sum_of_intervals([(1, 5), (6, 10)])
from test import test
funk_name = 'sum_of_intervals'
args = [[(1, 5)],
        [(1, 5), (6, 10)],
        [(1, 5), (1, 5)],
        [(1, 4), (7, 10), (3, 5)]]
expect = [4,8,4,7]
test(funk_name, args, expect)