N = int(input())
S = ''
for i in range(10):
    if N>0:
        tmp = N
        N = tmp // 2
        S = str(tmp%2) + S
    
    else:
        S = '0'+S
print(int(S))

#桁数が指定されていない場合
# N = int(input())
# S = ''
# while N>0:
#         tmp = N #商と余りを計算するために保管しておく
#         N = tmp//2 #商
#         S = str(tmp%2) + S

        
# print(int(S))