import time


start = time.time()

with open("../Wordlists/rando_1M_cela_cisla.txt", "r") as file:
    #arr = [line.rstrip() for line in file]
    arr = [int(line.rstrip()) for line in file]


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)



quickSort(arr, 0, len(arr) - 1)


end = time.time() - start
print("Sorted in " + str(end) + " seconds")

with open("../Wordlists/sorted.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line) + "\n")
