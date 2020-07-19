#Question link : https://www.codechef.com/JULY20B/problems/ADAKING

# solution :

for _ in range(int(input())):
    a=int(input())
    list_=[['.' for i in range(8)]for j in range(8)]
    list_[0][0]='O'
    row=a//8
    col=a%8
    if row<8:
        if row>0:
            for i in range(col,8):
                list_[row][i]='X'
        else:
            list_[row][col]='X'
        if col!=0 and row<7:
            for i in range(col+1):
                list_[row+1][i]='X'
        elif row!=7:
            for i in range(8):
                list_[row][i]='X'
    for i in list_:
        print("".join(i))
    print()
