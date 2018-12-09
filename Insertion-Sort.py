#insertion-sort

def insertion_sort(List):
    for i in range(1,len(List)):
        key=List[i]
        for j in range(i-1,-1,-1):
            if List[j]>key:
                List[j+1]=List[j]
                List[j]=key
                
test=[5,32,6,7,89,9,1,5]
insertion_sort(test)
print test  
    
