n= int (input())
adad= [[0 for j in range (i+1)] for i in range(n)]
for i in range(n):
    adad[i][0] = 1
    adad[i][i] = 1
for i in range(2,n):
    for j in range(1,i):
        adad[i][j] = adad[i-1][j-1] + adad[i-1][j]
for i in range(n):
    for j in range(i+1):
        print(adad[i][j] , end=' ')
    print()                