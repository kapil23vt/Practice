def reverseWords(s):
    
    s = s.strip().split()
    
    low = 0
    high = len(s) - 1
    
    while low < high:
        s[low], s[high] = s[high], s[low]
        high = high - 1
        low = low + 1
    
    answer = " ".join(s)
    
    return (answer)
    
    
    

print(reverseWords("KD     is the best"))