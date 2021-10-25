arr = [1,3,4,3,5]
arr.sort()
print(arr)

for i in range(len(arr)-1):
    if arr[i+1] == arr[i]+1:
        pass
    elif arr[i] == arr[i+1]:
        dup = arr[i+1]
    else:
        replacement_value = arr[i]+1

print("replace {} by {}".format(dup,replacement_value))
