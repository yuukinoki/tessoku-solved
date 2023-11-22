#今回受け取る情報は点の個数とその座標のみなので、制約に記載されている最大値、最小値から二次配列を作る。
N = int(input())
X = [0]*(N+1)
Y = [0]*(N+1)

#点の有無を格納する二次元配列
S = [[0]*(1501) for _ in range(1501)]
for i in range(1,N+1): #座標の入力
    X[i],Y[i] = map(int,input().split()) #点の座標を受け取る
    S[X[i]][Y[i]] += 1#座標の打ち込みありなら0なら1


#個数の累積和を計算
for y in range(1,1501):
    for x in range(1,1501):
        S[x][y] += S[x-1][y]
for x in range(1,1501):
    for y in range(1,1501):
        S[x][y] += S[x][y-1]

#クエリの入力
Q = int(input())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for q in range(Q):
    a[q],b[q],c[q],d[q] = map(int,input().split())
    answer = S[c[q]][d[q]] + S[a[q]-1][b[q]-1] - S[a[q]-1][d[q]] - S[c[q]][b[q]-1]
    print(answer)

#配列の宣言の仕方
#最後まで丁寧に、a,b,c,dが配列であることを忘れていたため。