print("Chương trình kiểm tra Binary Min-Heap dùng đệ quy!")


def is_heap(arr, index, length):
    left = index * 2 + 1
    right = left + 1
    if left < length and arr[index] > arr[left]:
        return False
    if right < length and arr[index] > arr[right]:
        return False

    left_ok = left > length - 1 or is_heap(arr, left, length)
    if not left_ok:
        return False
    right_ok = right > length - 1 or is_heap(arr, right, length)
    return right_ok


array = [1, 5, 3, 7, 9, 8, 4]

if is_heap(array, 0, len(array)):
    print('array is a binary min-heap')
else:
    print('array is NOT a binary min-heap')
