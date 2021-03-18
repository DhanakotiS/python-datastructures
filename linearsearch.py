def search(arr,val):
    n = len(arr)
    if val in arr:
        for i in range(0,n):
            if(val==arr[i]):
                return i
    else:
        return -1


arr = [2,8,9,7,95,1,6,71,5,7,15]
val = 95
ind = search(arr,val)
if (ind == -1):
    print('Value Not Found')
else:
    print('Value Found in Index:',ind)