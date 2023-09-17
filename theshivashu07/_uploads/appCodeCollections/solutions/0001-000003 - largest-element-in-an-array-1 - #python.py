

def getLargestElement(array,n):    
	temp,index=array[0],1    
	for i in range(n):        
		if temp<array[i]:            
			temp=array[i]            
			index=i+1    
	return index


