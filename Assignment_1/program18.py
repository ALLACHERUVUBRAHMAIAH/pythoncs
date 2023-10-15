#18.Python program to implement binary search .
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2  
    if arr[mid] == target:
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if found:
    print(f'Target {target} found at index {mid}.')
else:
    print(f'Target {target} not found in the list.')


