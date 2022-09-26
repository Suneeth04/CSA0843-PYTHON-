statement=input("Enter the sentence:")
string=statement.lower()
print(string)
count=0
l1=['a','e','i','o','u','A','E','I','O','U']
for i in string:
    if i in l1:
        count=count+1
print("Number of vowels in given statement is:",count)
 

