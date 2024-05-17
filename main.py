from loguru import logger
logger.add('debug.log', level='DEBUG')


@logger.catch()
def pipe_fix(nums):
    return [i for i in range(nums[0],nums[-1]+1)]

print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))



