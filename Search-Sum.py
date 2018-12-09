#lose

def search_sum(List,x):
    for i in range(0,len(List)):
        a=x-List[i]
        head,tail=0,len(List)
        while head<tail:
            mid=(head+tail)//2
            if a==List[mid]:
                return "YES"
            elif a>List[mid]:
                head=mid+1
            elif a<List[mid]:
                tail=mid-1
    return "NIL"
                
test=[2,5,7,9,11,12]
print search_sum(test,15)  
    
