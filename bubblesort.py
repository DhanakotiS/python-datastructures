def bubblesort(arr,n):
    for i in range(n):
        print(arr)
        for j in range(0,n-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # temp = arr[j+1]
                # arr[j+1] = arr[j]
                # arr[j] = temp
            else:
                pass
    
    return arr
arr = [6,5,4,3,2,1]
n = len(arr)-1
print(bubblesort(arr,n))