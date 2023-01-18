def insertion(lis):
    for i in range(1,len(lis)):
        n=lis[i]
        j=i-1
        while j>=0 and n< lis[j]:
            lis[j+1]=lis[j]
            j=j-1
            print(lis)
        lis[j+1]=n  
    print(lis)      

insertion([2,4,6,8,3])