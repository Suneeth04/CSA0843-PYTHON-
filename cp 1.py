def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b
while True:
    ch=input("enter the choise(1/2/3/4/5):")
    if ch in('1','2','3','4','5'):
             a=float(input("enter the value of a:"))
             b=float(input("enter the value of b:"))
             if ch=='1':
                 print(a,'+',b,'=',add(a,b))
             elif ch=='2':
                 print(a,'-',b,'=',sub(a,b))
             elif ch=='3':
                 print(a,'*',b,'=',mul(a,b))
             elif ch=='4':
                 print(a,'/',b,'=',div(a,b))
             elif ch=='5':
                 print(a,'**',b,'=',pow(a,b))
                 break
             else:
                 print("enter the valid choise")
             

