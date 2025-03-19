def find_common_elements(A,B):
    return list(set(A) & set(B))
A = [1, 2, 3, 4, 5]
B= [3, 4, 5, 6, 7]

common_elements = find_common_elements(A,B)
print(common_elements)


