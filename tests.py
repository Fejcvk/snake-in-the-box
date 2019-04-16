from solution import create_snake,generate_gray_code,create_adjacency_matrix
import time
import datetime

gray_codes = [ generate_gray_code(i) for i in range(0,7) ]


def run_test_case(n):
    matrix = create_adjacency_matrix(gray_codes[n])
    snake = create_snake(matrix,len(gray_codes[n]),n)
    return snake


def run_test():
    f = open(f"results/results_{datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')}.txt", "w+")
    for i in range(2, 6):
        f.write("**********************************************\n")
        start_of_n = time.time()
        avg_time = 0
        min_t = 1000
        max_t = 0

        for j in range(0,10000):
            start = time.time()
            run_test_case(i)
            end = time.time()
            exec_time = end - start
            avg_time += exec_time
            min_t = exec_time if exec_time < min_t else min_t
            max_t = exec_time if exec_time > max_t else max_t
        end_of_n = time.time()
        f.write(f"Test took {end_of_n-start_of_n} seconds with average time {avg_time/10000} s on 10000 calls for N = {i}\n")
        f.write(f"Maximal time of execution is equal to = {max_t}, minimal to = {min_t}\n")

    min_t = 1000
    max_t = 0
    avg_time = 0
    for j in range(1,1001):
        start = time.time()
        run_test_case(6)
        end = time.time()
        exec_time = end - start
        avg_time += exec_time
        min_t = exec_time if exec_time < min_t else min_t
        max_t = exec_time if exec_time > max_t else max_t
        print(f"Call {j-1}/1000 : Current avg time is {avg_time/j} s")
    end_of_n = time.time()
    f.write(f"Test took {end_of_n-start_of_n} seconds with average time {avg_time/1000} s on 1000 call for N = 6\n")
    f.write(f"Maximal time of execution is equal to = {max_t}, minimal to = {min_t}\n")
    f.close()


run_test()