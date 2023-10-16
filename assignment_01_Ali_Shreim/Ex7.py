#AliShreim Ex7
import math as m
def show_stat(l):
    sum=0
    for i in l:
        sum+=i
    print("Mean: ",sum/len(l))
    l.sort()
    if len(l) % 2 == 0:
        median = (l[len(l)//2-1]+l[len(l)//2])/2
        print("The median is ", median)
    else:
        median = l[len(l)//2]
        print("The median is ", median)
    mode={}
    for i in l:
        if i in mode:
            mode[i]+=1
        else:
            mode[i]=1
    max_val=0
    max_k=0
    for key,val in mode.items():
        if val>max_val:
            max_k=key
            max_val=val
    print("Mode: ", mode[max_k])
    print("Range: ",max(l)-min(l))
    mvar=0
    mean=sum/len(l)
    for i in l:
        mvar+=((i-mean)*(i-mean))
    var=mvar/len(l)
    print("Variance: ",var)
    print("Standard Deviation: ",m.sqrt(var))

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

show_stat(l)


    

