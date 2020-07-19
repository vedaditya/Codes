#Question link: https://www.codechef.com/JULY20B/problems/CRDGAME

# solution:

for _ in range(int(input())):
    n=int(input())
    C,M=0,0
    for i in range(n):
        a,b=input().split()
        sum_a= sum(int(digit) for digit in a)
        sum_b= sum(int(digit) for digit in b)
        if sum_a>sum_b:
            C+=1
        elif sum_a<sum_b:
            M+=1
        else:
            C+=1
            M+=1
    if C>M:
        print(0,C)
    elif C<M :
        print(1,M)
    else:
        print(2,C)

