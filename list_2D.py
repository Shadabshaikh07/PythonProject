l2d = [[5, 5, 7],
       [9, 6, 4],
       [9,14, 4],
       [1, 4, 5]]
print(l2d[2][1])

#TODO
# 1. sum the rows of l2d: [17, 19, 27, 10]
# 2. sum of columns of l2d: [24, 29, 20]
# 3. sum all elements of l2d


print('--------------')

l2d = [[5, 5, 7],
        [9, 6, 4],
        [9, 14, 4],
        [1, 4, 5]
        ]
su = [sum(i) for i in l2d]
print(su)

print('--------------------')

# colsum = []
# for i in range(len(l2d)):
#     sum = 0
#     for j in range(len(l2d)):
#         sum=sum + l2d[j][i]
#     print("Sum of columns {}:".format(i+1), (sum))
#     colsum.append(sum)
#
# print(colsum)

print('---------')

import numpy as np

s_rows = np.sum(l2d, axis=1)
print(s_rows)

s_cols = np.sum(l2d, axis=0)
print(s_cols)