import time

start = time.time()

with open("../Wordlists/rando_1M_cela_cisla.txt", "r") as file:
    #arr = [line.rstrip() for line in file]
    arr = [int(line.rstrip()) for line in file]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)



def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

heapSort(arr)

end = time.time() - start
print("Sorted in " + str(end) + " seconds")

with open("../Wordlists/sorted.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line) + "\n")
