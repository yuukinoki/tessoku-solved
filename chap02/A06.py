#0のインデックスから開始してあげると累積和は楽
N ,Q = map(int,input().split())
A_list = list(map(int,input().split()))

L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[j], R[j] = map(int,input().split())

S = [None] * (N + 1)
S[0] = 0
for i in range(N):
    S[i+1] = S[i] + A[i]
for i in range(Q):
    print(S[R[i]] - S[L[i] -1])




# N ,Q = map(int,input().split())
# A_list = list(map(int,input().split()))
# tmp = 0
# for i in range(N):
#     A_list[i] += tmp #現在のインデックスの来場者数に前日の累計来場者数を足す
#     tmp = A_list[i]

# answer = []
# for q in range(Q):
#     L,R = map(int,input().split()) #期間の入力
#     if L == 1:
#         answer.append(A_list[R-1])  # Lが1の場合はA_list[R-1]のみが答え
#     else:
#         answer.append(A_list[R-1] - A_list[L-2])  # Lが1より大きい場合はL-2の位置の累積和を引く

# for ans in answer:
#     print(ans)

