s1="listen"
s2="silent"
def check(s1,s2):
    print(sorted(s1))
    print(sorted(s2))
    if(sorted(s1)==sorted(s2)):
        print("the strings are anagrams.")
    else:
        print("the strings are not anagams.")
check(s1,s2)

