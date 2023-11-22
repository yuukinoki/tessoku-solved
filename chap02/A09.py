H,W,N = map(int,input().split())

S = [[0]*(W+2) for _ in range(H+2)]
#H+2にするのは、配列の範囲外にアクセスしないため
#H+1にすると、i=HのときにZ[i+1][j]にアクセスできないため
A = [0]*N
B = [0]*N
C = [0]*N
D = [0]*N
for i in range(N):
    A[i],B[i],C[i],D[i] = map(int,input().split())
    S[A[i]][B[i]] += 1
    S[A[i]][D[i]+1] -= 1
    S[C[i]+1][B[i]] -= 1
    S[C[i]+1][D[i]+1] += 1


#+1はアクセル、-1はブレーキで考える。
#横と縦は別のループで考えないとおかしくなる
Answer = [[0]*(W+2) for _ in range(H+2)]
for h in range(1,H+1):
    for w in range(1,W+1):
        Answer[h][w] = Answer[h][w-1] + S[h][w]

for w in range(1,W+1):
    for h in range(1,H+1):
        Answer[h][w] += Answer[h-1][w]

for i in range(1,H+1):
    for j in range(1,W+1):
        if j>=2:
            print(" ", end="")
        print(Answer[i][j], end="")
    print("")