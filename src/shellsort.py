from datetime import datetime
startTime = datetime.now()


def shellSort(numeroarray):
    gap = len(numeroarray) // 2
    print("-------Gap on", gap)
    while gap > 0:

        for i in range(gap, len(numeroarray)):
            temp = numeroarray[i]
            j = i
            print(numeroarray)

            while j >= gap and numeroarray[j - gap] > temp:
                print(numeroarray, "Vaihdetaan luvut",
                      numeroarray[j], "ja", numeroarray[j-gap], "päittäin")
                numeroarray[j] = numeroarray[j - gap]
                j = j-gap
            numeroarray[j] = temp

        gap = gap//2
        print("-------Gap on", gap)


numeroarray = [5, 2, 6, 3, 1, 0, 4]

shellSort(numeroarray)
time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
