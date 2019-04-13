lst = [[9, 3, 2, 1], [9, 8], [7], [5, 2, 4]]


def adds(lst):
    total = 0
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            total += lst[row][col]
    return total


def adds2(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total


print(adds(lst))
print(adds2(lst))
