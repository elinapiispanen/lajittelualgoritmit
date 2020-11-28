from datetime import datetime
startTime = datetime.now()


def insertionSort(numeroarray):

    for i in range(1, len(numeroarray)):

        key = numeroarray[i]

        j = i-1
        while j >= 0 and key < numeroarray[j]:
            print(numeroarray, "Luku",
                  key, "on pienempi kuin", numeroarray[j])
            numeroarray[j+1] = numeroarray[j]
            j -= 1
            print(numeroarray, "Kopioidaan luku",
                  numeroarray[j+1], "indeksiin", j+2, ",ja jos", key, "on suurempi kuin", numeroarray[j], "asetetaan se indeksiin", j+1)
        numeroarray[j+1] = key
        print(numeroarray)


numeroarray = [5, 2, 6, 3, 1, 0, 4]
insertionSort(numeroarray)
time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
