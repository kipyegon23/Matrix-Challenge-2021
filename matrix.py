def solution(arr):
    square = 1
    high = max(arr)
    l = len(arr)
    position = arr.index(high)
    m = min(l, high)
    i = m + 1
    while i >= 2:
        j = 0
        while j < l:
            sub = arr[j:j + i]
            if min(sub) >= len(sub) > square:
                square = len(sub)

            j += 1
        i -= 1

    return square
