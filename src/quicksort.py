from datetime import datetime
startTime = datetime.now()


def partition(numeroarray, low, high):
    pivot = numeroarray[(low+high) // 2]
    print("Uusi pivot-luku on", pivot)
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while numeroarray[i] < pivot:
            i = i+1

        j -= 1
        while numeroarray[j] > pivot:
            j -= 1

        if i >= j:
            return j

        numeroarray[i], numeroarray[j] = numeroarray[j], numeroarray[i]


def quicksort(numeroarray):
    def _quicksort(items, low, high):
        if low < high:
            p = partition(items, low, high)
            print(
                numeroarray, "Siirretty pivot-lukua pienemmät arvot vasemmalle ja suuremmat oikealle")
            _quicksort(items, low, p)
            _quicksort(items, p+1, high)

    _quicksort(numeroarray, 0, len(numeroarray)-1)


numeroarray = [5, 2, 6, 3, 1, 0, 4]
print(numeroarray)
quicksort(numeroarray)
time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
