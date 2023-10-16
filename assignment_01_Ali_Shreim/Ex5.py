#AliShreim Ex5
def week_strong_pass(s):
    lower,upper,has_digit,has_sp,l=False,False,False,False,False
    sp=['#','!','?','$']
    for i in s:
        if i in sp:
            has_sp=True
        if(97<= ord(i) <=122):
            lower=True
        if(65<= ord(i) <=90):
            upper=True
        if(48<= ord(i) <=57):
            has_digit=True
    con=lower and upper and has_digit and has_sp and (len(s)>=8)

    if(con):
        print( "Strong Password")
    else:
        print("Week Password")

password=input("Enter a password \n")
week_strong_pass(password)

  


