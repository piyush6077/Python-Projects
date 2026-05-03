s = "abbcd"
d = {} 

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

    d[i] = d.get(i,0) + 1
    
print(d)