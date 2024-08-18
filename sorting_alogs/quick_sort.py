def partition(arr, low, high):
    pivot = arr[low]  # Take the first element as pivot
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]  # Swap pivot with right pointer
    return right

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)











