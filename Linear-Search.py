#Linear-Search

def linear_search(List,v):
    for i in range(0,len(List)):
        if v==List[i]:
            return i
    return "NIL"
                
test=[5,32,6,7,89,9,1,5]
print linear_search(test,5)  
    
