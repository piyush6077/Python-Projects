###read
"""
with open("filex.txt","r") as f:
    data = f.read()
    print(data)
"""

#readline   ---> read Firstline from the paragraph
"""
with open("filex.txt","r") as f:
    data = f.readline()
    print(data)
"""

#readlines  ---> convert all the line from the file into list ["firstline /n" , "secondline /n" , .......]
"""
with open("filex.txt","r") as f:
    data = f.readlines()
    print(data)
"""

###write
"""
with open("filex.txt","w") as f:
    f.write("why does it has to happen to me")
"""

###append    ---> we use write only but with write("/n") -- "" /n ""
"""
with open("filex.txt","a") as f:
    f.write("\nWhy does it has to be you")
"""


###File Pointer (Cursor)

#tell()   ---> current position
#seek()   ---> go to the beginning
f = open("filex.txt")
data = f.read()
print(f.tell())
print(f.seek(0))
f.close()

#"""" All should use exception handling here to be safe """"

try:
    with open("filex.txt","w") as f:
        f.write("Does it really happened")
except FileNotFoundError:
    print("File not found")