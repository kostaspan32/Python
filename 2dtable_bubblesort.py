ar = [
    [1, 1, 4, 5, 6],
    [2, 3, 7, 6, 8],
    [3, 9, 0, 7, 4],
    [8, 9, 2, 3, 3],
    [1, 4, 0, 2, 6]
]

def bubble_sort(sort_list):
    cnt = -1
    for i in range(len(sort_list) - 1):
        cnt += 1
        pos = len(sort_list) - 2
        min_pos = len(sort_list) - 1
        while True:
            if pos < cnt:
                break
            while sort_list[min_pos] <= sort_list[pos]:
                if pos == cnt:
                    break
                pos -= 1
            if pos == cnt:
                if sort_list[min_pos] < sort_list[pos]:
                    bubble = sort_list[min_pos]
                    sort_list.pop(min_pos)
                    sort_list.insert(pos, bubble)
                    break
                if sort_list[min_pos] == sort_list[pos]:
                    break
            if sort_list[min_pos] > sort_list[pos]:
                bubble = sort_list[min_pos]
                sort_list.pop(min_pos)
                sort_list.insert(pos + 1, bubble)
                min_pos = pos
                pos = min_pos - 1

    return sort_list


sorted_by_row_list = []
sorted_by_col_list = []

def sort_by_row(array):
    for row in range(len(array)):
        sorted_by_row_list.append(bubble_sort(array[row]))
    return sorted_by_row_list


def sort_by_col(array):
    for col in range(len(array[0])): #only works for arrays with equal length
        new_col = []
        for _ in range(len(array)):
            new_col.append(array[_][col])
        sorted_by_col_list.append(bubble_sort(new_col))
    return sorted_by_col_list



print(sort_by_col(ar))
