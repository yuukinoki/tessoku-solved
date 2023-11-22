N,K = map(int,input().split())







# #2枚が決まればもう一枚は決まる。
# N,K = map(int,input().split())
# count = 0
# for r in range(1,N+1):
#     for b in range(1,N+1):
#         if 1 <= K-(r+b) <= N:
#             count += 1

# print(count)


# N,K = map(int,input().split())
# count = 0
# for r in range(1,N+1):
#     for b in range(1,N+1):
#         for w in range(1,N+1):
#             if r+b+w == K:
#                 count += 1


# print(count)