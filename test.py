a = [1,2,3,4,5,6,7,8,9,10]

result = []

# for i in a:
#     if i%2 == 0:
#         result.append(i*3)

# print(result) 

result = [f'{i} x {j} = {i*j}' for i in range(2,10) for j in range(1,10)]

print(result)