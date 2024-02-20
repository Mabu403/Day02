#to remove duplicates in the string
str=input()
s1=""
for i in str:
    if i not in s1:
        s1+=i
print(s1)
        
