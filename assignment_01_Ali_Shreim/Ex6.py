#AliShreim Ex6
def valid_ip(ip):
    l=ip.split(".")
    if len(l)>4 or len(l)<4:
        print("invalled IP")
        return 
    
    for i in range(len(l)-1):
        s=l[i]
        if s[0] =='0' and len(s)>1:
            print("invalled IP")
            return 
        
    for i in range(len(l)-1):
        s=l[i]
        for j in s:
            if (ord(j)<48 or ord(j)>57):
                print("invalled IP")
                return
            
    for i in range(len(l)-1):
        if int(i)<0 or int(i)>255:
            print("invalled IP")
            return
    print("The IP is valid")


ip=input("Enter an Ip: \n")
valid_ip(ip)



