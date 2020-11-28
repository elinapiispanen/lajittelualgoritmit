from datetime import datetime
startTime = datetime.now()


def merge_sort(numeroarray):
    if len(numeroarray) <= 1:
        return numeroarray
    print(numeroarray)
    middle = len(numeroarray) // 2
    left_list = numeroarray[:middle]
    right_list = numeroarray[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))


def merge(left_half, right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            print("Vasen lista:", left_half, "--- Oikea lista:", right_half)
            print(left_half[0], "on pienempi kuin", right_half[0])
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            print(left_half[0], "on suurempi kuin", right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
        print("Lisätään käsitellyt luvut listaan:", res, "\n")
    else:
        res = res + left_half
        print("Lisätään käsitellyt luvut listaan:", res, "\n")
    return res


numeroarray = [5, 2, 6, 3, 1, 0, 4]

merge_sort(numeroarray)

time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
