pin=int(input("enter the pin"))
set_pin=12345
if(pin==set_pin):
    print("avail_amt==10000")
    avail_amt=10000
    wid_amt=int(input("enter wid_amt"))
    if(wid_amt<avail_amt):
        print("sucessfully_widrown")
    else:
        print("insufficieant")                 
else:
    print("invalid_pin")
    
    


