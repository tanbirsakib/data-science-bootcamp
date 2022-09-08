if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    


#     champ = 0
#     runner_up = -999
#     #57 57 -57 57 
#     for i in arr:
#         if i>champ:
#             runner_up = champ
#             champ = i
#         else:
#             if i>runner_up and i<champ:
#                 runner_up = i
for i in range(0, len(arr)):
    print(arr[i])
 

