#AliShreim Ex1
def factorial(x):
    if x <0:
        return "Enter a positive number"
    elif (x==0 or x==1):
        return 1
    else:
        return x*factorial(x-1)
    
while True:
    try:
        x = int(input("Enter a integer \n"))  
        break
    except:
        print("not an integer \n")
    

print(factorial(x))

