from collections import Counter
import io
import operator
def domaincount():
    domain_split = '@'
    
    with io.open("easylist.txt", "r", encoding = "utf-8", errors = 'ignore') as file:
        d = dict()
        
        for line in file:
            if domain_split in line:
                
                data = line.strip().split("@")
            
                if len(data) == 2:
                    a, b = data
                    
                    if b in d:
                        d[b] += 1
                    else:
                        d[b] = 1
        
    #for key, value in d.items():
        #print(key, value)
    
    for key, value in sorted(d.items(), key=operator.itemgetter(1), reverse = True):
        print (key, value)     

domaincount()