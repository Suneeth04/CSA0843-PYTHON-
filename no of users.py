ts=int(input("enter the total users:"))
stu=int(input("enter the staff users:"))
su=0
if ts<=0 or ts==stu :
    print("enter the total users value greater than zero or greater than student users")
else:
    nsu=(stu+(stu//3))
    su=su+(ts-nsu)
    print(su)
 
