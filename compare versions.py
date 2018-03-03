def compareVersion(version1, version2):
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]
    
    print(versions1)
    print(versions2)
    sum1, sum2 = 0,0
    
    for i in range(len(versions1)):
        sum1 = 10*sum1 + versions1[i]
    for i in range(len(versions2)):
        sum2 = 10*sum1 + versions2[i] 
    
    if sum1> sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0
    


print(compareVersion("13.38", "13.37"))