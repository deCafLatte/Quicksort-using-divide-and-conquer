import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #pivot = arr[len(arr) // 2]
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 8, 2, 1, 9, 5, 4, 6, 7]
sorted_arr = quick_sort(arr)
print(sorted_arr)
