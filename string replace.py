def replacer(s, old, new):
    
    # string = 'The quick brown fox jusmps over the lazy dog'
    # Define your variables
    
    result = ''
    
    words = s.split()
    
    print(words)
    
    for i in range(len(words)):
        
        if words[i] == old:
            words[i] = new
            result = result + words[i]
        else:
            result = result + words[i]
        

            
    print (result)            

replacer("aa bb cc dd", "aa", "xx")