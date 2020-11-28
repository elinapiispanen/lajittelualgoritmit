from datetime import datetime
startTime = datetime.now()


def selection_sort(numeroarray):

    for i in range(len(numeroarray)):

        min_i = i
        for j in range(i+1, len(numeroarray)):
            if numeroarray[min_i] > numeroarray[j]:
                min_i = j

        print(numeroarray, "Siirretään luku",
              numeroarray[min_i], "oikealle paikalle", numeroarray[i], ":n tilalle")

        numeroarray[i], numeroarray[min_i] = numeroarray[min_i], numeroarray[i]


numeroarray = [5, 2, 6, 3, 1, 0, 4]
selection_sort(numeroarray)

time = (datetime.now() - startTime)
print("Aikaa kului", time.microseconds / 1000000, "sekuntia")
