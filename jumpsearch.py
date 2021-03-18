import math

def jmpsearch(arr,n,val):
    i = 0
    inc = int(math.sqrt(n))
    m = inc-1
    while(val>=arr[m]):
            i = m
            m = m + inc
    for x in range(i,m+1):
        if(val == arr[x]):
            return x
            print (x)

arr = [1,3,5,7,12,13,15,21,26]
n = len(arr)
val = 12
result = jmpsearch(arr,n,val)
print("element is found in index:",result)
