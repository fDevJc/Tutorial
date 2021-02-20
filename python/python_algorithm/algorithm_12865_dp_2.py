n,k = map(int,input().split(" "))
dp = [[0] * (n+10) for _ in range(k+10)]

arr = [0]

for i in range(n):
    arr.append(tuple(int(x) for x in input().split(" ")))

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= arr[i][0]:
            dp[i][j]=max(dp[i - 1][j], (dp[i - 1][j - arr[i][0]]) + arr[i][1])
        else:
            dp[i][j] = dp[i - 1][j]


for i in range(len(dp)):
    print()
    for j in range(len(dp[i])):
        print(dp[i][j], end="    ")
