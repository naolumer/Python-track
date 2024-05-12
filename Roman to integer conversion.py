s = '()]]'

if len(s)%2!=0:
    return False

elif len(s)%2==0:
    i=0
    while i<len(s):
        if i< len(s)-1 and s[i]==s[i+1]:
            return True  
            i+=1
        else:
            return False
        
        
        
        
     

    

    