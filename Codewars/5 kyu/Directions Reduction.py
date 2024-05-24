def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for direction in arr:
        if result and result[-1] == opposites[direction]:
            result.pop()
        else:
            result.append(direction)
    return result










print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]),"       " ,['WEST'])