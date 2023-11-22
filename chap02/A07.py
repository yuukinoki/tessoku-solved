D = int(input()) #日数
N = int(input()) #人数


#空リストの準備
L = [0]*N
R = [0]*N
for i in range(N):#参加者iの参加期間
    L[i],R[i] = map(int,input().split())

#前日比
B =[0] * (D+2) #1~D+1までの日数を確保、D日目の翌日が必要になる処理であるためD+1を確保
for i in range(N):#1~D+1までの前日比を格納
    B[L[i]] += 1
    B[R[i]+1] -= 1

Answer = [None] * (D+2)
Answer[0] = 0
for d in range(1,D+1):
    Answer[d] = Answer[d-1] + B[d]
    print(Answer[d])

