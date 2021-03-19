def selectsort(arr,n):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(arr[min_index]>arr[j]):
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]
        print(arr)
    return arr 
arr = [25,16,35,75,8,95,15]
n = len(arr)
print(selectsort(arr,n))
