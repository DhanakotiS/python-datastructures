def search(arr,n,val):
    max = n
    min =0
    while(max>=min):
        mid = int((max+min)/2)
        if(val==arr[mid]):
            return mid
        elif(val>arr[mid]):
            min = mid+1
        else:
            max = mid-1


arr = ['1','3','5','8','12','15']
val = input("Enter the element to search: ")
n = len(arr)-1
result = search(arr,n,val)
if(result):
	print("Element is found in the location",result)
else:
	print("The Given Element is not Found")
