#def globals
l = [2, 4, 9, 1, 0, 8, 6, 7, 5, 3]

#def functions
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
            if sort_list[min_pos] > sort_list[pos]:
                bubble = sort_list[min_pos]
                sort_list.pop(min_pos)
                sort_list.insert(pos + 1, bubble)
                min_pos = pos
                pos = min_pos - 1

    return sort_list


#def main

def main():
    print(bubble_sort(l))


main()
