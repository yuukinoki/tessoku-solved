N = int(input())
A = list(map(int,input().split()))

for a1 in range(N):
    for a2 in range(N):
        for a3 in range(N):
            if A[a1]+A[a2]+A[a3] == 1000 and a1!=a2!=a3!=a1: 
                print('Yes')
                exit()

print('No')

#a1!=a2!=a3だとa1とa3が同じである可能性を排除できていない。
#atcoderの環境だとexit()を推奨していないから、フラグを使うか関数にコードをラップしてreturnを使う方法