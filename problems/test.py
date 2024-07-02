out = [0]
arr = [5, 4, 7, 9, 2, 4, 4, 5, 6]
for i in range(len(arr)-2, -1, -1):
    # print((arr[i],arr[i+1]))

    if arr[i]==arr[i+1]: # if index 1 is equal to index 2
        out.append(out[-1])
    # elif arr[i]>arr[i+1]: # if index 1 is greater than index 2
    #     out.append(out[-1]+1)
    else: # if index 1 is less than index 2
        count = 0
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
        out.append(count)

print(out[::-1])