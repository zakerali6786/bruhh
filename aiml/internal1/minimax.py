import math

def minimax(depth, node_index, is_max, leaves, h):
    if depth == h:
        return leaves[node_index]
    
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, leaves, h),
            minimax(depth + 1, node_index * 2 + 1, False, leaves, h)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, leaves, h),
            minimax(depth + 1, node_index * 2 + 1, True, leaves, h)
        )

leaves = [3, 5, 2, 9, 12, 5, 23, 23]
h = int(math.log2(len(leaves)))

optimal_value = minimax(0, 0, True, leaves, h)
print(optimal_value)
