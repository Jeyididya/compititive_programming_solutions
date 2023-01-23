class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, array,n):
        for step in range(1, n):
            key = array[step]
            j = step - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key