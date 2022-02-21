matrix = [[y for y in x.split()] for x in input().split('|')]

for sub_matrix in reversed(matrix):
    if sub_matrix:
        print(*sub_matrix, end=' ')

# sub_lists = input().split('|')
# result = []
#
# while sub_lists:
#     sub_list = sub_lists.pop().split()
#     for x in sub_list:
#         result.append(x)
#
# print(*result, sep=' ')
