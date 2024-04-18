def remove_duplicates(arr):
   
    if not arr:
        return 0

    k = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[k]:
            k += 1
            arr[k] = arr[i]

    return k + 1

arr = list(map(int, input("Enter a sorted array of integers separated by space: ").split()))

new_length = remove_duplicates(arr)

print("New array:", arr[:new_length])
print("New length:", new_length)
