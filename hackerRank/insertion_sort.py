def insertion(arr):
    for i in range(1,len(arr)):
        nn=arr[i]
        j=i-1
        while j>=0 and nn< arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            print(*arr)
        arr[j+1]=nn 
    print(*arr)    

