T = int(input()) #Tは閉店時間
N = int(input()) #Nは従業員数

L = [None] * N
R = [None] * N
for i in range(N):
    L[i],R[i] = map(int,input().split())


B = [0] * (T+1)
for n in range(N):
    B[L[n]] += 1
    B[R[n]] -= 1

Answer = [0] * (T+1)
for t in range(1,T+1):
    Answer[t] = Answer[t-1] + B[t-1]
    print(Answer[t])
    