import time

start = time.time()

with open("../Wordlists/sorted.txt", "r") as file:
    #arr = [line.rstrip() for line in file]
    arr = [int(line.rstrip()) for line in file]

def selectionSort(array):
    for ind in range(len(array)):
        min_index = ind

        for j in range(ind + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


selectionSort(arr)

end = time.time() - start
print("Sorted in " + str(end) + " seconds")

with open("../Wordlists/sorted.txt", "w") as txt_file:
    for line in arr:
        txt_file.write(str(line) + "\n")
