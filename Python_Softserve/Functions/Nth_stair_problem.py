"""
A child is running up a staircase with n
steps and can hop either 1 step, 2 steps, or
3 steps at a time. 
Implement a method to
count how many possible ways the child
can run up the stairs.
"""


def stair_problem (n_stairs):
    # base case
    if(n_stairs == 0):
        return 1
    
    if (n_stairs < 0):
        return 0
    
    return stair_problem(n_stairs - 1) + stair_problem(n_stairs - 2) + stair_problem(n_stairs - 3)

print(stair_problem(3))

def stair_paths(n, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    # Caso base: llegó a la cima exactamente
    if n == 0:
        all_paths.append(path.copy())  # Guarda una copia del camino actual
        return

    # Caso base: si se pasa, no es válido
    if n < 0:
        return

    # Intentar saltar 1 escalón
    path.append(1)
    stair_paths(n - 1, path, all_paths)
    path.pop()

    # Intentar saltar 2 escalones
    path.append(2)
    stair_paths(n - 2, path, all_paths)
    path.pop()

    # Intentar saltar 3 escalones
    path.append(3)
    stair_paths(n - 3, path, all_paths)
    path.pop()

    return all_paths

print(stair_paths(4))