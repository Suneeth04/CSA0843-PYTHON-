column=int(input("enter the no.of columns you required:"))
row=int(input("enter the no.of rows you required:"))
print("Square dollar pattern:")
for i in range(row):
    for j in range(column):
        if(i==0 or j==0 or i==row-1 or j==column-1):
            print("$",end="$")
        else:
            print("$",end="$")
    print()

