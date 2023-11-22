N,X = int(input())
a_list = list(int,input().split())

for a in a_list:
    if a == X:
        print('Yes')
        exit()

print('No')
#exit()とbreakの違い
#exit()はプログラムを終了する
#breakはループを終了する