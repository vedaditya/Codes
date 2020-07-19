#Question link : https://www.codechef.com/JULY20B/problems/CHEFSTR1

#Solution:

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    su=0
    for i in range(1,len(li)):
        su+=abs(li[i]-li[i-1])-1
    print(su)
