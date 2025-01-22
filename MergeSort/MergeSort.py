import time

start = time.time()

with open("../Wordlists/rando_1M_cela_cisla.txt", "r") as file:
    #arr = [line.rstrip() for line in file]
    arr = [int(line.rstrip()) for line in file]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

mergeSort(arr, 0, len(arr) - 1)

end = time.time() - start
print("Sorted in " + str(end) + " seconds")

with open("../Wordlists/sorted.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line) + "\n")
