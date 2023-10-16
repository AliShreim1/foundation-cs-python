#AliShreim Ex3
def reverseString(s):
    rev_s=""
    for i in range(len(s)-1,-1,-1):
        rev_s+=s[i]
    return rev_s


x=input("Entar a string")
print(reverseString(x))
