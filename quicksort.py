import random
import time

# Fungsi generate array random
def generate_random_number(ran_num):
    arr = []
    a = 900       # Ubah batas atas dari bilangan acak
    for i in range(ran_num):
        arr.append(random.randint(1, a))
    return arr

# Fungsi partition
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Fungsi Quick Sort secara Rekursif
def quickSortRecursive(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quickSortRecursive(arr, low, piv - 1)
        quickSortRecursive(arr, piv + 1, high)

# Fungsi Quick Sort secara Iteratif
def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h

n = 900           # Ubah ukuran array random di sini
arr = generate_random_number(n)

arr_recursive = arr.copy()
start_time_recursive = time.time()
quickSortRecursive(arr_recursive, 0, len(arr_recursive) - 1)
end_time_recursive = time.time()

arr_iterative = arr.copy()
start_time_iterative = time.time()
quickSortIterative(arr_iterative, 0, len(arr_iterative) - 1)
end_time_iterative = time.time()

print(f"Running time untuk algoritma Quick Sort secara Rekursif dengan {n} bilangan random: {end_time_recursive - start_time_recursive:.6f} seconds")
print(f"Running time untuk algoritma Quick Sort secara Iteratif dengan {n} bilangan random: {end_time_iterative - start_time_iterative:.6f} seconds")

# Pengujian worst case untuk berbagai nilai n
n_values = [10, 50, 100, 250, 500, 900]

if n_values > [0]:
    print("")
    print("Worst Case")

for n in n_values:
    arr_recursive = list(range(n, 0, -1))
    start_time_recursive = time.time()
    quickSortRecursive(arr_recursive, 0, len(arr_recursive) - 1)
    end_time_recursive = time.time()
    print(f"Running time untuk algoritma Quick Sort secara Rekursif dengan {n} bilangan: {end_time_recursive - start_time_recursive:.6f} seconds")

if n_values > [0]:
    print("=============================================================================================")

for n in n_values:
    arr_iterative = list(range(n, 0, -1))
    start_time_iterative = time.time()
    quickSortIterative(arr_iterative, 0, len(arr_iterative) - 1)
    end_time_iterative = time.time()
    print(f"Running time untuk algoritma Quick Sort secara Iteratif dengan {n} bilangan: {end_time_iterative - start_time_iterative:.6f} seconds")
