import math 
def count_digits(digit):
    if digit==0:
        return 0
    return 1 +count_digits(digit//10)

def find_max(list):
    if len(list==1):
        return list[0]
    first_num=list[0]
    array=list[1:]
    num=find_max(array)
    if num>first_num:
        return num
    return first_num

def nor(mat,col):
    import math
    sum=0
    count=0
    for i in mat:
        sum +=i[col]
        count=count+1
    mean=sum/count
    temp=0
    for i in mat:
        temp+=(i[col]-mean)*(i[col]-mean)
    std=math.sqrt(temp/mean)
    print(std,"\n",mean)
    return mean==0 and std==1
def count_nor(mat,col=0):
    if col>len(mat):
        return 0
    if nor(mat,col):
        return 1+count_nor(mat,col=col+1)
    return count_nor(mat,col=col+1)

print("1. Count Digits")
print("2. Find Max")
print("3.1. Count Tags")
print("3.2. Count Normalized Columns")
print("4. Exit")
print("----------------------------------")

x=float(input("Enter a choice: \n"))

if x==1:
    digit=int(input("Emter an number"))
    print(count_digits(digit))
elif x==2:
    list=[]
    while(True):
        num=int(input("Enter an number \n"))
        if num:
            list.append(num)
        else:
            break
    print(find_max(list))
elif x==3.2:
    mat=[[]]
    count_nor(mat)
elif x==4:
    exit()








 