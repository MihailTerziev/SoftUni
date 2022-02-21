rows = int(input())
flat_matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    flat_matrix.extend(nums)

print(flat_matrix)

# for _ in range(rows):
#     nums = [int(x) for x in input().split(", ")]
#     flat_matrix.append(nums)
#
# result = []
# for i in range(len(flat_matrix)):
#     for j in range(len(flat_matrix[i])):
#         result.append(flat_matrix[i][j])
#
# print(result)
