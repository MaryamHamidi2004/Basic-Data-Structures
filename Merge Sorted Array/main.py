def merge_sorted_arrays(num1, num2):
    
    m, n = len(num1), len(num2)
    num1.extend([0] * n)  
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1

    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1

num1 = list(map(int, input("Enter the first sorted integer array separated by space: ").split()))
num2 = list(map(int, input("Enter the second sorted integer array separated by space: ").split()))

merge_sorted_arrays(num1, num2)

print("Merged sorted array:", num1)
