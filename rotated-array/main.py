def rotate_array(arr, k):
   
    arr[:] = arr[-k:] + arr[:-k]

n = int(input("Enter the array size: "))
arr = list(map(int, input(f"Enter {n} array elements separated by space: ").split()))

k = int(input("Enter the rotation factor: "))

rotate_array(arr, k)

print("Rotated array:", arr)
