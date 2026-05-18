import time


def bubble_sort(arr):
    start_time = time.perf_counter()

    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    end_time = time.perf_counter()
    print(f"Bubble Sort выполнился за {end_time - start_time:.8f} секунд")

    return arr


def insertion_sort(arr):
    start_time = time.perf_counter()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.perf_counter()
    print(f"Insertion Sort выполнился за {end_time - start_time:.8f} секунд")

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]

if __name__ == "__main__":
    print("Отсортированный список пузырьком:",
          bubble_sort(numbers.copy()))

    print("Отсортированный список вставками:",
          insertion_sort(numbers.copy()))