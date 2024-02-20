#to check the given number is armstong ornot
n=int(input())
sum=n
ans=0
while n>0:
    digit=n%10
    ans=ans+digit**3
    n//=10
if ans==sum:
    print("it is armstrong num")
else:
    print("not a armstrong num")
