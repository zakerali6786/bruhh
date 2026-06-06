variables = ['A', 'B', 'C']
graph = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
colors = ['Red', 'Green']

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = [v for v in variables if v not in assignment][0]

    for color in colors:
        if all(assignment.get(neighbor) != color for neighbor in graph[var]):
            assignment[var] = color
            
            result = backtrack(assignment)
            if result:
                return result
                
            del assignment[var]
            
    return None

solution = backtrack({})
print(solution)