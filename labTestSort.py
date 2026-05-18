def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Последние i элементов уже отсортированы, их не трогаем
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если обменов не было, список отсортирован
        if not swapped:
            break
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]

if __name__ == "__main__":
	print("Отсортированный список:", bubble_sort(numbers))
