def insertsort(arr,n):
    for i in range(1,n):
        print(arr)
        for j in range(0,n):
            if(arr[i]>arr[j]):
                arr[j],arr[i] = arr[j],arr[i]
            elif(arr[i]<arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
        
    return arr

arr = [28,12,35,96,25,4,8,10]
n = len(arr)
print(insertsort(arr,n))