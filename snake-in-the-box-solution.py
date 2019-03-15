import numpy as np
import pprint
import time

def get_hamming_distance(first_string, second_string):
    distance = 0
    for i in range(0,len(first_string)):
        if first_string[i] != second_string[i]:
            distance +=1
    return distance


def generate_gray_code(len):
    codes = []
    for i in range(0, 1 << len):
        gray = i ^ (i >> 1)
        codes.append("{0:0{1}b}".format(gray, len))
    return codes


def create_adjacency_matrix(nodes):
    nodes_count = len(nodes)
    adjacency_matrix = np.zeros(shape=(nodes_count,nodes_count),dtype=np.int)
    for i in range(0,nodes_count):
        curr_node = nodes[i]
        for j in range(0, nodes_count):
            if get_hamming_distance(first_string=curr_node, second_string=nodes[j]) == 1 :
                adjacency_matrix[i,j] = 1
    return adjacency_matrix


def create_possible_move_matrix(nodes):
    nodes_count = len(nodes)
    possible_move_matirx = np.zeros(shape=(nodes_count,nodes_count), dtype=np.bool)
    for i in range(0,nodes_count):
        curr_node = nodes[i]
        for j in range(0, nodes_count):
            if get_hamming_distance(first_string=curr_node, second_string=nodes[j]) == 1 :
                possible_move_matirx[i,j] = True
    return possible_move_matirx


def mark_neighbours_as_unvisitable(matrix, row, size):
    for j in range(0,size):
        if matrix[row, j]:
            matrix[:, j] = False
            matrix[j, :] = False
    return matrix


def create_snake(adjacency_matrix, possible_move_matrix, size):
    current_snake = [0]
    print('initial_setup = \n {0}'.format(possible_move_matrix))
    print('*****************************************')
    snake_finished = False
    row = 0
    col = 0
    while not snake_finished:
        if adjacency_matrix[row,col] == 1 and possible_move_matrix[row,col]:
            current_snake.append(col)
            possible_move_matrix[row, col] = False
            possible_move_matrix[col,row] = False
            possible_move_matrix = mark_neighbours_as_unvisitable(matrix=possible_move_matrix, row=row, size=size)
            print(possible_move_matrix)
            print('*****************************************')
            row = col
            col = 0
        else:
            if row == size-1 and col == size-1:
                snake_finished = True
            elif col < size-1:
                col += 1
            else:
                row += 1
                col = 0
    return current_snake


n = 2

cube_nodes = generate_gray_code(n)

adjacency_matrix = create_adjacency_matrix(nodes = cube_nodes)
move_matrix = create_possible_move_matrix(nodes = cube_nodes)
start = time.clock()
end = time.clock()
snake = create_snake(adjacency_matrix,move_matrix,len(cube_nodes))
snake_string = [cube_nodes[element] for element in snake]
print(snake_string)
print(len(snake_string) - 1)
print('Time passed {0}s'.format(end-start))