def answer(maze):
    h, w = len(maze), len(maze[0])

    # helper function returning passable adjacent nodes
    def get_neighbors(i, j):
        result = []
        def addpass(i, j):
            if maze[i][j] == 0:
                result.append((i, j))
        if i > 0:   addpass(i-1, j)
        if i < h-1: addpass(i+1, j)
        if j > 0:   addpass(i, j-1)
        if j < w-1: addpass(i, j+1)
        return result

    # function to return a matrix of shortest path from start_point using BFS
    def traverse_passable(i0, j0):
        dist_matrix = [[400 for _ in range(w)] for _ in range(h)] # 400 ~= inf for 20x20
        dist_matrix[i0][j0] = 1
        to_visit = [(i0, j0)] # queue of nodes to visit with distance
        while len(to_visit) > 0:
            # dequeue node
            i, j = to_visit[0]
            to_visit = to_visit[1:]
            for ni, nj in get_neighbors(i, j):
                # if neighbor has not been visited already,
                # set distance and mark for visitation
                if dist_matrix[ni][nj] == 400:
                    dist_matrix[ni][nj] = dist_matrix[i][j] + 1
                    to_visit.append((ni, nj))
        return dist_matrix

    # function to return a matrix of shortest path length resulting from removing
    # impassable nodes
    def traverse_impassable():
        result_matrix = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                # look at only impassable nodes
                if maze[i][j] == 1:
                    neighbors = get_neighbors(i, j)
                    min_en_dist = min_ex_dist = 400
                    # find the shortest sum of dist to exit and entrance
                    # among passable neighbors
                    for ni, nj in neighbors:
                        if en_dist_mat[ni][nj] < min_en_dist:
                            min_en_dist = en_dist_mat[ni][nj]
                        if ex_dist_mat[ni][nj] < min_ex_dist:
                            min_ex_dist = ex_dist_mat[ni][nj]
                    result_matrix[i][j] = min_ex_dist + min_en_dist + 1
                else:
                    result_matrix[i][j] = 400
        return result_matrix

    # step 1. get matrices of shortest distance starting from entrance and exit
    en_dist_mat = traverse_passable(0, 0)
    ex_dist_mat = traverse_passable(h-1, w-1)
    # step 2. get matrix of shortest path resulting from removing each
    # impassable node by looking at adjacent nodes in previous two matrices
    imp_dist_mat = traverse_impassable()

    # return min(shortest path with no removals, shortest path with a removal)
    return min(min([min(imp_dist_row) for imp_dist_row in imp_dist_mat]), ex_dist_mat[0][0])

# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(answer(maze))
