import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    return sum(state[i] != goal[i] for i in range(9) if state[i] != 0)

def solve(start):
    queue = [(h(start), 0, start, [])]
    visited = set()
    
    while queue:
        _, g, state, path = heapq.heappop(queue)
        
        if state == goal:
            return path + [state]
            
        if state in visited:
            continue
        visited.add(state)
        
        zero_idx = state.index(0)
        
        valid_moves = []
        if zero_idx >= 3: valid_moves.append(zero_idx - 3)
        if zero_idx <= 5: valid_moves.append(zero_idx + 3)
        if zero_idx % 3 != 0: valid_moves.append(zero_idx - 1)
        if zero_idx % 3 != 2: valid_moves.append(zero_idx + 1)
        
        for next_idx in valid_moves:
            new_state = list(state)
            new_state[zero_idx], new_state[next_idx] = new_state[next_idx], new_state[zero_idx]
            new_state = tuple(new_state)
            heapq.heappush(queue, (g + 1 + h(new_state), g + 1, new_state, path + [state]))

start = (1, 2, 3, 4, 5, 6, 0, 7, 8)
path = solve(start)
print(path)