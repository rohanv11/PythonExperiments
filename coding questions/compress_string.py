def compressstring(s):
    c = -1
    count = 0
    new_str = ''
    for i in range(len(s)):
        if c == -1:
            c = s[i]
            count+=1
            new_str = c
        elif c == s[i]:
            count += 1
        else:
            new_str += str(count)
            count = 1
            c = s[i]
            new_str += c
    new_str += str(count)    
    print(new_str)

x = 'abcefab'
compressstring(x)

