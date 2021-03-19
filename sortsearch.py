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

def binarysearch(arr,n,val):
    max = n
    min = 0
    while(max >= min):
        mid = int((max+min)/2)
        if(val == arr[mid]):
            return mid
        elif(val > arr[mid]):
            min = mid + 1
        elif(val < arr[mid]):
            max = mid - 1
        else:
            return -1

n = int(input("Enter the size of array: "))

# arr = [None]*n
# print("Enter the array elements:")
# for i in range(0,n):
#     print("Enter the",i,"th element:")
#     arr[i] = input()

arr =[]
print('Enter the array elements')
for i in range(n):
    arr.append(int(input()))
print('Given List:\n',arr)

val = int(input("Enter the element to search: "))
sortedarr = bubblesort(arr,n-1)
print('Sorted List:\n',sortedarr)
res = binarysearch(sortedarr,n,val)
if(res == -1):
    print("Element Not Found")
else:
    print("Element is Found in the index:", res)