import time

start = time.time()

with open("../Wordlists/rando_1M_cela_cisla.txt", "r") as file:
    #arr = [line.rstrip() for line in file]
    arr = [int(line.rstrip()) for line in file]

def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(arr)

end = time.time() - start
print("Sorted in " + str(end) + " seconds")

with open("../Wordlists/sorted.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line) + "\n")
