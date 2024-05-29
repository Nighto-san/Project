def pick_peaks(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[i]:
                    break
                elif arr[j] < arr[i]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
    return {"pos": pos, "peaks": peaks}






print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))


