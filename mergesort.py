def merge_sort(arr):
    # Base case: If the list has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)

    return sorted_arr


def merge(left, right):
    merged = []
    i = j = 0

    # Compare and merge elements from left and right sublists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the left sublist
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Append any remaining elements from the right sublist
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Example usage:
arr = [9, 5, 1, 3, 8, 4, 2, 7, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
