from graphillion import GraphSet
import graphillion.tutorial as tl
import random
import math
import time
import itertools
import copy

# Given: numbers of parameter values + strength
# input: list of numbers of values for parameters
# should be in decending order
# input = [10, 7, 6, 5, 2]
# input = [10,10,4,3,3,2,2,2,2,2]
input = [10, 10, 4, 3, 3, 2, 2, 2, 2, 2, 2, 2]  
# input = [4,4,4,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2]
# 
STRENGTH = 7

universe = []
PATH_LEN = 2 * STRENGTH + (len(input) - STRENGTH)  # Calculate distance n-tuple(n=STRENGTH)
print("path length", PATH_LEN)
CANDIDATE = 5 # default = 5
LEN_INPUT = len(input)

start = time.time()
for num_testcase, value in enumerate(input):  # set universe
    for num_param in range(1, value + 1):
        universe.append((str(num_testcase + 1), (str(num_testcase + 1) + "." + str(num_param))))
        universe.append(((str(num_testcase + 1) + "." + str(num_param)), str(num_testcase + 2)))
    universe.append((str(num_testcase + 1), str(num_testcase + 2)))
print(universe)
GraphSet.set_universe(universe)

paths = GraphSet.paths(str(1), str(len(input) + 1))
tuple_paths = paths.graph_size(PATH_LEN)  # enumerate All n-tuples

# Create first test cases 
test_case = []
temp = list(range(len(input)))  
def initial(t):
    for i in range(input[t - 1]):
        temp[t - 1] = i + 1
        if(t == 1):
            for k in range(STRENGTH, len(input)):
                temp[k] = random.randint(1, input[k])
            test_case.append(copy.deepcopy(temp))  # testcase
            # print (temp)
        else:
            initial(t - 1)

initial(STRENGTH)
print("testcase", test_case)

for tc in test_case:
    cover = []
    for j in range(len(input)):
        cover.append((str(j + 1), str(j + 2)))
        cover.append((str(j + 1), str(j + 1) + "." + str(tc[j])))
        cover.append((str(j + 1) + "." + str(tc[j]), str(j + 2)))
    actual_test = GraphSet([cover])
    actual_test = tuple_paths.included(actual_test)
    tuple_paths = tuple_paths ^ actual_test
    # print (len(tuple_paths))

'''
elasped_time = time.time() - start
print("fin")
print("time={0}".format(elasped_time))
print('test_num=%d' % (len(test_case)))
'''

while len(tuple_paths) > 0:
    # choose a tuple that has not been covered yet
    uncover_tuple = tuple_paths.choice()
    # [('1', '1.1'), ('1.1', '2'), ('2', '2.1'), ('2.1', '3'), ('3', '4'), ('4', '4.2'), ('4.2', '5')]
    test_param = []
    test_candidate = []
    # print("uncover tuple:", uncover_tuple)

    test_param = [None] * LEN_INPUT
    for edge in uncover_tuple:
        if '.' in edge[1]:  # ('1', '1.1')
            para, val = edge[1].split(".")
            test_param[int(para) - 1] = int(val)
        elif '.' not in edge[0]:  # ('3', '4')
            para = edge[0]
            test_param[int(para) - 1] = None
    # print("test_param:", test_param)

    # Create test case candidates by assigning random values to parameters with no fixed values
    for j in range(CANDIDATE):
        temp = [0] * LEN_INPUT
        for index, val in enumerate(test_param):
            if val is None:
                temp[index] = random.randint(1, input[index])
            else:
                temp[index] = val
        test_candidate.append(temp)

    test_covers = []
    for cand in test_candidate:
        cover = []
        # print ("candidate:", cand)
        for i in range(1, LEN_INPUT + 1):
            cover.append((str(i), str(i+1)))
            cover.append((str(i), str(i)+"."+str(cand[i-1])))
            cover.append((str(i)+"."+str(cand[i-1]), str(i+1)))
        test_covers.append(GraphSet([cover]))

    before_len = 0
    location = 0
    for i, test_cover in enumerate(test_covers):
        cover_tuple = tuple_paths.included(test_cover)
        if(len(cover_tuple) > before_len):
            before_len = len(cover_tuple)
            actual_test = cover_tuple
            location = i

    test_case.append(test_candidate[location])
    tuple_paths = tuple_paths ^ actual_test

elasped_time = time.time() - start
print("fin")
print("time={0}".format(elasped_time))
print('test_num=%d' % (len(test_case)))
# print test_case
# for p in tuple_paths:
#   print p

'''
'''