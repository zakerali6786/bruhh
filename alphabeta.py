import math

def alpha_beta(depth, node_index, is_max, values, alpha, beta, h):
    if depth == h:
        return values[node_index]

    if is_max:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
h = int(math.log2(len(values)))

optimal_value = alpha_beta(0, 0, True, values, float('-inf'), float('inf'), h)
print(optimal_value)