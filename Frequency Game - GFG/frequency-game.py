#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    d={}
    m=100000000
    ma=0
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        m=min(d[i],m)
    for i in d:
        if d[i]==m:
            ma=max(ma,i)
    return ma


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends