def find_missing_number(arr):
    
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = total_sum - actual_sum
    return missing_number

n = int(input("Enter the value of n: "))

arr = []
for i in range(n-1):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)

