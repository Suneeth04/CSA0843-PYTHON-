try:
    a=int(input("enter the number:"))
    if(a>0):
        l=[]
        f=0
        for i in range(1,a+1):
            if(a%i==0):
                f+=1
                l.append(i)
        print(f)
        b=int(input('N:'))
        if(b>0):
            print(l[b-1])
        else:
            raise Error
    else:
        raise Error
except:
    print('invalid')
