# results = []

# for x in [2, 4, 5, 6]:
#     for y in [9, 10]:
#         results.append([x, y])
# print(results)

# print([[x,y] for x in [2, 4, 5, 6]  for y in [9, 10]])

# result = []
# for x in range(10):
#     if x%3==0:
#         result.append(x)
# print(result)S

# print([y for y in range(10) if y%3==0])

# List Comprehensions in Python - Hacker Rank Solution
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     # List Comprehensions in Python - Hacker Rank Solution START
#     output = [];
#     abc = [];
#     for X in range(x+1):
#         for Y in range(y+1):
#             for Z in range(z+1):
#                 if X+Y+Z != n:
#                     abc = [X,Y,Z];
#                     # print(abc)
#                     output.append(abc);
# print(output);


#---------main cood----------#

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])