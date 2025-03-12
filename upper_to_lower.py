str=input("enter a string:")
newstr=''
i=0

while i<=len(str)-1:
    data=str[i]
    ascii=ord(data)
    if (ascii>=97 and ascii<=122):
        newascii=ascii-32
        convchar=chr(newascii)
        newstr=newstr+convchar
    elif (ascii>=65 and ascii<=90):
        newascii=ascii+32 
        convchar=chr(newascii)
        newstr=newstr+convchar
    else: 
        newstr=newstr+data
    i+=1
print(newstr)



