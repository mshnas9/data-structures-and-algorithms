def Insert(sorted, value):
    i = 0
    while value > sorted[i]:
        i = i + 1
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i = i + 1
    sorted.append(value)


def InsertionSort(input):
    sorted = []
    sorted.append(input[0])
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted
