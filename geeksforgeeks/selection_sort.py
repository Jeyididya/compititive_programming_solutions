#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return(min(arr[i+1:]))
    
    def selectionSort(self, arr,n):
        curr_ind = 0
        for i in range(n):
            # mi = min(arr[curr_ind:])
            # mi_i = arr.index(mi)
            # chv = arr[curr_ind]
            # arr[curr_ind] = mi
            # arr[mi_i] = chv
            # curr_ind += 1
            min_index = i
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
