f = open("a.txt", "r")
str = f.read()
s = ""
for x in str:
    if x == '\"':
        s = s + '\\' + x
    else:
        s = s + x
print(s)
f.close()
f = open("b.txt", "w")
f.write(s)
f.close()
