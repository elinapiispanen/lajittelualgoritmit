from datetime import datetime
startTime = datetime.now()


def bubblesort(list):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numeroarray)-1):
            if numeroarray[i] > numeroarray[i+1]:
                print(numeroarray, "Luku",
                      numeroarray[i], "on suurempi kuin", numeroarray[i+1], ": Vaihdetaan paikkoja")

                numeroarray[i], numeroarray[i +
                                            1] = numeroarray[i+1], numeroarray[i]
                swapped = True
                print(numeroarray)


numeroarray = [5, 2, 6, 3, 1, 0, 4]
bubblesort(numeroarray)
time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
