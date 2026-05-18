import time


def measure_time(sort_function):
    """Декоратор для измерения времени выполнения сортировки."""

    def wrapper(arr):

        if not isinstance(arr, list):
            print("Ошибка: необходимо передать список")
            return []

        start_time = time.perf_counter()

        result = sort_function(arr)

        end_time = time.perf_counter()

        print(f"{sort_function.__name__} выполнился за "
              f"{end_time - start_time:.8f} секунд")

        return result

    return wrapper


@measure_time
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


@measure_time
def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":

    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Результат Bubble Sort:",
          bubble_sort(numbers.copy()))

    print("Отсортированный список вставками:",
          insertion_sort(numbers.copy()))
    x=5