#to print armstrong nums in a order using functions
def armstrong(n,m):
    for i in range(n,m+1):
        sum=0
        x=i
        while i>0:
            temp=i%10
            sum+=temp**3
            i//=10
        if sum==x:
            print(x)
n,m=map(int,input().split(" "))
armstrong(n,m)
            
    

    
    
