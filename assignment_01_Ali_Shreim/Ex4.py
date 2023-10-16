#AliShreim Ex4
def even_list(x):
    eve=[]
    for i in x:
        if i%2==0:
            eve.append(i)
    return eve

l=[]
while True:
    try:
        x =int(input("Enter a integer and press 0 to stop\n"))
        if x==0:
            break
        else:
            l.append(x)
    except:
        print("x not integer \n")
print(even_list(l))