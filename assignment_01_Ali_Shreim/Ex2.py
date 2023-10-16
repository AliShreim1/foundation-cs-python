#AliShreim Ex2
def is_divisor(x):
    div_list=[]
    for i in range(1,x+1):
        if x%i== 0:
            div_list.append(i)
    return div_list

while True:
    try:
        x =int(input("Enter a integer \n"))  
        break
    except:
        print("x not integer \n")
print(is_divisor(x))