def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        leftPart=alist[:mid]
        rightPart=alist[mid:]
        mergeSort(leftPart)
        mergeSort(rightPart)    
        i=0
        j=0
        k=0
        while i<len(leftPart) and j<len(rightPart):
            if leftPart[i]<rightPart[j]:
                alist[k]=leftPart[i]
                i+=1
                k+=1
            else:
                alist[k]=rightPart[j]
                j+=1
                k+=1
        while i<len(leftPart):
            alist[k]=leftPart[i]
            i+=1
            k+=1
        while j<len(rightPart):
            alist[k]=rightPart[j]
            j+=1
            k+=1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
