import numpy as np
import pprint
import time
import sys, getopt


MAX_SNAKE_LENGTH = [1, 2, 4, 7, 13, 26, 50, 98]

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

#TODO: Dodac iteracje dla kazdego patha

def create_snake(adjacency_matrix, possible_move_matrix, size,n, start_idx):
    current_snake = [start_idx]
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


def rearrange_matrices(adj_matrix, poss_matrix):
    return None


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"n:",["length-of-word="])
    except getopt.GetoptError:
        print ('snake-in-the-box.py -n <length-of-the-word>')
        sys.exit(2)
    for opt,arg in opts:
        if opt in ("-n","--length-of-word"):
            n = int(arg)
            longest_snake_found = False
            nodes = generate_gray_code(n)
            adjacency_matrix = create_adjacency_matrix(nodes = nodes)
            move_matrix = create_possible_move_matrix(nodes = nodes)
            start = time.clock()
            end = time.clock()
            while not longest_snake_found:
                starting_idx = 0
                snake = create_snake(adjacency_matrix,move_matrix,len(nodes),n,starting_idx)
                print(snake)
                print(len(snake) == MAX_SNAKE_LENGTH[n-1])
                if len(snake) == MAX_SNAKE_LENGTH[n-1]:
                    print("LONGEST SNAKE FOUND")
                    longest_snake_found = True
                    break
                starting_idx = starting_idx + 1
             
            snake_string = [nodes[element] for element in snake]
            print(snake)
            print(snake_string)
            print(len(snake_string) - 1)
            print('Time passed {0}s'.format(end-start))

if __name__ == "__main__":
   main(sys.argv[1:])