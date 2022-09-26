income=int(input("enter the income"))
tax=0
if(income<=150000):
    tax=0
if(income>150001 and income<=300000):
    tax=income*0.1
if(income>300001 and income<=500000):
    tax=income*0.2
if(income>500000):
    tax=income*0.3
print(tax)
