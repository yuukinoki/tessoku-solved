N = int(input())

A = list(map(int,input().split()))
Q = int(input())

S = [0] * (N+1)
L = [0] * Q
R = [0] * Q 
for j in range(Q):
    L[j],R[j] = map(int,input().split())

for i in range(N):
    if A[i] == 0:
        S[i+1] = -1 + S[i]
    else:
        S[i+1] = A[i] + S[i]

for j in range(Q):
    if S[R[j]]-S[L[j]-1] > 0:
        print("win")
    elif S[R[j]]-S[L[j]-1] == 0:#L~Rの累計なのでL-1までの累積和を引く
        print("draw")
    else:
        print("lose")