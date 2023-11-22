H,W = map(int,input().split())
x_table = [[0]*(W+1) for _ in range(H+1)]

# for h in range(1,H+1):
#     x_table[h] = list(map(int,input().split())) 




for h in range(1, H + 1):
    line = list(map(int, input().split()))
    for w in range(1, W + 1):
        x_table[h][w] = line[w - 1]

Q = int(input())
# A = [0]*(Q+1)
# B = [0]*(Q+1)
# C = [0]*(Q+1)
# D = [0]*(Q+1)
#リストの内包表記を使うと以下のように書ける
A,B,C,D=[[0]*(Q+1) for _ in range(4)]

for j in range(1,Q+1):#クエリの入力
    A[j],B[j],C[j],D[j] = map(int,input().split())

#累積和の計算
# S = [[0*(W+1)]*(H+1)] これだと同じリストの参照を複数作成してしまうので、一つの行を変更すると全ての行が変更されてしまう。
S = [[0]*(W+1) for _ in range(H+1)] 
for h in range(1,H+1):#横方向の累積和
    for w in range(1,W+1):
        S[h][w] = S[h][w-1] + x_table[h][w]

for w in range(1,W+1):#縦方向の累積和
    for h in range(1,H+1):
        S[h][w] =S[h-1][w] + S[h][w]

for j in range(1,Q+1):
    answer = S[C[j]][D[j]] + S[A[j]-1][B[j]-1] - S[C[j]][B[j]-1] - S[A[j]-1][D[j]]
    print(answer)