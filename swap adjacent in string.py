def swapad(s):
    a = ''
    for i in range(0,len(s),2):
        if(i < len(s)-1):
            print(i)
            a += s[i+1]
            a += s[i]

    return a


s = 'abcd'
print (swapad(s))
# In Python, strings are immutable, so you can't change their characters in-place.