import numpy as np
import time
import sys, getopt

MAX_SNAKE_LENGTH = [1, 2, 4, 7, 13, 26, 50, 98]


def get_hamming_distance(first_string, second_string):
    assert len(first_string) == len(second_string)
    return sum(c1 != c2 for c1, c2 in zip(first_string, second_string))

def generate_gray_code(len):
    codes = []
    for i in range(0, 1 << len):
        gray = i ^ (i >> 1)
        codes.append("{0:0{1}b}".format(gray, len))
    return codes


def create_adjacency_matrix(nodes):
    nodes_count = len(nodes)
    adjacency_matrix = np.zeros(shape=(nodes_count, nodes_count), dtype=np.int)

    for i in range(0, nodes_count):
        curr_node = nodes[i]
        for j in range(0, nodes_count):
            if get_hamming_distance(first_string=curr_node, second_string=nodes[j]) == 1:
                adjacency_matrix[i, j] = 1
    return adjacency_matrix


def mark_neighbours_as_unvisitable(_matrix, row=None, dest=None,path=None):
    matrix = _matrix.copy()
    if path is not None:
        for idx in range(1,len(path)):
            martk_vertices_as_unvisitable(matrix, path[idx - 1], path[idx])
    else:
        martk_vertices_as_unvisitable(matrix, row, dest)
    return matrix


def martk_vertices_as_unvisitable(matrix, row, dest):
    matrix[row, dest] = False
    matrix[dest, row] = False
    true_idxs = matrix[row].nonzero()[0]
    for idx in true_idxs:
        matrix[:, idx] = False
        matrix[idx, :] = False
    return matrix


def adapt_matrix_from_path(path, adjacency_matrix):
    blank_matrix = adjacency_matrix.astype(bool)
    if len(path) < 2:
        return blank_matrix

    blank_matrix = mark_neighbours_as_unvisitable(blank_matrix, path=path)
    return blank_matrix


def dfs(source, path, visited_array, number_of_nodes, adjacency_matrix=None, possible_move_matrix=None):
    path.append(source)
    
    if possible_move_matrix is None and adjacency_matrix is not None:
        possible_move_matrix = adapt_matrix_from_path(path, adjacency_matrix)

    visited_array[source] = True
    if not possible_move_matrix.max():
        # print(path)
        yield path.copy()
    else:
        for node in range(3, number_of_nodes):
            if possible_move_matrix[source, node]:
                if not visited_array[node]:
                    yield from dfs(
                                    node, 
                                    path, 
                                    visited_array, 
                                    number_of_nodes,
                                    possible_move_matrix=mark_neighbours_as_unvisitable(possible_move_matrix, row=source, dest=node),
                    )
    path.pop()
    visited_array[source] = False


def create_snake(adj_matrix, number_of_nodes, n):
    max_len = 0
    max_path = []
    is_visited = np.zeros(number_of_nodes, dtype=np.bool)
    for path in dfs(source=2, path=[0, 1], visited_array=is_visited, number_of_nodes=number_of_nodes,
                    adjacency_matrix=adj_matrix):
        if len(path) > max_len:
            max_len = len(path)
            print('New max len = {0}'.format(max_len - 1))
        if len(path) - 1 == MAX_SNAKE_LENGTH[n - 1]:
            return path
    return []


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["length-of-word="])
    except getopt.GetoptError:
        print('snake-in-the-box.py -n <length-of-the-word>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-n", "--length-of-word"):
            n = int(arg)
            nodes = generate_gray_code(n)
            adjacency_matrix = create_adjacency_matrix(nodes=nodes)
            start = time.clock()
            snake = create_snake(adjacency_matrix, len(nodes), n)
            end = time.clock()
            snake_string = [nodes[element] for element in snake]
            print('*****************************')
            print(snake)
            print(snake_string)
            print(len(snake_string) - 1)
            print('Time passed {0}s'.format(end - start))


if __name__ == "__main__":
    main(sys.argv[1:])
