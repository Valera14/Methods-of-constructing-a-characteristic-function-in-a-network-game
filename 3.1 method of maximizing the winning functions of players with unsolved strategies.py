
# coding: utf-8

# In[1]:


import numpy as np

N = 6

g = [[0, 1, 0, 0, 0, 0], 
    [1, 0, 1, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0],]



first_player_strategies = list()
second_player_strategies = list()
third_player_strategies = list()
forth_player_strategies = list()
fifth_player_strategies = list()
sixth_player_strategies = list()

first_player_strategies.append('A')
first_player_strategies.append('B')
first_player_strategies.append('C')
first_player_strategies.append('D')
first_player_strategies.append('E')
first_player_strategies.append('F')
first_player_strategies.append('G')
first_player_strategies.append('H')
first_player_strategies.append('I')
first_player_strategies.append('J')


second_player_strategies.append('A')
second_player_strategies.append('B')
second_player_strategies.append('C')
second_player_strategies.append('D')
second_player_strategies.append('E')
second_player_strategies.append('F')
second_player_strategies.append('G')
second_player_strategies.append('H')
second_player_strategies.append('I')
second_player_strategies.append('J')

third_player_strategies.append('A')
third_player_strategies.append('B')
third_player_strategies.append('C')
third_player_strategies.append('D')
third_player_strategies.append('E')
third_player_strategies.append('F')
third_player_strategies.append('G')
third_player_strategies.append('H')
third_player_strategies.append('I')
third_player_strategies.append('J')


forth_player_strategies.append('A')
forth_player_strategies.append('B')
forth_player_strategies.append('C')
forth_player_strategies.append('D')
forth_player_strategies.append('E')
forth_player_strategies.append('F')
forth_player_strategies.append('G')
forth_player_strategies.append('H')
forth_player_strategies.append('I')
forth_player_strategies.append('J')



fifth_player_strategies.append('A')
fifth_player_strategies.append('B')
fifth_player_strategies.append('C')
fifth_player_strategies.append('D')
fifth_player_strategies.append('E')
fifth_player_strategies.append('F')
fifth_player_strategies.append('G')
fifth_player_strategies.append('H')
fifth_player_strategies.append('I')
fifth_player_strategies.append('J')

sixth_player_strategies.append('A')
sixth_player_strategies.append('B')
sixth_player_strategies.append('C')
sixth_player_strategies.append('D')
sixth_player_strategies.append('E')
sixth_player_strategies.append('F')
sixth_player_strategies.append('G')
sixth_player_strategies.append('H')
sixth_player_strategies.append('I')
sixth_player_strategies.append('J')

K_function_1 = np.zeros((10, 10))

K_function_1[0][0] = 7
K_function_1[0][1] = 4
K_function_1[0][2] = 3
K_function_1[0][3] = 5
K_function_1[0][4] = 7
K_function_1[0][5] = 4
K_function_1[0][6] = 8
K_function_1[0][7] = 11
K_function_1[0][8] = 3
K_function_1[0][9] = 7

K_function_1[1][0] = 3
K_function_1[1][1] = 7
K_function_1[1][2] = 8
K_function_1[1][3] = 8
K_function_1[1][4] = 7
K_function_1[1][5] = 4
K_function_1[1][6] = 4
K_function_1[1][7] = 1
K_function_1[1][8] = 6
K_function_1[1][9] = 3

K_function_1[2][0] = 4
K_function_1[2][1] = 3
K_function_1[2][2] = 5
K_function_1[2][3] = 5
K_function_1[2][4] = 1
K_function_1[2][5] = 11
K_function_1[2][6] = 12
K_function_1[2][7] = 11
K_function_1[2][8] = 2
K_function_1[2][9] = 4


K_function_1[3][0] = 3
K_function_1[3][1] = 11
K_function_1[3][2] = 5
K_function_1[3][3] = 6
K_function_1[3][4] = 7
K_function_1[3][5] = 4
K_function_1[3][6] = 1
K_function_1[3][7] = 2
K_function_1[3][8] = 7
K_function_1[3][9] = 9


K_function_1[4][0] = 3
K_function_1[4][1] = 1
K_function_1[4][2] = 8
K_function_1[4][3] = 5
K_function_1[4][4] = 2
K_function_1[4][5] = 2
K_function_1[4][6] = 2
K_function_1[4][7] = 11
K_function_1[4][8] = 8
K_function_1[4][9] = 13

K_function_1[5][0] = 3
K_function_1[5][1] = 3
K_function_1[5][2] = 4
K_function_1[5][3] = 3
K_function_1[5][4] = 4
K_function_1[5][5] = 1
K_function_1[5][6] = 2
K_function_1[5][7] = 8
K_function_1[5][8] = 10
K_function_1[5][9] = 9

K_function_1[6][0] = 3
K_function_1[6][1] = 2
K_function_1[6][2] = 4
K_function_1[6][3] = 8
K_function_1[6][4] = 14
K_function_1[6][5] = 3
K_function_1[6][6] = 2
K_function_1[6][7] = 9
K_function_1[6][8] = 3
K_function_1[6][9] = 8

K_function_1[7][0] = 5
K_function_1[7][1] = 7
K_function_1[7][2] = 1
K_function_1[7][3] = 3
K_function_1[7][4] = 2
K_function_1[7][5] = 7
K_function_1[7][6] = 11
K_function_1[7][7] = 3
K_function_1[7][8] = 4
K_function_1[7][9] = 7

K_function_1[8][0] = 7
K_function_1[8][1] = 3
K_function_1[8][2] = 1
K_function_1[8][3] = 2
K_function_1[8][4] = 8
K_function_1[8][5] = 9
K_function_1[8][6] = 14
K_function_1[8][7] = 2
K_function_1[8][8] = 6
K_function_1[8][9] = 5

K_function_1[9][0] = 5
K_function_1[9][1] = 1
K_function_1[9][2] = 6
K_function_1[9][3] = 7
K_function_1[9][4] = 9
K_function_1[9][5] = 4
K_function_1[9][6] = 2
K_function_1[9][7] = 5
K_function_1[9][8] = 7
K_function_1[9][9] = 9
#K_function_2 = np.zeros((5, 3, 5, 7))

K_function_2 = np.zeros((10, 10, 10))

K_function_2[0][0][0] = 3
K_function_2[0][1][0] = 5
K_function_2[0][2][0] = 7
K_function_2[0][3][0] = 9
K_function_2[0][4][0] = 14
K_function_2[0][5][0] = 13
K_function_2[0][6][0] = 3
K_function_2[0][7][0] = 1
K_function_2[0][8][0] = 7
K_function_2[0][9][0] = 8

K_function_2[1][0][0] = 9
K_function_2[1][1][0] = 9
K_function_2[1][2][0] = 3
K_function_2[1][3][0] = 4
K_function_2[1][4][0] = 5
K_function_2[1][5][0] = 3
K_function_2[1][6][0] = 6
K_function_2[1][7][0] = 9
K_function_2[1][8][0] = 6
K_function_2[1][9][0] = 7

K_function_2[2][0][0] = 3
K_function_2[2][1][0] = 1
K_function_2[2][2][0] = 14
K_function_2[2][3][0] = 11
K_function_2[2][4][0] = 12
K_function_2[2][5][0] = 6
K_function_2[2][6][0] = 1
K_function_2[2][7][0] = 5
K_function_2[2][8][0] = 3
K_function_2[2][9][0] = 9


K_function_2[3][0][0] = 9
K_function_2[3][1][0] = 3
K_function_2[3][2][0] = 7
K_function_2[3][3][0] = 5
K_function_2[3][4][0] = 6
K_function_2[3][5][0] = 11
K_function_2[3][6][0] = 2
K_function_2[3][7][0] = 5
K_function_2[3][8][0] = 5
K_function_2[3][9][0] = 3


K_function_2[4][0][0] = 5
K_function_2[4][1][0] = 6
K_function_2[4][2][0] = 7
K_function_2[4][3][0] = 5
K_function_2[4][4][0] = 3
K_function_2[4][5][0] = 4
K_function_2[4][6][0] = 6
K_function_2[4][7][0] = 8
K_function_2[4][8][0] = 9
K_function_2[4][9][0] = 5

K_function_2[5][0][0] = 6
K_function_2[5][1][0] = 9
K_function_2[5][2][0] = 7
K_function_2[5][3][0] = 8
K_function_2[5][4][0] = 6
K_function_2[5][5][0] = 1
K_function_2[5][6][0] = 12
K_function_2[5][7][0] = 5
K_function_2[5][8][0] = 3
K_function_2[5][9][0] = 8

K_function_2[6][0][0] = 6
K_function_2[6][1][0] = 4
K_function_2[6][2][0] = 9
K_function_2[6][3][0] = 3
K_function_2[6][4][0] = 4
K_function_2[6][5][0] = 5
K_function_2[6][6][0] = 3
K_function_2[6][7][0] = 6
K_function_2[6][8][0] = 9
K_function_2[6][9][0] = 1

K_function_2[7][0][0] = 3
K_function_2[7][1][0] = 5
K_function_2[7][2][0] = 6
K_function_2[7][3][0] = 8
K_function_2[7][4][0] = 9
K_function_2[7][5][0] = 9
K_function_2[7][6][0] = 1
K_function_2[7][7][0] = 2
K_function_2[7][8][0] = 11
K_function_2[7][9][0] = 10

K_function_2[8][0][0] = 5
K_function_2[8][1][0] = 6
K_function_2[8][2][0] = 8
K_function_2[8][3][0] = 3
K_function_2[8][4][0] = 7
K_function_2[8][5][0] = 4
K_function_2[8][6][0] = 4
K_function_2[8][7][0] = 3
K_function_2[8][8][0] = 5
K_function_2[8][9][0] = 3

K_function_2[9][0][0] = 4
K_function_2[9][1][0] = 8
K_function_2[9][2][0] = 5
K_function_2[9][3][0] = 3
K_function_2[9][4][0] = 12
K_function_2[9][5][0] = 1
K_function_2[9][6][0] = 6
K_function_2[9][7][0] = 9
K_function_2[9][8][0] = 5
K_function_2[9][9][0] = 4


K_function_2[0][0][1] = 8
K_function_2[0][1][1] = 3
K_function_2[0][2][1] = 2
K_function_2[0][3][1] = 9
K_function_2[0][4][1] = 7
K_function_2[0][5][1] = 2
K_function_2[0][6][1] = 12
K_function_2[0][7][1] = 7
K_function_2[0][8][1] = 5
K_function_2[0][9][1] = 3

K_function_2[1][0][1] = 7
K_function_2[1][1][1] = 2
K_function_2[1][2][1] = 5
K_function_2[1][3][1] = 9
K_function_2[1][4][1] = 9
K_function_2[1][5][1] = 9
K_function_2[1][6][1] = 4
K_function_2[1][7][1] = 3
K_function_2[1][8][1] = 12
K_function_2[1][9][1] = 15

K_function_2[2][0][1] = 3
K_function_2[2][1][1] = 5
K_function_2[2][2][1] = 9
K_function_2[2][3][1] = 6
K_function_2[2][4][1] = 2
K_function_2[2][5][1] = 5
K_function_2[2][6][1] = 8
K_function_2[2][7][1] = 3
K_function_2[2][8][1] = 5
K_function_2[2][9][1] = 9


K_function_2[3][0][1] = 5
K_function_2[3][1][1] = 6
K_function_2[3][2][1] = 11
K_function_2[3][3][1] = 10
K_function_2[3][4][1] = 2
K_function_2[3][5][1] = 1
K_function_2[3][6][1] = 6
K_function_2[3][7][1] = 8
K_function_2[3][8][1] = 9
K_function_2[3][9][1] = 4


K_function_2[4][0][1] = 5
K_function_2[4][1][1] = 12
K_function_2[4][2][1] = 7
K_function_2[4][3][1] = 6
K_function_2[4][4][1] = 3
K_function_2[4][5][1] = 4
K_function_2[4][6][1] = 6
K_function_2[4][7][1] = 8
K_function_2[4][8][1] = 9
K_function_2[4][9][1] = 9

K_function_2[5][0][1] = 5
K_function_2[5][1][1] = 7
K_function_2[5][2][1] = 9
K_function_2[5][3][1] = 5
K_function_2[5][4][1] = 6
K_function_2[5][5][1] = 1
K_function_2[5][6][1] = 4
K_function_2[5][7][1] = 10
K_function_2[5][8][1] = 3
K_function_2[5][9][1] = 1

K_function_2[6][0][1] = 2
K_function_2[6][1][1] = 1
K_function_2[6][2][1] = 3
K_function_2[6][3][1] = 9
K_function_2[6][4][1] = 1
K_function_2[6][5][1] = 7
K_function_2[6][6][1] = 6
K_function_2[6][7][1] = 5
K_function_2[6][8][1] = 6
K_function_2[6][9][1] = 3

K_function_2[7][0][1] = 14
K_function_2[7][1][1] = 3
K_function_2[7][2][1] = 5
K_function_2[7][3][1] = 9
K_function_2[7][4][1] = 1
K_function_2[7][5][1] = 5
K_function_2[7][6][1] = 6
K_function_2[7][7][1] = 7
K_function_2[7][8][1] = 5
K_function_2[7][9][1] = 3

K_function_2[8][0][1] = 5
K_function_2[8][1][1] = 7
K_function_2[8][2][1] = 9
K_function_2[8][3][1] = 8
K_function_2[8][4][1] = 4
K_function_2[8][5][1] = 3
K_function_2[8][6][1] = 1
K_function_2[8][7][1] = 5
K_function_2[8][8][1] = 7
K_function_2[8][9][1] = 9

K_function_2[9][0][1] = 6
K_function_2[9][1][1] = 3
K_function_2[9][2][1] = 4
K_function_2[9][3][1] = 8
K_function_2[9][4][1] = 12
K_function_2[9][5][1] = 11
K_function_2[9][6][1] = 10
K_function_2[9][7][1] = 1
K_function_2[9][8][1] = 8
K_function_2[9][9][1] = 3
















K_function_2[0][0][2] = 7
K_function_2[0][1][2] = 2
K_function_2[0][2][2] = 8
K_function_2[0][3][2] = 3
K_function_2[0][4][2] = 12
K_function_2[0][5][2] = 3
K_function_2[0][6][2] = 7
K_function_2[0][7][2] = 2
K_function_2[0][8][2] = 1
K_function_2[0][9][2] = 5

K_function_2[1][0][2] = 5
K_function_2[1][1][2] = 5
K_function_2[1][2][2] = 3
K_function_2[1][3][2] = 6
K_function_2[1][4][2] = 12
K_function_2[1][5][2] = 13
K_function_2[1][6][2] = 14
K_function_2[1][7][2] = 5
K_function_2[1][8][2] = 3
K_function_2[1][9][2] = 4

K_function_2[2][0][2] = 3
K_function_2[2][1][2] = 5
K_function_2[2][2][2] = 9
K_function_2[2][3][2] = 7
K_function_2[2][4][2] = 12
K_function_2[2][5][2] = 3
K_function_2[2][6][2] = 2
K_function_2[2][7][2] = 9
K_function_2[2][8][2] = 13
K_function_2[2][9][2] = 8


K_function_2[3][0][2] = 7
K_function_2[3][1][2] = 9
K_function_2[3][2][2] = 12
K_function_2[3][3][2] = 5
K_function_2[3][4][2] = 9
K_function_2[3][5][2] = 7
K_function_2[3][6][2] = 12
K_function_2[3][7][2] = 3
K_function_2[3][8][2] = 8
K_function_2[3][9][2] = 5


K_function_2[4][0][2] = 8
K_function_2[4][1][2] = 4
K_function_2[4][2][2] = 3
K_function_2[4][3][2] = 7
K_function_2[4][4][2] = 6
K_function_2[4][5][2] = 13
K_function_2[4][6][2] = 4
K_function_2[4][7][2] = 7
K_function_2[4][8][2] = 4
K_function_2[4][9][2] = 6

K_function_2[5][0][2] = 7
K_function_2[5][1][2] = 9
K_function_2[5][2][2] = 5
K_function_2[5][3][2] = 8
K_function_2[5][4][2] = 3
K_function_2[5][5][2] = 2
K_function_2[5][6][2] = 1
K_function_2[5][7][2] = 5
K_function_2[5][8][2] = 7
K_function_2[5][9][2] = 3
K_function_2[6][0][2] = 5
K_function_2[6][1][2] = 4
K_function_2[6][2][2] = 11
K_function_2[6][3][2] = 10
K_function_2[6][4][2] = 14
K_function_2[6][5][2] = 7
K_function_2[6][6][2] = 3
K_function_2[6][7][2] = 6
K_function_2[6][8][2] = 5
K_function_2[6][9][2] = 7

K_function_2[7][0][2] = 9
K_function_2[7][1][2] = 3
K_function_2[7][2][2] = 5
K_function_2[7][3][2] = 9
K_function_2[7][4][2] = 7
K_function_2[7][5][2] = 5
K_function_2[7][6][2] = 6
K_function_2[7][7][2] = 8
K_function_2[7][8][2] = 9
K_function_2[7][9][2] = 5

K_function_2[8][0][2] = 3
K_function_2[8][1][2] = 7
K_function_2[8][2][2] = 9
K_function_2[8][3][2] = 3
K_function_2[8][4][2] = 7
K_function_2[8][5][2] = 4
K_function_2[8][6][2] = 9
K_function_2[8][7][2] = 5
K_function_2[8][8][2] = 3
K_function_2[8][9][2] = 6

K_function_2[9][0][2] = 4
K_function_2[9][1][2] = 6
K_function_2[9][2][2] = 4
K_function_2[9][3][2] = 5
K_function_2[9][4][2] = 8
K_function_2[9][5][2] = 2
K_function_2[9][6][2] = 1
K_function_2[9][7][2] = 3
K_function_2[9][8][2] = 4
K_function_2[9][9][2] = 6
















K_function_2[0][0][3] = 8
K_function_2[0][1][3] = 6
K_function_2[0][2][3] = 7
K_function_2[0][3][3] = 8
K_function_2[0][4][3] = 2
K_function_2[0][5][3] = 3
K_function_2[0][6][3] = 6
K_function_2[0][7][3] = 9
K_function_2[0][8][3] = 6
K_function_2[0][9][3] = 8

K_function_2[1][0][3] = 7
K_function_2[1][1][3] = 8
K_function_2[1][2][3] = 6
K_function_2[1][3][3] = 5
K_function_2[1][4][3] = 4
K_function_2[1][5][3] = 2
K_function_2[1][6][3] = 7
K_function_2[1][7][3] = 5
K_function_2[1][8][3] = 8
K_function_2[1][9][3] = 6

K_function_2[2][0][3] = 8
K_function_2[2][1][3] = 1
K_function_2[2][2][3] = 3
K_function_2[2][3][3] = 7
K_function_2[2][4][3] = 5
K_function_2[2][5][3] = 8
K_function_2[2][6][3] = 2
K_function_2[2][7][3] = 5
K_function_2[2][8][3] = 7
K_function_2[2][9][3] = 9


K_function_2[3][0][3] = 8
K_function_2[3][1][3] = 6
K_function_2[3][2][3] = 3
K_function_2[3][3][3] = 8
K_function_2[3][4][3] = 9
K_function_2[3][5][3] = 7
K_function_2[3][6][3] = 5
K_function_2[3][7][3] = 3
K_function_2[3][8][3] = 6
K_function_2[3][9][3] = 8

K_function_2[4][0][3] = 8
K_function_2[4][1][3] = 3
K_function_2[4][2][3] = 6
K_function_2[4][3][3] = 8
K_function_2[4][4][3] = 5
K_function_2[4][5][3] = 6
K_function_2[4][6][3] = 3
K_function_2[4][7][3] = 7
K_function_2[4][8][3] = 12
K_function_2[4][9][3] = 10

K_function_2[5][0][3] = 5
K_function_2[5][1][3] = 9
K_function_2[5][2][3] = 6
K_function_2[5][3][3] = 5
K_function_2[5][4][3] = 3
K_function_2[5][5][3] = 5
K_function_2[5][6][3] = 12
K_function_2[5][7][3] = 4
K_function_2[5][8][3] = 8
K_function_2[5][9][3] = 5

K_function_2[6][0][3] = 6
K_function_2[6][1][3] = 6
K_function_2[6][2][3] = 5
K_function_2[6][3][3] = 3
K_function_2[6][4][3] = 8
K_function_2[6][5][3] = 5
K_function_2[6][6][3] = 6
K_function_2[6][7][3] = 4
K_function_2[6][8][3] = 5
K_function_2[6][9][3] = 9

K_function_2[7][0][3] = 4
K_function_2[7][1][3] = 5
K_function_2[7][2][3] = 9
K_function_2[7][3][3] = 7
K_function_2[7][4][3] = 5
K_function_2[7][5][3] = 4
K_function_2[7][6][3] = 3
K_function_2[7][7][3] = 5
K_function_2[7][8][3] = 5
K_function_2[7][9][3] = 8

K_function_2[8][0][3] = 5
K_function_2[8][1][3] = 6
K_function_2[8][2][3] = 4
K_function_2[8][3][3] = 8
K_function_2[8][4][3] = 7
K_function_2[8][5][3] = 7
K_function_2[8][6][3] = 7
K_function_2[8][7][3] = 3
K_function_2[8][8][3] = 5
K_function_2[8][9][3] = 4

K_function_2[9][0][3] = 9
K_function_2[9][1][3] = 5
K_function_2[9][2][3] = 4
K_function_2[9][3][3] = 5
K_function_2[9][4][3] = 12
K_function_2[9][5][3] = 8
K_function_2[9][6][3] = 9
K_function_2[9][7][3] = 9
K_function_2[9][8][3] = 5
K_function_2[9][9][3] = 7















K_function_2[0][0][4] = 2
K_function_2[0][1][4] = 3
K_function_2[0][2][4] = 5
K_function_2[0][3][4] = 9
K_function_2[0][4][4] = 8
K_function_2[0][5][4] = 1
K_function_2[0][6][4] = 11
K_function_2[0][7][4] = 8
K_function_2[0][8][4] = 5
K_function_2[0][9][4] = 6

K_function_2[1][0][4] = 8
K_function_2[1][1][4] = 5
K_function_2[1][2][4] = 6
K_function_2[1][3][4] = 4
K_function_2[1][4][4] = 3
K_function_2[1][5][4] = 5
K_function_2[1][6][4] = 5
K_function_2[1][7][4] = 8
K_function_2[1][8][4] = 9
K_function_2[1][9][4] = 6

K_function_2[2][0][4] = 7
K_function_2[2][1][4] = 1
K_function_2[2][2][4] = 1
K_function_2[2][3][4] = 12
K_function_2[2][4][4] = 14
K_function_2[2][5][4] = 8
K_function_2[2][6][4] = 3
K_function_2[2][7][4] = 5
K_function_2[2][8][4] = 3
K_function_2[2][9][4] = 5


K_function_2[3][0][4] = 5
K_function_2[3][1][4] = 8
K_function_2[3][2][4] = 2
K_function_2[3][3][4] = 3
K_function_2[3][4][4] = 6
K_function_2[3][5][4] = 8
K_function_2[3][6][4] = 5
K_function_2[3][7][4] = 9
K_function_2[3][8][4] = 8
K_function_2[3][9][4] = 5


K_function_2[4][0][4] = 4
K_function_2[4][1][4] = 12
K_function_2[4][2][4] = 7
K_function_2[4][3][4] = 7
K_function_2[4][4][4] = 5
K_function_2[4][5][4] = 3
K_function_2[4][6][4] = 7
K_function_2[4][7][4] = 5
K_function_2[4][8][4] = 4
K_function_2[4][9][4] = 2

K_function_2[5][0][4] = 12
K_function_2[5][1][4] = 1
K_function_2[5][2][4] = 5
K_function_2[5][3][4] = 7
K_function_2[5][4][4] = 8
K_function_2[5][5][4] = 3
K_function_2[5][6][4] = 1
K_function_2[5][7][4] = 4
K_function_2[5][8][4] = 8
K_function_2[5][9][4] = 3

K_function_2[6][0][4] = 8
K_function_2[6][1][4] = 7
K_function_2[6][2][4] = 1
K_function_2[6][3][4] = 5
K_function_2[6][4][4] = 8
K_function_2[6][5][4] = 5
K_function_2[6][6][4] = 4
K_function_2[6][7][4] = 8
K_function_2[6][8][4] = 7
K_function_2[6][9][4] = 3

K_function_2[7][0][4] = 4
K_function_2[7][1][4] = 5
K_function_2[7][2][4] = 4
K_function_2[7][3][4] = 8
K_function_2[7][4][4] = 6
K_function_2[7][5][4] = 3
K_function_2[7][6][4] = 4
K_function_2[7][7][4] = 5
K_function_2[7][8][4] = 3
K_function_2[7][9][4] = 5

K_function_2[8][0][4] = 4
K_function_2[8][1][4] = 5
K_function_2[8][2][4] = 9
K_function_2[8][3][4] = 5
K_function_2[8][4][4] = 5
K_function_2[8][5][4] = 4
K_function_2[8][6][4] = 3
K_function_2[8][7][4] = 5
K_function_2[8][8][4] = 6
K_function_2[8][9][4] = 7

K_function_2[9][0][4] = 4
K_function_2[9][1][4] = 8
K_function_2[9][2][4] = 6
K_function_2[9][3][4] = 5
K_function_2[9][4][4] = 4
K_function_2[9][5][4] = 8
K_function_2[9][6][4] = 9
K_function_2[9][7][4] = 7
K_function_2[9][8][4] = 5
K_function_2[9][9][4] = 5



















K_function_2[0][0][5] = 12
K_function_2[0][1][5] = 8
K_function_2[0][2][5] = 5
K_function_2[0][3][5] = 6
K_function_2[0][4][5] = 8
K_function_2[0][5][5] = 8
K_function_2[0][6][5] = 2
K_function_2[0][7][5] = 8
K_function_2[0][8][5] = 6
K_function_2[0][9][5] = 9

K_function_2[1][0][5] = 8
K_function_2[1][1][5] = 5
K_function_2[1][2][5] = 9
K_function_2[1][3][5] = 5
K_function_2[1][4][5] = 5
K_function_2[1][5][5] = 1
K_function_2[1][6][5] = 7
K_function_2[1][7][5] = 5
K_function_2[1][8][5] = 9
K_function_2[1][9][5] = 8

K_function_2[2][0][5] = 5
K_function_2[2][1][5] = 5
K_function_2[2][2][5] = 8
K_function_2[2][3][5] = 9
K_function_2[2][4][5] = 4
K_function_2[2][5][5] = 6
K_function_2[2][6][5] = 5
K_function_2[2][7][5] = 8
K_function_2[2][8][5] = 4
K_function_2[2][9][5] = 5


K_function_2[3][0][5] = 6
K_function_2[3][1][5] = 4
K_function_2[3][2][5] = 3
K_function_2[3][3][5] = 5
K_function_2[3][4][5] = 4
K_function_2[3][5][5] = 2
K_function_2[3][6][5] = 14
K_function_2[3][7][5] = 3
K_function_2[3][8][5] = 5
K_function_2[3][9][5] = 5


K_function_2[4][0][5] = 7
K_function_2[4][1][5] = 8
K_function_2[4][2][5] = 5
K_function_2[4][3][5] = 3
K_function_2[4][4][5] = 1
K_function_2[4][5][5] = 5
K_function_2[4][6][5] = 9
K_function_2[4][7][5] = 7
K_function_2[4][8][5] = 5
K_function_2[4][9][5] = 5

K_function_2[5][0][5] = 8
K_function_2[5][1][5] = 2
K_function_2[5][2][5] = 1
K_function_2[5][3][5] = 12
K_function_2[5][4][5] = 8
K_function_2[5][5][5] = 4
K_function_2[5][6][5] = 8
K_function_2[5][7][5] = 5
K_function_2[5][8][5] = 3
K_function_2[5][9][5] = 5

K_function_2[6][0][5] = 8
K_function_2[6][1][5] = 5
K_function_2[6][2][5] = 3
K_function_2[6][3][5] = 5
K_function_2[6][4][5] = 7
K_function_2[6][5][5] = 5
K_function_2[6][6][5] = 1
K_function_2[6][7][5] = 5
K_function_2[6][8][5] = 8
K_function_2[6][9][5] = 6

K_function_2[7][0][5] = 9
K_function_2[7][1][5] = 5
K_function_2[7][2][5] = 2
K_function_2[7][3][5] = 1
K_function_2[7][4][5] = 5
K_function_2[7][5][5] = 8
K_function_2[7][6][5] = 9
K_function_2[7][7][5] = 1
K_function_2[7][8][5] = 8
K_function_2[7][9][5] = 3

K_function_2[8][0][5] = 6
K_function_2[8][1][5] = 3
K_function_2[8][2][5] = 4
K_function_2[8][3][5] = 2
K_function_2[8][4][5] = 9
K_function_2[8][5][5] = 7
K_function_2[8][6][5] = 5
K_function_2[8][7][5] = 7
K_function_2[8][8][5] = 3
K_function_2[8][9][5] = 4

K_function_2[9][0][5] = 2
K_function_2[9][1][5] = 3
K_function_2[9][2][5] = 4
K_function_2[9][3][5] = 5
K_function_2[9][4][5] = 7
K_function_2[9][5][5] = 3
K_function_2[9][6][5] = 1
K_function_2[9][7][5] = 6
K_function_2[9][8][5] = 3
K_function_2[9][9][5] = 8

















K_function_2[0][0][6] = 8
K_function_2[0][1][6] = 3
K_function_2[0][2][6] = 6
K_function_2[0][3][6] = 11
K_function_2[0][4][6] = 12
K_function_2[0][5][6] = 5
K_function_2[0][6][6] = 9
K_function_2[0][7][6] = 9
K_function_2[0][8][6] = 5
K_function_2[0][9][6] = 3

K_function_2[1][0][6] = 9
K_function_2[1][1][6] = 5
K_function_2[1][2][6] = 4
K_function_2[1][3][6] = 1
K_function_2[1][4][6] = 1
K_function_2[1][5][6] = 5
K_function_2[1][6][6] = 3
K_function_2[1][7][6] = 5
K_function_2[1][8][6] = 4
K_function_2[1][9][6] = 9

K_function_2[2][0][6] = 7
K_function_2[2][1][6] = 5
K_function_2[2][2][6] = 6
K_function_2[2][3][6] = 1
K_function_2[2][4][6] = 5
K_function_2[2][5][6] = 4
K_function_2[2][6][6] = 7
K_function_2[2][7][6] = 6
K_function_2[2][8][6] = 8
K_function_2[2][9][6] = 4


K_function_2[3][0][6] = 8
K_function_2[3][1][6] = 4
K_function_2[3][2][6] = 3
K_function_2[3][3][6] = 4
K_function_2[3][4][6] = 14
K_function_2[3][5][6] = 5
K_function_2[3][6][6] = 12
K_function_2[3][7][6] = 7
K_function_2[3][8][6] = 5
K_function_2[3][9][6] = 6


K_function_2[4][0][6] = 8
K_function_2[4][1][6] = 5
K_function_2[4][2][6] = 6
K_function_2[4][3][6] = 4
K_function_2[4][4][6] = 8
K_function_2[4][5][6] = 7
K_function_2[4][6][6] = 6
K_function_2[4][7][6] = 7
K_function_2[4][8][6] = 3
K_function_2[4][9][6] = 10

K_function_2[5][0][6] = 8
K_function_2[5][1][6] = 5
K_function_2[5][2][6] = 4
K_function_2[5][3][6] = 6
K_function_2[5][4][6] = 5
K_function_2[5][5][6] = 3
K_function_2[5][6][6] = 5
K_function_2[5][7][6] = 7
K_function_2[5][8][6] = 12
K_function_2[5][9][6] = 8

K_function_2[6][0][6] = 6
K_function_2[6][1][6] = 5
K_function_2[6][2][6] = 1
K_function_2[6][3][6] = 2
K_function_2[6][4][6] = 5
K_function_2[6][5][6] = 9
K_function_2[6][6][6] = 9
K_function_2[6][7][6] = 6
K_function_2[6][8][6] = 3
K_function_2[6][9][6] = 6

K_function_2[7][0][6] = 8
K_function_2[7][1][6] = 7
K_function_2[7][2][6] = 5
K_function_2[7][3][6] = 6
K_function_2[7][4][6] = 8
K_function_2[7][5][6] = 9
K_function_2[7][6][6] = 5
K_function_2[7][7][6] = 6
K_function_2[7][8][6] = 9
K_function_2[7][9][6] = 9

K_function_2[8][0][6] = 5
K_function_2[8][1][6] = 4
K_function_2[8][2][6] = 3
K_function_2[8][3][6] = 8
K_function_2[8][4][6] = 2
K_function_2[8][5][6] = 3
K_function_2[8][6][6] = 7
K_function_2[8][7][6] = 5
K_function_2[8][8][6] = 9
K_function_2[8][9][6] = 3

K_function_2[9][0][6] = 8
K_function_2[9][1][6] = 2
K_function_2[9][2][6] = 4
K_function_2[9][3][6] = 6
K_function_2[9][4][6] = 3
K_function_2[9][5][6] = 7
K_function_2[9][6][6] = 8
K_function_2[9][7][6] = 9
K_function_2[9][8][6] = 6
K_function_2[9][9][6] = 3


















K_function_2[0][0][7] = 8
K_function_2[0][1][7] = 5
K_function_2[0][2][7] = 6
K_function_2[0][3][7] = 7
K_function_2[0][4][7] = 8
K_function_2[0][5][7] = 4
K_function_2[0][6][7] = 3
K_function_2[0][7][7] = 14
K_function_2[0][8][7] = 7
K_function_2[0][9][7] = 5

K_function_2[1][0][7] = 6
K_function_2[1][1][7] = 12
K_function_2[1][2][7] = 4
K_function_2[1][3][7] = 8
K_function_2[1][4][7] = 3
K_function_2[1][5][7] = 5
K_function_2[1][6][7] = 9
K_function_2[1][7][7] = 7
K_function_2[1][8][7] = 5
K_function_2[1][9][7] = 6

K_function_2[2][0][7] = 8
K_function_2[2][1][7] = 4
K_function_2[2][2][7] = 3
K_function_2[2][3][7] = 6
K_function_2[2][4][7] = 4
K_function_2[2][5][7] = 9
K_function_2[2][6][7] = 2
K_function_2[2][7][7] = 8
K_function_2[2][8][7] = 6
K_function_2[2][9][7] = 3


K_function_2[3][0][7] = 9
K_function_2[3][1][7] = 7
K_function_2[3][2][7] = 3
K_function_2[3][3][7] = 7
K_function_2[3][4][7] = 5
K_function_2[3][5][7] = 6
K_function_2[3][6][7] = 3
K_function_2[3][7][7] = 6
K_function_2[3][8][7] = 8
K_function_2[3][9][7] = 9


K_function_2[4][0][7] = 8
K_function_2[4][1][7] = 5
K_function_2[4][2][7] = 1
K_function_2[4][3][7] = 3
K_function_2[4][4][7] = 5
K_function_2[4][5][7] = 8
K_function_2[4][6][7] = 6
K_function_2[4][7][7] = 8
K_function_2[4][8][7] = 7
K_function_2[4][9][7] = 6

K_function_2[5][0][7] = 9
K_function_2[5][1][7] = 7
K_function_2[5][2][7] = 5
K_function_2[5][3][7] = 6
K_function_2[5][4][7] = 8
K_function_2[5][5][7] = 5
K_function_2[5][6][7] = 3
K_function_2[5][7][7] = 6
K_function_2[5][8][7] = 7
K_function_2[5][9][7] = 8

K_function_2[6][0][7] = 5
K_function_2[6][1][7] = 4
K_function_2[6][2][7] = 6
K_function_2[6][3][7] = 3
K_function_2[6][4][7] = 7
K_function_2[6][5][7] = 5
K_function_2[6][6][7] = 8
K_function_2[6][7][7] = 6
K_function_2[6][8][7] = 7
K_function_2[6][9][7] = 2

K_function_2[7][0][7] = 7
K_function_2[7][1][7] = 5
K_function_2[7][2][7] = 3
K_function_2[7][3][7] = 7
K_function_2[7][4][7] = 5
K_function_2[7][5][7] = 6
K_function_2[7][6][7] = 8
K_function_2[7][7][7] = 9
K_function_2[7][8][7] = 8
K_function_2[7][9][7] = 3

K_function_2[8][0][7] = 3
K_function_2[8][1][7] = 4
K_function_2[8][2][7] = 13
K_function_2[8][3][7] = 3
K_function_2[8][4][7] = 6
K_function_2[8][5][7] = 7
K_function_2[8][6][7] = 5
K_function_2[8][7][7] = 3
K_function_2[8][8][7] = 9
K_function_2[8][9][7] = 9

K_function_2[9][0][7] = 7
K_function_2[9][1][7] = 8
K_function_2[9][2][7] = 8
K_function_2[9][3][7] = 2
K_function_2[9][4][7] = 3
K_function_2[9][5][7] = 5
K_function_2[9][6][7] = 7
K_function_2[9][7][7] = 3
K_function_2[9][8][7] = 5
K_function_2[9][9][7] = 4














K_function_2[0][0][8] = 4
K_function_2[0][1][8] = 6
K_function_2[0][2][8] = 8
K_function_2[0][3][8] = 3
K_function_2[0][4][8] = 5
K_function_2[0][5][8] = 9
K_function_2[0][6][8] = 4
K_function_2[0][7][8] = 3
K_function_2[0][8][8] = 9
K_function_2[0][9][8] = 2

K_function_2[1][0][8] = 5
K_function_2[1][1][8] = 4
K_function_2[1][2][8] = 7
K_function_2[1][3][8] = 4
K_function_2[1][4][8] = 5
K_function_2[1][5][8] = 3
K_function_2[1][6][8] = 2
K_function_2[1][7][8] = 3
K_function_2[1][8][8] = 9
K_function_2[1][9][8] = 8

K_function_2[2][0][8] = 6
K_function_2[2][1][8] = 3
K_function_2[2][2][8] = 4
K_function_2[2][3][8] = 6
K_function_2[2][4][8] = 4
K_function_2[2][5][8] = 3
K_function_2[2][6][8] = 5
K_function_2[2][7][8] = 6
K_function_2[2][8][8] = 3
K_function_2[2][9][8] = 5


K_function_2[3][0][8] = 7
K_function_2[3][1][8] = 9
K_function_2[3][2][8] = 6
K_function_2[3][3][8] = 3
K_function_2[3][4][8] = 12
K_function_2[3][5][8] = 5
K_function_2[3][6][8] = 6
K_function_2[3][7][8] = 7
K_function_2[3][8][8] = 8
K_function_2[3][9][8] = 9


K_function_2[4][0][8] = 8
K_function_2[4][1][8] = 2
K_function_2[4][2][8] = 3
K_function_2[4][3][8] = 6
K_function_2[4][4][8] = 9
K_function_2[4][5][8] = 6
K_function_2[4][6][8] = 8
K_function_2[4][7][8] = 7
K_function_2[4][8][8] = 3
K_function_2[4][9][8] = 5

K_function_2[5][0][8] = 5
K_function_2[5][1][8] = 6
K_function_2[5][2][8] = 7
K_function_2[5][3][8] = 6
K_function_2[5][4][8] = 5
K_function_2[5][5][8] = 3
K_function_2[5][6][8] = 5
K_function_2[5][7][8] = 7
K_function_2[5][8][8] = 6
K_function_2[5][9][8] = 9

K_function_2[6][0][8] = 6
K_function_2[6][1][8] = 5
K_function_2[6][2][8] = 3
K_function_2[6][3][8] = 7
K_function_2[6][4][8] = 9
K_function_2[6][5][8] = 5
K_function_2[6][6][8] = 5
K_function_2[6][7][8] = 7
K_function_2[6][8][8] = 6
K_function_2[6][9][8] = 7

K_function_2[7][0][8] = 3
K_function_2[7][1][8] = 3
K_function_2[7][2][8] = 5
K_function_2[7][3][8] = 8
K_function_2[7][4][8] = 9
K_function_2[7][5][8] = 4
K_function_2[7][6][8] = 5
K_function_2[7][7][8] = 1
K_function_2[7][8][8] = 5
K_function_2[7][9][8] = 8

K_function_2[8][0][8] = 9
K_function_2[8][1][8] = 6
K_function_2[8][2][8] = 7
K_function_2[8][3][8] = 3
K_function_2[8][4][8] = 7
K_function_2[8][5][8] = 3
K_function_2[8][6][8] = 7
K_function_2[8][7][8] = 5
K_function_2[8][8][8] = 8
K_function_2[8][9][8] = 6

K_function_2[9][0][8] = 8
K_function_2[9][1][8] = 6
K_function_2[9][2][8] = 9
K_function_2[9][3][8] = 7
K_function_2[9][4][8] = 9
K_function_2[9][5][8] = 3
K_function_2[9][6][8] = 1
K_function_2[9][7][8] = 2
K_function_2[9][8][8] = 5
K_function_2[9][9][8] = 7












K_function_2[0][0][9] = 3
K_function_2[0][1][9] = 6
K_function_2[0][2][9] = 9
K_function_2[0][3][9] = 5
K_function_2[0][4][9] = 7
K_function_2[0][5][9] = 6
K_function_2[0][6][9] = 9
K_function_2[0][7][9] = 7
K_function_2[0][8][9] = 5
K_function_2[0][9][9] = 2

K_function_2[1][0][9] = 4
K_function_2[1][1][9] = 8
K_function_2[1][2][9] = 8
K_function_2[1][3][9] = 3
K_function_2[1][4][9] = 5
K_function_2[1][5][9] = 1
K_function_2[1][6][9] = 2
K_function_2[1][7][9] = 3
K_function_2[1][8][9] = 3
K_function_2[1][9][9] = 5

K_function_2[2][0][9] = 3
K_function_2[2][1][9] = 1
K_function_2[2][2][9] = 8
K_function_2[2][3][9] = 9
K_function_2[2][4][9] = 4
K_function_2[2][5][9] = 6
K_function_2[2][6][9] = 3
K_function_2[2][7][9] = 6
K_function_2[2][8][9] = 8
K_function_2[2][9][9] = 2


K_function_2[3][0][9] = 5
K_function_2[3][1][9] = 9
K_function_2[3][2][9] = 1
K_function_2[3][3][9] = 3
K_function_2[3][4][9] = 8
K_function_2[3][5][9] = 5
K_function_2[3][6][9] = 7
K_function_2[3][7][9] = 3
K_function_2[3][8][9] = 3
K_function_2[3][9][9] = 6


K_function_2[4][0][9] = 5
K_function_2[4][1][9] = 4
K_function_2[4][2][9] = 3
K_function_2[4][3][9] = 9
K_function_2[4][4][9] = 5
K_function_2[4][5][9] = 6
K_function_2[4][6][9] = 7
K_function_2[4][7][9] = 8
K_function_2[4][8][9] = 3
K_function_2[4][9][9] = 2

K_function_2[5][0][9] = 3
K_function_2[5][1][9] = 5
K_function_2[5][2][9] = 4
K_function_2[5][3][9] = 8
K_function_2[5][4][9] = 5
K_function_2[5][5][9] = 3
K_function_2[5][6][9] = 5
K_function_2[5][7][9] = 9
K_function_2[5][8][9] = 9
K_function_2[5][9][9] = 3

K_function_2[6][0][9] = 7
K_function_2[6][1][9] = 5
K_function_2[6][2][9] = 8
K_function_2[6][3][9] = 9
K_function_2[6][4][9] = 3
K_function_2[6][5][9] = 5
K_function_2[6][6][9] = 9
K_function_2[6][7][9] = 9
K_function_2[6][8][9] = 5
K_function_2[6][9][9] = 7

K_function_2[7][0][9] = 9
K_function_2[7][1][9] = 2
K_function_2[7][2][9] = 3
K_function_2[7][3][9] = 5
K_function_2[7][4][9] = 6
K_function_2[7][5][9] = 8
K_function_2[7][6][9] = 2
K_function_2[7][7][9] = 6
K_function_2[7][8][9] = 8
K_function_2[7][9][9] = 9

K_function_2[8][0][9] = 5
K_function_2[8][1][9] = 1
K_function_2[8][2][9] = 7
K_function_2[8][3][9] = 8
K_function_2[8][4][9] = 3
K_function_2[8][5][9] = 5
K_function_2[8][6][9] = 7
K_function_2[8][7][9] = 5
K_function_2[8][8][9] = 8
K_function_2[8][9][9] = 9

K_function_2[9][0][9] = 9
K_function_2[9][1][9] = 3
K_function_2[9][2][9] = 7
K_function_2[9][3][9] = 8
K_function_2[9][4][9] = 12
K_function_2[9][5][9] = 3
K_function_2[9][6][9] = 5
K_function_2[9][7][9] = 4
K_function_2[9][8][9] = 9
K_function_2[9][9][9] = 5













K_function_3 = np.zeros((10, 10, 10))

K_function_3[0][0][0] = 3
K_function_3[0][1][0] = 6
K_function_3[0][2][0] = 9
K_function_3[0][3][0] = 4
K_function_3[0][4][0] = 2
K_function_3[0][5][0] = 12
K_function_3[0][6][0] = 6
K_function_3[0][7][0] = 3
K_function_3[0][8][0] = 2
K_function_3[0][9][0] = 7

K_function_3[1][0][0] = 3
K_function_3[1][1][0] = 3
K_function_3[1][2][0] = 7
K_function_3[1][3][0] = 5
K_function_3[1][4][0] = 4
K_function_3[1][5][0] = 1
K_function_3[1][6][0] = 5
K_function_3[1][7][0] = 9
K_function_3[1][8][0] = 11
K_function_3[1][9][0] = 1

K_function_3[2][0][0] = 1
K_function_3[2][1][0] = 3
K_function_3[2][2][0] = 6
K_function_3[2][3][0] = 8
K_function_3[2][4][0] = 3
K_function_3[2][5][0] = 1
K_function_3[2][6][0] = 9
K_function_3[2][7][0] = 6
K_function_3[2][8][0] = 4
K_function_3[2][9][0] = 4


K_function_3[3][0][0] = 3
K_function_3[3][1][0] = 3
K_function_3[3][2][0] = 1
K_function_3[3][3][0] = 2
K_function_3[3][4][0] = 9
K_function_3[3][5][0] = 4
K_function_3[3][6][0] = 7
K_function_3[3][7][0] = 6
K_function_3[3][8][0] = 1
K_function_3[3][9][0] = 5


K_function_3[4][0][0] = 8
K_function_3[4][1][0] = 6
K_function_3[4][2][0] = 3
K_function_3[4][3][0] = 9
K_function_3[4][4][0] = 10
K_function_3[4][5][0] = 11
K_function_3[4][6][0] = 3
K_function_3[4][7][0] = 4
K_function_3[4][8][0] = 6
K_function_3[4][9][0] = 3

K_function_3[5][0][0] = 9
K_function_3[5][1][0] = 10
K_function_3[5][2][0] = 11
K_function_3[5][3][0] = 7
K_function_3[5][4][0] = 8
K_function_3[5][5][0] = 11
K_function_3[5][6][0] = 12
K_function_3[5][7][0] = 3
K_function_3[5][8][0] = 6
K_function_3[5][9][0] = 9

K_function_3[6][0][0] = 7
K_function_3[6][1][0] = 6
K_function_3[6][2][0] = 8
K_function_3[6][3][0] = 12
K_function_3[6][4][0] = 8
K_function_3[6][5][0] = 3
K_function_3[6][6][0] = 8
K_function_3[6][7][0] = 3
K_function_3[6][8][0] = 8
K_function_3[6][9][0] = 13

K_function_3[7][0][0] = 10
K_function_3[7][1][0] = 2
K_function_3[7][2][0] = 3
K_function_3[7][3][0] = 5
K_function_3[7][4][0] = 6
K_function_3[7][5][0] = 3
K_function_3[7][6][0] = 5
K_function_3[7][7][0] = 9
K_function_3[7][8][0] = 12
K_function_3[7][9][0] = 6

K_function_3[8][0][0] = 11
K_function_3[8][1][0] = 3
K_function_3[8][2][0] = 6
K_function_3[8][3][0] = 4
K_function_3[8][4][0] = 9
K_function_3[8][5][0] = 5
K_function_3[8][6][0] = 8
K_function_3[8][7][0] = 3
K_function_3[8][8][0] = 6
K_function_3[8][9][0] = 3

K_function_3[9][0][0] = 8
K_function_3[9][1][0] = 4
K_function_3[9][2][0] = 6
K_function_3[9][3][0] = 9
K_function_3[9][4][0] = 2
K_function_3[9][5][0] = 12
K_function_3[9][6][0] = 9
K_function_3[9][7][0] = 3
K_function_3[9][8][0] = 8
K_function_3[9][9][0] = 3


K_function_3[0][0][1] = 3
K_function_3[0][1][1] = 5
K_function_3[0][2][1] = 9
K_function_3[0][3][1] = 10
K_function_3[0][4][1] = 3
K_function_3[0][5][1] = 4
K_function_3[0][6][1] = 9
K_function_3[0][7][1] = 12
K_function_3[0][8][1] = 6
K_function_3[0][9][1] = 4

K_function_3[1][0][1] = 9
K_function_3[1][1][1] = 3
K_function_3[1][2][1] = 7
K_function_3[1][3][1] = 8
K_function_3[1][4][1] = 6
K_function_3[1][5][1] = 2
K_function_3[1][6][1] = 3
K_function_3[1][7][1] = 8
K_function_3[1][8][1] = 6
K_function_3[1][9][1] = 5

K_function_3[2][0][1] = 8
K_function_3[2][1][1] = 3
K_function_3[2][2][1] = 8
K_function_3[2][3][1] = 3
K_function_3[2][4][1] = 8
K_function_3[2][5][1] = 2
K_function_3[2][6][1] = 8
K_function_3[2][7][1] = 3
K_function_3[2][8][1] = 6
K_function_3[2][9][1] = 10


K_function_3[3][0][1] = 7
K_function_3[3][1][1] = 8
K_function_3[3][2][1] = 6
K_function_3[3][3][1] = 8
K_function_3[3][4][1] = 3
K_function_3[3][5][1] = 6
K_function_3[3][6][1] = 8
K_function_3[3][7][1] = 4
K_function_3[3][8][1] = 5
K_function_3[3][9][1] = 3


K_function_3[4][0][1] = 1
K_function_3[4][1][1] = 8
K_function_3[4][2][1] = 4
K_function_3[4][3][1] = 9
K_function_3[4][4][1] = 4
K_function_3[4][5][1] = 3
K_function_3[4][6][1] = 8
K_function_3[4][7][1] = 4
K_function_3[4][8][1] = 3
K_function_3[4][9][1] = 5

K_function_3[5][0][1] = 4
K_function_3[5][1][1] = 4
K_function_3[5][2][1] = 8
K_function_3[5][3][1] = 9
K_function_3[5][4][1] = 3
K_function_3[5][5][1] = 8
K_function_3[5][6][1] = 10
K_function_3[5][7][1] = 9
K_function_3[5][8][1] = 4
K_function_3[5][9][1] = 2

K_function_3[6][0][1] = 3
K_function_3[6][1][1] = 4
K_function_3[6][2][1] = 5
K_function_3[6][3][1] = 9
K_function_3[6][4][1] = 8
K_function_3[6][5][1] = 4
K_function_3[6][6][1] = 3
K_function_3[6][7][1] = 6
K_function_3[6][8][1] = 8
K_function_3[6][9][1] = 4

K_function_3[7][0][1] = 9
K_function_3[7][1][1] = 5
K_function_3[7][2][1] = 3
K_function_3[7][3][1] = 4
K_function_3[7][4][1] = 5
K_function_3[7][5][1] = 2
K_function_3[7][6][1] = 3
K_function_3[7][7][1] = 9
K_function_3[7][8][1] = 4
K_function_3[7][9][1] = 12

K_function_3[8][0][1] = 8
K_function_3[8][1][1] = 9
K_function_3[8][2][1] = 6
K_function_3[8][3][1] = 7
K_function_3[8][4][1] = 2
K_function_3[8][5][1] = 14
K_function_3[8][6][1] = 5
K_function_3[8][7][1] = 6
K_function_3[8][8][1] = 4
K_function_3[8][9][1] = 3

K_function_3[9][0][1] = 8
K_function_3[9][1][1] = 5
K_function_3[9][2][1] = 4
K_function_3[9][3][1] = 9
K_function_3[9][4][1] = 4
K_function_3[9][5][1] = 8
K_function_3[9][6][1] = 6
K_function_3[9][7][1] = 9
K_function_3[9][8][1] = 5
K_function_3[9][9][1] = 13
















K_function_3[0][0][2] = 8
K_function_3[0][1][2] = 5
K_function_3[0][2][2] = 4
K_function_3[0][3][2] = 3
K_function_3[0][4][2] = 9
K_function_3[0][5][2] = 5
K_function_3[0][6][2] = 4
K_function_3[0][7][2] = 8
K_function_3[0][8][2] = 9
K_function_3[0][9][2] = 3

K_function_3[1][0][2] = 9
K_function_3[1][1][2] = 12
K_function_3[1][2][2] = 5
K_function_3[1][3][2] = 7
K_function_3[1][4][2] = 6
K_function_3[1][5][2] = 9
K_function_3[1][6][2] = 5
K_function_3[1][7][2] = 3
K_function_3[1][8][2] = 8
K_function_3[1][9][2] = 4

K_function_3[2][0][2] = 5
K_function_3[2][1][2] = 9
K_function_3[2][2][2] = 6
K_function_3[2][3][2] = 4
K_function_3[2][4][2] = 3
K_function_3[2][5][2] = 5
K_function_3[2][6][2] = 9
K_function_3[2][7][2] = 4
K_function_3[2][8][2] = 8
K_function_3[2][9][2] = 6


K_function_3[3][0][2] = 9
K_function_3[3][1][2] = 3
K_function_3[3][2][2] = 6
K_function_3[3][3][2] = 7
K_function_3[3][4][2] = 8
K_function_3[3][5][2] = 5
K_function_3[3][6][2] = 9
K_function_3[3][7][2] = 6
K_function_3[3][8][2] = 4
K_function_3[3][9][2] = 3


K_function_3[4][0][2] = 5
K_function_3[4][1][2] = 8
K_function_3[4][2][2] = 3
K_function_3[4][3][2] = 6
K_function_3[4][4][2] = 8
K_function_3[4][5][2] = 9
K_function_3[4][6][2] = 4
K_function_3[4][7][2] = 6
K_function_3[4][8][2] = 8
K_function_3[4][9][2] = 3

K_function_3[5][0][2] = 6
K_function_3[5][1][2] = 5
K_function_3[5][2][2] = 2
K_function_3[5][3][2] = 1
K_function_3[5][4][2] = 5
K_function_3[5][5][2] = 3
K_function_3[5][6][2] = 5
K_function_3[5][7][2] = 4
K_function_3[5][8][2] = 9
K_function_3[5][9][2] = 3
K_function_3[6][0][2] = 2
K_function_3[6][1][2] = 7
K_function_3[6][2][2] = 8
K_function_3[6][3][2] = 4
K_function_3[6][4][2] = 3
K_function_3[6][5][2] = 8
K_function_3[6][6][2] = 6
K_function_3[6][7][2] = 8
K_function_3[6][8][2] = 4
K_function_3[6][9][2] = 3

K_function_3[7][0][2] = 14
K_function_3[7][1][2] = 10
K_function_3[7][2][2] = 3
K_function_3[7][3][2] = 9
K_function_3[7][4][2] = 9
K_function_3[7][5][2] = 7
K_function_3[7][6][2] = 3
K_function_3[7][7][2] = 6
K_function_3[7][8][2] = 5
K_function_3[7][9][2] = 8

K_function_3[8][0][2] = 9
K_function_3[8][1][2] = 2
K_function_3[8][2][2] = 3
K_function_3[8][3][2] = 8
K_function_3[8][4][2] = 10
K_function_3[8][5][2] = 7
K_function_3[8][6][2] = 3
K_function_3[8][7][2] = 6
K_function_3[8][8][2] = 1
K_function_3[8][9][2] = 6

K_function_3[9][0][2] = 8
K_function_3[9][1][2] = 10
K_function_3[9][2][2] = 7
K_function_3[9][3][2] = 1
K_function_3[9][4][2] = 3
K_function_3[9][5][2] = 5
K_function_3[9][6][2] = 6
K_function_3[9][7][2] = 3
K_function_3[9][8][2] = 5
K_function_3[9][9][2] = 3
















K_function_3[0][0][3] = 5
K_function_3[0][1][3] = 8
K_function_3[0][2][3] = 3
K_function_3[0][3][3] = 7
K_function_3[0][4][3] = 6
K_function_3[0][5][3] = 4
K_function_3[0][6][3] = 9
K_function_3[0][7][3] = 5
K_function_3[0][8][3] = 3
K_function_3[0][9][3] = 12

K_function_3[1][0][3] = 6
K_function_3[1][1][3] = 7
K_function_3[1][2][3] = 4
K_function_3[1][3][3] = 8
K_function_3[1][4][3] = 12
K_function_3[1][5][3] = 11
K_function_3[1][6][3] = 3
K_function_3[1][7][3] = 10
K_function_3[1][8][3] = 9
K_function_3[1][9][3] = 2

K_function_3[2][0][3] = 3
K_function_3[2][1][3] = 5
K_function_3[2][2][3] = 6
K_function_3[2][3][3] = 9
K_function_3[2][4][3] = 7
K_function_3[2][5][3] = 5
K_function_3[2][6][3] = 3
K_function_3[2][7][3] = 10
K_function_3[2][8][3] = 12
K_function_3[2][9][3] = 11


K_function_3[3][0][3] = 14
K_function_3[3][1][3] = 9
K_function_3[3][2][3] = 3
K_function_3[3][3][3] = 4
K_function_3[3][4][3] = 9
K_function_3[3][5][3] = 8
K_function_3[3][6][3] = 6
K_function_3[3][7][3] = 8
K_function_3[3][8][3] = 3
K_function_3[3][9][3] = 9

K_function_3[4][0][3] = 12
K_function_3[4][1][3] = 5
K_function_3[4][2][3] = 4
K_function_3[4][3][3] = 6
K_function_3[4][4][3] = 9
K_function_3[4][5][3] = 7
K_function_3[4][6][3] = 5
K_function_3[4][7][3] = 2
K_function_3[4][8][3] = 3
K_function_3[4][9][3] = 9

K_function_3[5][0][3] = 8
K_function_3[5][1][3] = 2
K_function_3[5][2][3] = 11
K_function_3[5][3][3] = 8
K_function_3[5][4][3] = 2
K_function_3[5][5][3] = 3
K_function_3[5][6][3] = 7
K_function_3[5][7][3] = 5
K_function_3[5][8][3] = 6
K_function_3[5][9][3] = 6

K_function_3[6][0][3] = 2
K_function_3[6][1][3] = 2
K_function_3[6][2][3] = 3
K_function_3[6][3][3] = 3
K_function_3[6][4][3] = 8
K_function_3[6][5][3] = 1
K_function_3[6][6][3] = 9
K_function_3[6][7][3] = 9
K_function_3[6][8][3] = 8
K_function_3[6][9][3] = 3

K_function_3[7][0][3] = 4
K_function_3[7][1][3] = 8
K_function_3[7][2][3] = 9
K_function_3[7][3][3] = 10
K_function_3[7][4][3] = 3
K_function_3[7][5][3] = 4
K_function_3[7][6][3] = 5
K_function_3[7][7][3] = 9
K_function_3[7][8][3] = 3
K_function_3[7][9][3] = 5

K_function_3[8][0][3] = 8
K_function_3[8][1][3] = 6
K_function_3[8][2][3] = 5
K_function_3[8][3][3] = 2
K_function_3[8][4][3] = 3
K_function_3[8][5][3] = 11
K_function_3[8][6][3] = 2
K_function_3[8][7][3] = 3
K_function_3[8][8][3] = 7
K_function_3[8][9][3] = 2

K_function_3[9][0][3] = 3
K_function_3[9][1][3] = 3
K_function_3[9][2][3] = 5
K_function_3[9][3][3] = 9
K_function_3[9][4][3] = 8
K_function_3[9][5][3] = 7
K_function_3[9][6][3] = 5
K_function_3[9][7][3] = 2
K_function_3[9][8][3] = 3
K_function_3[9][9][3] = 9













9
K_function_3[0][0][4] = 2
K_function_3[0][1][4] = 4
K_function_3[0][2][4] = 9
K_function_3[0][3][4] = 3
K_function_3[0][4][4] = 6
K_function_3[0][5][4] = 5
K_function_3[0][6][4] = 9
K_function_3[0][7][4] = 7
K_function_3[0][8][4] = 8
K_function_3[0][9][4] = 4

K_function_3[1][0][4] = 9
K_function_3[1][1][4] = 3
K_function_3[1][2][4] = 5
K_function_3[1][3][4] = 7
K_function_3[1][4][4] = 5
K_function_3[1][5][4] = 3
K_function_3[1][6][4] = 9
K_function_3[1][7][4] = 4
K_function_3[1][8][4] = 6
K_function_3[1][9][4] = 3

K_function_3[2][0][4] = 6
K_function_3[2][1][4] = 7
K_function_3[2][2][4] = 8
K_function_3[2][3][4] = 5
K_function_3[2][4][4] = 6
K_function_3[2][5][4] = 9
K_function_3[2][6][4] = 3
K_function_3[2][7][4] = 4
K_function_3[2][8][4] = 8
K_function_3[2][9][4] = 3


K_function_3[3][0][4] = 8
K_function_3[3][1][4] = 1
K_function_3[3][2][4] = 9
K_function_3[3][3][4] = 5
K_function_3[3][4][4] = 3
K_function_3[3][5][4] = 7
K_function_3[3][6][4] = 3
K_function_3[3][7][4] = 8
K_function_3[3][8][4] = 2
K_function_3[3][9][4] = 3


K_function_3[4][0][4] = 7
K_function_3[4][1][4] = 5
K_function_3[4][2][4] = 3
K_function_3[4][3][4] = 7
K_function_3[4][4][4] = 8
K_function_3[4][5][4] = 6
K_function_3[4][6][4] = 3
K_function_3[4][7][4] = 8
K_function_3[4][8][4] = 7
K_function_3[4][9][4] = 6

K_function_3[5][0][4] = 8
K_function_3[5][1][4] = 5
K_function_3[5][2][4] = 3
K_function_3[5][3][4] = 6
K_function_3[5][4][4] = 7
K_function_3[5][5][4] = 4
K_function_3[5][6][4] = 5
K_function_3[5][7][4] = 3
K_function_3[5][8][4] = 8
K_function_3[5][9][4] = 3

K_function_3[6][0][4] = 3
K_function_3[6][1][4] = 5
K_function_3[6][2][4] = 4
K_function_3[6][3][4] = 8
K_function_3[6][4][4] = 2
K_function_3[6][5][4] = 3
K_function_3[6][6][4] = 5
K_function_3[6][7][4] = 9
K_function_3[6][8][4] = 4
K_function_3[6][9][4] = 3

K_function_3[7][0][4] = 6
K_function_3[7][1][4] = 4
K_function_3[7][2][4] = 4
K_function_3[7][3][4] = 2
K_function_3[7][4][4] = 6
K_function_3[7][5][4] = 4
K_function_3[7][6][4] = 3
K_function_3[7][7][4] = 8
K_function_3[7][8][4] = 6
K_function_3[7][9][4] = 5

K_function_3[8][0][4] = 7
K_function_3[8][1][4] = 3
K_function_3[8][2][4] = 5
K_function_3[8][3][4] = 4
K_function_3[8][4][4] = 8
K_function_3[8][5][4] = 12
K_function_3[8][6][4] = 13
K_function_3[8][7][4] = 7
K_function_3[8][8][4] = 8
K_function_3[8][9][4] = 12

K_function_3[9][0][4] = 9
K_function_3[9][1][4] = 2
K_function_3[9][2][4] = 3
K_function_3[9][3][4] = 8
K_function_3[9][4][4] = 5
K_function_3[9][5][4] = 3
K_function_3[9][6][4] = 5
K_function_3[9][7][4] = 7
K_function_3[9][8][4] = 2
K_function_3[9][9][4] = 9



















K_function_3[0][0][5] = 7
K_function_3[0][1][5] = 2
K_function_3[0][2][5] = 13
K_function_3[0][3][5] = 9
K_function_3[0][4][5] = 5
K_function_3[0][5][5] = 3
K_function_3[0][6][5] = 1
K_function_3[0][7][5] = 5
K_function_3[0][8][5] = 7
K_function_3[0][9][5] = 2

K_function_3[1][0][5] = 3
K_function_3[1][1][5] = 7
K_function_3[1][2][5] = 5
K_function_3[1][3][5] = 6
K_function_3[1][4][5] = 3
K_function_3[1][5][5] = 2
K_function_3[1][6][5] = 7
K_function_3[1][7][5] = 4
K_function_3[1][8][5] = 9
K_function_3[1][9][5] = 7

K_function_3[2][0][5] = 3
K_function_3[2][1][5] = 4
K_function_3[2][2][5] = 2
K_function_3[2][3][5] = 1
K_function_3[2][4][5] = 7
K_function_3[2][5][5] = 6
K_function_3[2][6][5] = 7
K_function_3[2][7][5] = 12
K_function_3[2][8][5] = 3
K_function_3[2][9][5] = 1


K_function_3[3][0][5] = 4
K_function_3[3][1][5] = 2
K_function_3[3][2][5] = 3
K_function_3[3][3][5] = 8
K_function_3[3][4][5] = 4
K_function_3[3][5][5] = 3
K_function_3[3][6][5] = 7
K_function_3[3][7][5] = 5
K_function_3[3][8][5] = 6
K_function_3[3][9][5] = 5


K_function_3[4][0][5] = 9
K_function_3[4][1][5] = 7
K_function_3[4][2][5] = 6
K_function_3[4][3][5] = 2
K_function_3[4][4][5] = 3
K_function_3[4][5][5] = 4
K_function_3[4][6][5] = 8
K_function_3[4][7][5] = 6
K_function_3[4][8][5] = 7
K_function_3[4][9][5] = 3

K_function_3[5][0][5] = 6
K_function_3[5][1][5] = 4
K_function_3[5][2][5] = 3
K_function_3[5][3][5] = 8
K_function_3[5][4][5] = 3
K_function_3[5][5][5] = 6
K_function_3[5][6][5] = 4
K_function_3[5][7][5] = 8
K_function_3[5][8][5] = 3
K_function_3[5][9][5] = 1

K_function_3[6][0][5] = 9
K_function_3[6][1][5] = 3
K_function_3[6][2][5] = 8
K_function_3[6][3][5] = 6
K_function_3[6][4][5] = 4
K_function_3[6][5][5] = 3
K_function_3[6][6][5] = 8
K_function_3[6][7][5] = 6
K_function_3[6][8][5] = 7
K_function_3[6][9][5] = 9

K_function_3[7][0][5] = 4
K_function_3[7][1][5] = 5
K_function_3[7][2][5] = 1
K_function_3[7][3][5] = 3
K_function_3[7][4][5] = 8
K_function_3[7][5][5] = 4
K_function_3[7][6][5] = 12
K_function_3[7][7][5] = 4
K_function_3[7][8][5] = 5
K_function_3[7][9][5] = 8

K_function_3[8][0][5] = 6
K_function_3[8][1][5] = 6
K_function_3[8][2][5] = 8
K_function_3[8][3][5] = 4
K_function_3[8][4][5] = 4
K_function_3[8][5][5] = 9
K_function_3[8][6][5] = 8
K_function_3[8][7][5] = 12
K_function_3[8][8][5] = 13
K_function_3[8][9][5] = 8

K_function_3[9][0][5] = 9
K_function_3[9][1][5] = 4
K_function_3[9][2][5] = 2
K_function_3[9][3][5] = 3
K_function_3[9][4][5] = 4
K_function_3[9][5][5] = 8
K_function_3[9][6][5] = 2
K_function_3[9][7][5] = 4
K_function_3[9][8][5] = 8
K_function_3[9][9][5] = 4

















K_function_3[0][0][6] = 6
K_function_3[0][1][6] = 4
K_function_3[0][2][6] = 8
K_function_3[0][3][6] = 4
K_function_3[0][4][6] = 8
K_function_3[0][5][6] = 12
K_function_3[0][6][6] = 8
K_function_3[0][7][6] = 8
K_function_3[0][8][6] = 4
K_function_3[0][9][6] = 4

K_function_3[1][0][6] = 8
K_function_3[1][1][6] = 2
K_function_3[1][2][6] = 3
K_function_3[1][3][6] = 4
K_function_3[1][4][6] = 8
K_function_3[1][5][6] = 7
K_function_3[1][6][6] = 8
K_function_3[1][7][6] = 3
K_function_3[1][8][6] = 5
K_function_3[1][9][6] = 4

K_function_3[2][0][6] = 3
K_function_3[2][1][6] = 6
K_function_3[2][2][6] = 7
K_function_3[2][3][6] = 8
K_function_3[2][4][6] = 6
K_function_3[2][5][6] = 9
K_function_3[2][6][6] = 8
K_function_3[2][7][6] = 3
K_function_3[2][8][6] = 7
K_function_3[2][9][6] = 12


K_function_3[3][0][6] = 4
K_function_3[3][1][6] = 7
K_function_3[3][2][6] = 3
K_function_3[3][3][6] = 3
K_function_3[3][4][6] = 5
K_function_3[3][5][6] = 4
K_function_3[3][6][6] = 3
K_function_3[3][7][6] = 7
K_function_3[3][8][6] = 8
K_function_3[3][9][6] = 6


K_function_3[4][0][6] = 7
K_function_3[4][1][6] = 2
K_function_3[4][2][6] = 7
K_function_3[4][3][6] = 8
K_function_3[4][4][6] = 3
K_function_3[4][5][6] = 6
K_function_3[4][6][6] = 6
K_function_3[4][7][6] = 3
K_function_3[4][8][6] = 4
K_function_3[4][9][6] = 8

K_function_3[5][0][6] = 3
K_function_3[5][1][6] = 7
K_function_3[5][2][6] = 7
K_function_3[5][3][6] = 6
K_function_3[5][4][6] = 3
K_function_3[5][5][6] = 4
K_function_3[5][6][6] = 9
K_function_3[5][7][6] = 4
K_function_3[5][8][6] = 3
K_function_3[5][9][6] = 4

K_function_3[6][0][6] = 8
K_function_3[6][1][6] = 3
K_function_3[6][2][6] = 4
K_function_3[6][3][6] = 6
K_function_3[6][4][6] = 8
K_function_3[6][5][6] = 4
K_function_3[6][6][6] = 7
K_function_3[6][7][6] = 2
K_function_3[6][8][6] = 3
K_function_3[6][9][6] = 6

K_function_3[7][0][6] = 3
K_function_3[7][1][6] = 3
K_function_3[7][2][6] = 6
K_function_3[7][3][6] = 8
K_function_3[7][4][6] = 8
K_function_3[7][5][6] = 3
K_function_3[7][6][6] = 3
K_function_3[7][7][6] = 6
K_function_3[7][8][6] = 4
K_function_3[7][9][6] = 4

K_function_3[8][0][6] = 9
K_function_3[8][1][6] = 3
K_function_3[8][2][6] = 3
K_function_3[8][3][6] = 7
K_function_3[8][4][6] = 8
K_function_3[8][5][6] = 8
K_function_3[8][6][6] = 6
K_function_3[8][7][6] = 1
K_function_3[8][8][6] = 2
K_function_3[8][9][6] = 3

K_function_3[9][0][6] = 3
K_function_3[9][1][6] = 3
K_function_3[9][2][6] = 5
K_function_3[9][3][6] = 8
K_function_3[9][4][6] = 4
K_function_3[9][5][6] = 10
K_function_3[9][6][6] = 8
K_function_3[9][7][6] = 9
K_function_3[9][8][6] = 12
K_function_3[9][9][6] = 4


















K_function_3[0][0][7] = 1
K_function_3[0][1][7] = 3
K_function_3[0][2][7] = 10
K_function_3[0][3][7] = 3
K_function_3[0][4][7] = 7
K_function_3[0][5][7] = 5
K_function_3[0][6][7] = 3
K_function_3[0][7][7] = 3
K_function_3[0][8][7] = 8
K_function_3[0][9][7] = 1

K_function_3[1][0][7] = 3
K_function_3[1][1][7] = 6
K_function_3[1][2][7] = 2
K_function_3[1][3][7] = 4
K_function_3[1][4][7] = 9
K_function_3[1][5][7] = 9
K_function_3[1][6][7] = 9
K_function_3[1][7][7] = 14
K_function_3[1][8][7] = 3
K_function_3[1][9][7] = 8

K_function_3[2][0][7] = 3
K_function_3[2][1][7] = 4
K_function_3[2][2][7] = 9
K_function_3[2][3][7] = 2
K_function_3[2][4][7] = 10
K_function_3[2][5][7] = 9
K_function_3[2][6][7] = 5
K_function_3[2][7][7] = 7
K_function_3[2][8][7] = 9
K_function_3[2][9][7] = 10


K_function_3[3][0][7] = 13
K_function_3[3][1][7] = 14
K_function_3[3][2][7] = 3
K_function_3[3][3][7] = 9
K_function_3[3][4][7] = 3
K_function_3[3][5][7] = 1
K_function_3[3][6][7] = 8
K_function_3[3][7][7] = 6
K_function_3[3][8][7] = 7
K_function_3[3][9][7] = 6


K_function_3[4][0][7] = 3
K_function_3[4][1][7] = 9
K_function_3[4][2][7] = 6
K_function_3[4][3][7] = 3
K_function_3[4][4][7] = 6
K_function_3[4][5][7] = 5
K_function_3[4][6][7] = 1
K_function_3[4][7][7] = 9
K_function_3[4][8][7] = 3
K_function_3[4][9][7] = 6

K_function_3[5][0][7] = 5
K_function_3[5][1][7] = 3
K_function_3[5][2][7] = 8
K_function_3[5][3][7] = 4
K_function_3[5][4][7] = 12
K_function_3[5][5][7] = 13
K_function_3[5][6][7] = 2
K_function_3[5][7][7] = 8
K_function_3[5][8][7] = 7
K_function_3[5][9][7] = 3

K_function_3[6][0][7] = 7
K_function_3[6][1][7] = 12
K_function_3[6][2][7] = 13
K_function_3[6][3][7] = 5
K_function_3[6][4][7] = 6
K_function_3[6][5][7] = 8
K_function_3[6][6][7] = 3
K_function_3[6][7][7] = 4
K_function_3[6][8][7] = 7
K_function_3[6][9][7] = 3

K_function_3[7][0][7] = 14
K_function_3[7][1][7] = 8
K_function_3[7][2][7] = 3
K_function_3[7][3][7] = 6
K_function_3[7][4][7] = 2
K_function_3[7][5][7] = 2
K_function_3[7][6][7] = 3
K_function_3[7][7][7] = 7
K_function_3[7][8][7] = 9
K_function_3[7][9][7] = 2

K_function_3[8][0][7] = 3
K_function_3[8][1][7] = 2
K_function_3[8][2][7] = 8
K_function_3[8][3][7] = 4
K_function_3[8][4][7] = 3
K_function_3[8][5][7] = 8
K_function_3[8][6][7] = 6
K_function_3[8][7][7] = 9
K_function_3[8][8][7] = 2
K_function_3[8][9][7] = 3

K_function_3[9][0][7] = 5
K_function_3[9][1][7] = 3
K_function_3[9][2][7] = 4
K_function_3[9][3][7] = 8
K_function_3[9][4][7] = 5
K_function_3[9][5][7] = 6
K_function_3[9][6][7] = 3
K_function_3[9][7][7] = 2
K_function_3[9][8][7] = 8
K_function_3[9][9][7] = 12














K_function_3[0][0][8] = 9
K_function_3[0][1][8] = 1
K_function_3[0][2][8] = 3
K_function_3[0][3][8] = 10
K_function_3[0][4][8] = 12
K_function_3[0][5][8] = 10
K_function_3[0][6][8] = 6
K_function_3[0][7][8] = 3
K_function_3[0][8][8] = 2
K_function_3[0][9][8] = 1

K_function_3[1][0][8] = 9
K_function_3[1][1][8] = 6
K_function_3[1][2][8] = 3
K_function_3[1][3][8] = 4
K_function_3[1][4][8] = 3
K_function_3[1][5][8] = 8
K_function_3[1][6][8] = 9
K_function_3[1][7][8] = 10
K_function_3[1][8][8] = 11
K_function_3[1][9][8] = 4

K_function_3[2][0][8] = 3
K_function_3[2][1][8] = 4
K_function_3[2][2][8] = 6
K_function_3[2][3][8] = 7
K_function_3[2][4][8] = 5
K_function_3[2][5][8] = 3
K_function_3[2][6][8] = 1
K_function_3[2][7][8] = 1
K_function_3[2][8][8] = 1
K_function_3[2][9][8] = 9


K_function_3[3][0][8] = 8
K_function_3[3][1][8] = 3
K_function_3[3][2][8] = 7
K_function_3[3][3][8] = 5
K_function_3[3][4][8] = 6
K_function_3[3][5][8] = 3
K_function_3[3][6][8] = 8
K_function_3[3][7][8] = 7
K_function_3[3][8][8] = 2
K_function_3[3][9][8] = 3


K_function_3[4][0][8] = 3
K_function_3[4][1][8] = 5
K_function_3[4][2][8] = 6
K_function_3[4][3][8] = 9
K_function_3[4][4][8] = 1
K_function_3[4][5][8] = 3
K_function_3[4][6][8] = 7
K_function_3[4][7][8] = 6
K_function_3[4][8][8] = 9
K_function_3[4][9][8] = 12

K_function_3[5][0][8] = 7
K_function_3[5][1][8] = 6
K_function_3[5][2][8] = 2
K_function_3[5][3][8] = 3
K_function_3[5][4][8] = 8
K_function_3[5][5][8] = 9
K_function_3[5][6][8] = 10
K_function_3[5][7][8] = 8
K_function_3[5][8][8] = 8
K_function_3[5][9][8] = 3

K_function_3[6][0][8] = 6
K_function_3[6][1][8] = 3
K_function_3[6][2][8] = 9
K_function_3[6][3][8] = 8
K_function_3[6][4][8] = 4
K_function_3[6][5][8] = 6
K_function_3[6][6][8] = 9
K_function_3[6][7][8] = 4
K_function_3[6][8][8] = 3
K_function_3[6][9][8] = 4

K_function_3[7][0][8] = 8
K_function_3[7][1][8] = 4
K_function_3[7][2][8] = 6
K_function_3[7][3][8] = 9
K_function_3[7][4][8] = 3
K_function_3[7][5][8] = 2
K_function_3[7][6][8] = 1
K_function_3[7][7][8] = 5
K_function_3[7][8][8] = 3
K_function_3[7][9][8] = 9

K_function_3[8][0][8] = 8
K_function_3[8][1][8] = 2
K_function_3[8][2][8] = 3
K_function_3[8][3][8] = 6
K_function_3[8][4][8] = 8
K_function_3[8][5][8] = 4
K_function_3[8][6][8] = 2
K_function_3[8][7][8] = 3
K_function_3[8][8][8] = 4
K_function_3[8][9][8] = 3

K_function_3[9][0][8] = 3
K_function_3[9][1][8] = 6
K_function_3[9][2][8] = 3
K_function_3[9][3][8] = 8
K_function_3[9][4][8] = 6
K_function_3[9][5][8] = 3
K_function_3[9][6][8] = 2
K_function_3[9][7][8] = 9
K_function_3[9][8][8] = 6
K_function_3[9][9][8] = 4












K_function_3[0][0][9] = 6
K_function_3[0][1][9] = 8
K_function_3[0][2][9] = 4
K_function_3[0][3][9] = 4
K_function_3[0][4][9] = 9
K_function_3[0][5][9] = 6
K_function_3[0][6][9] = 3
K_function_3[0][7][9] = 8
K_function_3[0][8][9] = 4
K_function_3[0][9][9] = 4

K_function_3[1][0][9] = 3
K_function_3[1][1][9] = 7
K_function_3[1][2][9] = 8
K_function_3[1][3][9] = 6
K_function_3[1][4][9] = 3
K_function_3[1][5][9] = 4
K_function_3[1][6][9] = 6
K_function_3[1][7][9] = 8
K_function_3[1][8][9] = 4
K_function_3[1][9][9] = 9

K_function_3[2][0][9] = 3
K_function_3[2][1][9] = 6
K_function_3[2][2][9] = 2
K_function_3[2][3][9] = 3
K_function_3[2][4][9] = 8
K_function_3[2][5][9] = 12
K_function_3[2][6][9] = 8
K_function_3[2][7][9] = 3
K_function_3[2][8][9] = 5
K_function_3[2][9][9] = 6


K_function_3[3][0][9] = 3
K_function_3[3][1][9] = 4
K_function_3[3][2][9] = 5
K_function_3[3][3][9] = 2
K_function_3[3][4][9] = 3
K_function_3[3][5][9] = 13
K_function_3[3][6][9] = 12
K_function_3[3][7][9] = 11
K_function_3[3][8][9] = 12
K_function_3[3][9][9] = 8


K_function_3[4][0][9] = 3
K_function_3[4][1][9] = 6
K_function_3[4][2][9] = 9
K_function_3[4][3][9] = 8
K_function_3[4][4][9] = 2
K_function_3[4][5][9] = 3
K_function_3[4][6][9] = 8
K_function_3[4][7][9] = 1
K_function_3[4][8][9] = 8
K_function_3[4][9][9] = 3

K_function_3[5][0][9] = 2
K_function_3[5][1][9] = 3
K_function_3[5][2][9] = 14
K_function_3[5][3][9] = 3
K_function_3[5][4][9] = 9
K_function_3[5][5][9] = 4
K_function_3[5][6][9] = 2
K_function_3[5][7][9] = 4
K_function_3[5][8][9] = 14
K_function_3[5][9][9] = 3

K_function_3[6][0][9] = 8
K_function_3[6][1][9] = 9
K_function_3[6][2][9] = 2
K_function_3[6][3][9] = 1
K_function_3[6][4][9] = 3
K_function_3[6][5][9] = 7
K_function_3[6][6][9] = 8
K_function_3[6][7][9] = 2
K_function_3[6][8][9] = 3
K_function_3[6][9][9] = 4

K_function_3[7][0][9] = 8
K_function_3[7][1][9] = 3
K_function_3[7][2][9] = 9
K_function_3[7][3][9] = 6
K_function_3[7][4][9] = 7
K_function_3[7][5][9] = 12
K_function_3[7][6][9] = 3
K_function_3[7][7][9] = 1
K_function_3[7][8][9] = 9
K_function_3[7][9][9] = 2

K_function_3[8][0][9] = 8
K_function_3[8][1][9] = 3
K_function_3[8][2][9] = 9
K_function_3[8][3][9] = 3
K_function_3[8][4][9] = 4
K_function_3[8][5][9] = 9
K_function_3[8][6][9] = 2
K_function_3[8][7][9] = 1
K_function_3[8][8][9] = 3
K_function_3[8][9][9] = 5

K_function_3[9][0][9] = 10
K_function_3[9][1][9] = 11
K_function_3[9][2][9] = 9
K_function_3[9][3][9] = 3
K_function_3[9][4][9] = 6
K_function_3[9][5][9] = 3
K_function_3[9][6][9] = 14
K_function_3[9][7][9] = 8
K_function_3[9][8][9] = 3
K_function_3[9][9][9] = 6













K_function_4 = np.zeros((10, 10, 10))

K_function_4[0][0][0] = 6
K_function_4[0][1][0] = 8
K_function_4[0][2][0] = 6
K_function_4[0][3][0] = 3
K_function_4[0][4][0] = 5
K_function_4[0][5][0] = 6
K_function_4[0][6][0] = 7
K_function_4[0][7][0] = 3
K_function_4[0][8][0] = 2
K_function_4[0][9][0] = 1

K_function_4[1][0][0] = 11
K_function_4[1][1][0] = 1
K_function_4[1][2][0] = 2
K_function_4[1][3][0] = 6
K_function_4[1][4][0] = 8
K_function_4[1][5][0] = 14
K_function_4[1][6][0] = 7
K_function_4[1][7][0] = 3
K_function_4[1][8][0] = 8
K_function_4[1][9][0] = 3

K_function_4[2][0][0] = 7
K_function_4[2][1][0] = 6
K_function_4[2][2][0] = 4
K_function_4[2][3][0] = 8
K_function_4[2][4][0] = 3
K_function_4[2][5][0] = 5
K_function_4[2][6][0] = 5
K_function_4[2][7][0] = 7
K_function_4[2][8][0] = 10
K_function_4[2][9][0] = 7


K_function_4[3][0][0] = 4
K_function_4[3][1][0] = 12
K_function_4[3][2][0] = 13
K_function_4[3][3][0] = 5
K_function_4[3][4][0] = 9
K_function_4[3][5][0] = 2
K_function_4[3][6][0] = 7
K_function_4[3][7][0] = 8
K_function_4[3][8][0] = 3
K_function_4[3][9][0] = 7


K_function_4[4][0][0] = 3
K_function_4[4][1][0] = 15
K_function_4[4][2][0] = 6
K_function_4[4][3][0] = 13
K_function_4[4][4][0] = 11
K_function_4[4][5][0] = 5
K_function_4[4][6][0] = 9
K_function_4[4][7][0] = 3
K_function_4[4][8][0] = 2
K_function_4[4][9][0] = 7

K_function_4[5][0][0] = 3
K_function_4[5][1][0] = 8
K_function_4[5][2][0] = 2
K_function_4[5][3][0] = 14
K_function_4[5][4][0] = 13
K_function_4[5][5][0] = 5
K_function_4[5][6][0] = 7
K_function_4[5][7][0] = 12
K_function_4[5][8][0] = 13
K_function_4[5][9][0] = 11

K_function_4[6][0][0] = 5
K_function_4[6][1][0] = 6
K_function_4[6][2][0] = 9
K_function_4[6][3][0] = 5
K_function_4[6][4][0] = 3
K_function_4[6][5][0] = 8
K_function_4[6][6][0] = 12
K_function_4[6][7][0] = 11
K_function_4[6][8][0] = 5
K_function_4[6][9][0] = 6

K_function_4[7][0][0] = 9
K_function_4[7][1][0] = 11
K_function_4[7][2][0] = 3
K_function_4[7][3][0] = 6
K_function_4[7][4][0] = 8
K_function_4[7][5][0] = 3
K_function_4[7][6][0] = 3
K_function_4[7][7][0] = 6
K_function_4[7][8][0] = 8
K_function_4[7][9][0] = 8

K_function_4[8][0][0] = 2
K_function_4[8][1][0] = 3
K_function_4[8][2][0] = 6
K_function_4[8][3][0] = 3
K_function_4[8][4][0] = 5
K_function_4[8][5][0] = 9
K_function_4[8][6][0] = 3
K_function_4[8][7][0] = 2
K_function_4[8][8][0] = 3
K_function_4[8][9][0] = 8

K_function_4[9][0][0] = 3
K_function_4[9][1][0] = 5
K_function_4[9][2][0] = 8
K_function_4[9][3][0] = 1
K_function_4[9][4][0] = 9
K_function_4[9][5][0] = 5
K_function_4[9][6][0] = 3
K_function_4[9][7][0] = 7
K_function_4[9][8][0] = 8
K_function_4[9][9][0] = 6


K_function_4[0][0][1] = 1
K_function_4[0][1][1] = 5
K_function_4[0][2][1] = 12
K_function_4[0][3][1] = 10
K_function_4[0][4][1] = 8
K_function_4[0][5][1] = 9
K_function_4[0][6][1] = 3
K_function_4[0][7][1] = 5
K_function_4[0][8][1] = 6
K_function_4[0][9][1] = 6

K_function_4[1][0][1] = 8
K_function_4[1][1][1] = 1
K_function_4[1][2][1] = 6
K_function_4[1][3][1] = 7
K_function_4[1][4][1] = 7
K_function_4[1][5][1] = 3
K_function_4[1][6][1] = 6
K_function_4[1][7][1] = 7
K_function_4[1][8][1] = 1
K_function_4[1][9][1] = 8

K_function_4[2][0][1] = 1
K_function_4[2][1][1] = 12
K_function_4[2][2][1] = 8
K_function_4[2][3][1] = 3
K_function_4[2][4][1] = 9
K_function_4[2][5][1] = 12
K_function_4[2][6][1] = 11
K_function_4[2][7][1] = 5
K_function_4[2][8][1] = 4
K_function_4[2][9][1] = 2


K_function_4[3][0][1] = 3
K_function_4[3][1][1] = 8
K_function_4[3][2][1] = 2
K_function_4[3][3][1] = 8
K_function_4[3][4][1] = 4
K_function_4[3][5][1] = 3
K_function_4[3][6][1] = 7
K_function_4[3][7][1] = 8
K_function_4[3][8][1] = 4
K_function_4[3][9][1] = 7


K_function_4[4][0][1] = 3
K_function_4[4][1][1] = 8
K_function_4[4][2][1] = 12
K_function_4[4][3][1] = 3
K_function_4[4][4][1] = 8
K_function_4[4][5][1] = 5
K_function_4[4][6][1] = 7
K_function_4[4][7][1] = 9
K_function_4[4][8][1] = 2
K_function_4[4][9][1] = 8

K_function_4[5][0][1] = 10
K_function_4[5][1][1] = 11
K_function_4[5][2][1] = 8
K_function_4[5][3][1] = 4
K_function_4[5][4][1] = 3
K_function_4[5][5][1] = 2
K_function_4[5][6][1] = 9
K_function_4[5][7][1] = 5
K_function_4[5][8][1] = 8
K_function_4[5][9][1] = 13

K_function_4[6][0][1] = 1
K_function_4[6][1][1] = 5
K_function_4[6][2][1] = 10
K_function_4[6][3][1] = 3
K_function_4[6][4][1] = 6
K_function_4[6][5][1] = 8
K_function_4[6][6][1] = 6
K_function_4[6][7][1] = 7
K_function_4[6][8][1] = 3
K_function_4[6][9][1] = 11

K_function_4[7][0][1] = 15
K_function_4[7][1][1] = 8
K_function_4[7][2][1] = 3
K_function_4[7][3][1] = 2
K_function_4[7][4][1] = 14
K_function_4[7][5][1] = 3
K_function_4[7][6][1] = 6
K_function_4[7][7][1] = 4
K_function_4[7][8][1] = 8
K_function_4[7][9][1] = 2

K_function_4[8][0][1] = 3
K_function_4[8][1][1] = 10
K_function_4[8][2][1] = 8
K_function_4[8][3][1] = 7
K_function_4[8][4][1] = 8
K_function_4[8][5][1] = 3
K_function_4[8][6][1] = 6
K_function_4[8][7][1] = 10
K_function_4[8][8][1] = 12
K_function_4[8][9][1] = 8

K_function_4[9][0][1] = 3
K_function_4[9][1][1] = 8
K_function_4[9][2][1] = 9
K_function_4[9][3][1] = 8
K_function_4[9][4][1] = 3
K_function_4[9][5][1] = 14
K_function_4[9][6][1] = 8
K_function_4[9][7][1] = 7
K_function_4[9][8][1] = 3
K_function_4[9][9][1] = 14
















K_function_4[0][0][2] = 6
K_function_4[0][1][2] = 3
K_function_4[0][2][2] = 4
K_function_4[0][3][2] = 14
K_function_4[0][4][2] = 6
K_function_4[0][5][2] = 2
K_function_4[0][6][2] = 7
K_function_4[0][7][2] = 3
K_function_4[0][8][2] = 6
K_function_4[0][9][2] = 3

K_function_4[1][0][2] = 4
K_function_4[1][1][2] = 3
K_function_4[1][2][2] = 5
K_function_4[1][3][2] = 6
K_function_4[1][4][2] = 8
K_function_4[1][5][2] = 12
K_function_4[1][6][2] = 15
K_function_4[1][7][2] = 8
K_function_4[1][8][2] = 5
K_function_4[1][9][2] = 1

K_function_4[2][0][2] = 8
K_function_4[2][1][2] = 3
K_function_4[2][2][2] = 3
K_function_4[2][3][2] = 6
K_function_4[2][4][2] = 8
K_function_4[2][5][2] = 13
K_function_4[2][6][2] = 14
K_function_4[2][7][2] = 2
K_function_4[2][8][2] = 8
K_function_4[2][9][2] = 9


K_function_4[3][0][2] = 8
K_function_4[3][1][2] = 6
K_function_4[3][2][2] = 3
K_function_4[3][3][2] = 14
K_function_4[3][4][2] = 12
K_function_4[3][5][2] = 8
K_function_4[3][6][2] = 6
K_function_4[3][7][2] = 13
K_function_4[3][8][2] = 4
K_function_4[3][9][2] = 8


K_function_4[4][0][2] = 8
K_function_4[4][1][2] = 6
K_function_4[4][2][2] = 14
K_function_4[4][3][2] = 2
K_function_4[4][4][2] = 13
K_function_4[4][5][2] = 5
K_function_4[4][6][2] = 8
K_function_4[4][7][2] = 14
K_function_4[4][8][2] = 6
K_function_4[4][9][2] = 8

K_function_4[5][0][2] = 3
K_function_4[5][1][2] = 2
K_function_4[5][2][2] = 15
K_function_4[5][3][2] = 1
K_function_4[5][4][2] = 8
K_function_4[5][5][2] = 2
K_function_4[5][6][2] = 3
K_function_4[5][7][2] = 5
K_function_4[5][8][2] = 8
K_function_4[5][9][2] = 6
K_function_4[6][0][2] = 3
K_function_4[6][1][2] = 7
K_function_4[6][2][2] = 8
K_function_4[6][3][2] = 9
K_function_4[6][4][2] = 3
K_function_4[6][5][2] = 6
K_function_4[6][6][2] = 8
K_function_4[6][7][2] = 6
K_function_4[6][8][2] = 8
K_function_4[6][9][2] = 12

K_function_4[7][0][2] = 15
K_function_4[7][1][2] = 3
K_function_4[7][2][2] = 7
K_function_4[7][3][2] = 1
K_function_4[7][4][2] = 14
K_function_4[7][5][2] = 6
K_function_4[7][6][2] = 6
K_function_4[7][7][2] = 8
K_function_4[7][8][2] = 4
K_function_4[7][9][2] = 8

K_function_4[8][0][2] = 13
K_function_4[8][1][2] = 2
K_function_4[8][2][2] = 11
K_function_4[8][3][2] = 7
K_function_4[8][4][2] = 6
K_function_4[8][5][2] = 2
K_function_4[8][6][2] = 5
K_function_4[8][7][2] = 9
K_function_4[8][8][2] = 8
K_function_4[8][9][2] = 7

K_function_4[9][0][2] = 8
K_function_4[9][1][2] = 9
K_function_4[9][2][2] = 14
K_function_4[9][3][2] = 15
K_function_4[9][4][2] = 11
K_function_4[9][5][2] = 7
K_function_4[9][6][2] = 5
K_function_4[9][7][2] = 13
K_function_4[9][8][2] = 8
K_function_4[9][9][2] = 2
















K_function_4[0][0][3] = 8
K_function_4[0][1][3] = 7
K_function_4[0][2][3] = 3
K_function_4[0][3][3] = 8
K_function_4[0][4][3] = 6
K_function_4[0][5][3] = 12
K_function_4[0][6][3] = 5
K_function_4[0][7][3] = 8
K_function_4[0][8][3] = 5
K_function_4[0][9][3] = 7

K_function_4[1][0][3] = 2
K_function_4[1][1][3] = 3
K_function_4[1][2][3] = 8
K_function_4[1][3][3] = 13
K_function_4[1][4][3] = 13
K_function_4[1][5][3] = 1
K_function_4[1][6][3] = 2
K_function_4[1][7][3] = 5
K_function_4[1][8][3] = 2
K_function_4[1][9][3] = 8

K_function_4[2][0][3] = 8
K_function_4[2][1][3] = 2
K_function_4[2][2][3] = 14
K_function_4[2][3][3] = 8
K_function_4[2][4][3] = 3
K_function_4[2][5][3] = 3
K_function_4[2][6][3] = 3
K_function_4[2][7][3] = 6
K_function_4[2][8][3] = 4
K_function_4[2][9][3] = 8


K_function_4[3][0][3] = 9
K_function_4[3][1][3] = 7
K_function_4[3][2][3] = 11
K_function_4[3][3][3] = 5
K_function_4[3][4][3] = 8
K_function_4[3][5][3] = 3
K_function_4[3][6][3] = 6
K_function_4[3][7][3] = 8
K_function_4[3][8][3] = 5
K_function_4[3][9][3] = 7

K_function_4[4][0][3] = 8
K_function_4[4][1][3] = 13
K_function_4[4][2][3] = 6
K_function_4[4][3][3] = 7
K_function_4[4][4][3] = 8
K_function_4[4][5][3] = 6
K_function_4[4][6][3] = 13
K_function_4[4][7][3] = 8
K_function_4[4][8][3] = 6
K_function_4[4][9][3] = 8

K_function_4[5][0][3] = 10
K_function_4[5][1][3] = 11
K_function_4[5][2][3] = 13
K_function_4[5][3][3] = 8
K_function_4[5][4][3] = 7
K_function_4[5][5][3] = 14
K_function_4[5][6][3] = 3
K_function_4[5][7][3] = 1
K_function_4[5][8][3] = 1
K_function_4[5][9][3] = 1

K_function_4[6][0][3] = 6
K_function_4[6][1][3] = 7
K_function_4[6][2][3] = 8
K_function_4[6][3][3] = 13
K_function_4[6][4][3] = 1
K_function_4[6][5][3] = 2
K_function_4[6][6][3] = 8
K_function_4[6][7][3] = 9
K_function_4[6][8][3] = 12
K_function_4[6][9][3] = 11

K_function_4[7][0][3] = 8
K_function_4[7][1][3] = 3
K_function_4[7][2][3] = 5
K_function_4[7][3][3] = 9
K_function_4[7][4][3] = 2
K_function_4[7][5][3] = 8
K_function_4[7][6][3] = 1
K_function_4[7][7][3] = 6
K_function_4[7][8][3] = 13
K_function_4[7][9][3] = 11

K_function_4[8][0][3] = 7
K_function_4[8][1][3] = 8
K_function_4[8][2][3] = 5
K_function_4[8][3][3] = 8
K_function_4[8][4][3] = 5
K_function_4[8][5][3] = 6
K_function_4[8][6][3] = 4
K_function_4[8][7][3] = 8
K_function_4[8][8][3] = 12
K_function_4[8][9][3] = 3

K_function_4[9][0][3] = 8
K_function_4[9][1][3] = 4
K_function_4[9][2][3] = 5
K_function_4[9][3][3] = 12
K_function_4[9][4][3] = 11
K_function_4[9][5][3] = 5
K_function_4[9][6][3] = 8
K_function_4[9][7][3] = 6
K_function_4[9][8][3] = 12
K_function_4[9][9][3] = 5















K_function_4[0][0][4] = 4
K_function_4[0][1][4] = 6
K_function_4[0][2][4] = 8
K_function_4[0][3][4] = 7
K_function_4[0][4][4] = 8
K_function_4[0][5][4] = 6
K_function_4[0][6][4] = 2
K_function_4[0][7][4] = 5
K_function_4[0][8][4] = 8
K_function_4[0][9][4] = 6

K_function_4[1][0][4] = 8
K_function_4[1][1][4] = 2
K_function_4[1][2][4] = 6
K_function_4[1][3][4] = 5
K_function_4[1][4][4] = 12
K_function_4[1][5][4] = 12
K_function_4[1][6][4] = 7
K_function_4[1][7][4] = 3
K_function_4[1][8][4] = 5
K_function_4[1][9][4] = 8

K_function_4[2][0][4] = 6
K_function_4[2][1][4] = 8
K_function_4[2][2][4] = 6
K_function_4[2][3][4] = 8
K_function_4[2][4][4] = 6
K_function_4[2][5][4] = 7
K_function_4[2][6][4] = 12
K_function_4[2][7][4] = 3
K_function_4[2][8][4] = 5
K_function_4[2][9][4] = 6


K_function_4[3][0][4] = 8
K_function_4[3][1][4] = 9
K_function_4[3][2][4] = 3
K_function_4[3][3][4] = 4
K_function_4[3][4][4] = 4
K_function_4[3][5][4] = 2
K_function_4[3][6][4] = 6
K_function_4[3][7][4] = 3
K_function_4[3][8][4] = 2
K_function_4[3][9][4] = 8


K_function_4[4][0][4] = 7
K_function_4[4][1][4] = 3
K_function_4[4][2][4] = 6
K_function_4[4][3][4] = 12
K_function_4[4][4][4] = 5
K_function_4[4][5][4] = 8
K_function_4[4][6][4] = 13
K_function_4[4][7][4] = 5
K_function_4[4][8][4] = 3
K_function_4[4][9][4] = 6

K_function_4[5][0][4] = 8
K_function_4[5][1][4] = 3
K_function_4[5][2][4] = 6
K_function_4[5][3][4] = 4
K_function_4[5][4][4] = 11
K_function_4[5][5][4] = 2
K_function_4[5][6][4] = 2
K_function_4[5][7][4] = 3
K_function_4[5][8][4] = 8
K_function_4[5][9][4] = 3

K_function_4[6][0][4] = 5
K_function_4[6][1][4] = 4
K_function_4[6][2][4] = 3
K_function_4[6][3][4] = 6
K_function_4[6][4][4] = 5
K_function_4[6][5][4] = 7
K_function_4[6][6][4] = 4
K_function_4[6][7][4] = 3
K_function_4[6][8][4] = 8
K_function_4[6][9][4] = 6

K_function_4[7][0][4] = 8
K_function_4[7][1][4] = 1
K_function_4[7][2][4] = 1
K_function_4[7][3][4] = 3
K_function_4[7][4][4] = 6
K_function_4[7][5][4] = 7
K_function_4[7][6][4] = 6
K_function_4[7][7][4] = 8
K_function_4[7][8][4] = 9
K_function_4[7][9][4] = 12

K_function_4[8][0][4] = 5
K_function_4[8][1][4] = 2
K_function_4[8][2][4] = 6
K_function_4[8][3][4] = 8
K_function_4[8][4][4] = 12
K_function_4[8][5][4] = 3
K_function_4[8][6][4] = 1
K_function_4[8][7][4] = 8
K_function_4[8][8][4] = 5
K_function_4[8][9][4] = 5

K_function_4[9][0][4] = 6
K_function_4[9][1][4] = 6
K_function_4[9][2][4] = 9
K_function_4[9][3][4] = 4
K_function_4[9][4][4] = 1
K_function_4[9][5][4] = 8
K_function_4[9][6][4] = 7
K_function_4[9][7][4] = 3
K_function_4[9][8][4] = 5
K_function_4[9][9][4] = 12



















K_function_4[0][0][5] = 4
K_function_4[0][1][5] = 6
K_function_4[0][2][5] = 8
K_function_4[0][3][5] = 3
K_function_4[0][4][5] = 7
K_function_4[0][5][5] = 4
K_function_4[0][6][5] = 6
K_function_4[0][7][5] = 8
K_function_4[0][8][5] = 7
K_function_4[0][9][5] = 8

K_function_4[1][0][5] = 6
K_function_4[1][1][5] = 9
K_function_4[1][2][5] = 8
K_function_4[1][3][5] = 5
K_function_4[1][4][5] = 13
K_function_4[1][5][5] = 5
K_function_4[1][6][5] = 8
K_function_4[1][7][5] = 6
K_function_4[1][8][5] = 7
K_function_4[1][9][5] = 3

K_function_4[2][0][5] = 5
K_function_4[2][1][5] = 8
K_function_4[2][2][5] = 3
K_function_4[2][3][5] = 8
K_function_4[2][4][5] = 6
K_function_4[2][5][5] = 8
K_function_4[2][6][5] = 12
K_function_4[2][7][5] = 4
K_function_4[2][8][5] = 8
K_function_4[2][9][5] = 7


K_function_4[3][0][5] = 2
K_function_4[3][1][5] = 3
K_function_4[3][2][5] = 8
K_function_4[3][3][5] = 12
K_function_4[3][4][5] = 6
K_function_4[3][5][5] = 9
K_function_4[3][6][5] = 9
K_function_4[3][7][5] = 5
K_function_4[3][8][5] = 6
K_function_4[3][9][5] = 3


K_function_4[4][0][5] = 5
K_function_4[4][1][5] = 8
K_function_4[4][2][5] = 11
K_function_4[4][3][5] = 5
K_function_4[4][4][5] = 8
K_function_4[4][5][5] = 3
K_function_4[4][6][5] = 9
K_function_4[4][7][5] = 8
K_function_4[4][8][5] = 12
K_function_4[4][9][5] = 5

K_function_4[5][0][5] = 6
K_function_4[5][1][5] = 4
K_function_4[5][2][5] = 5
K_function_4[5][3][5] = 7
K_function_4[5][4][5] = 8
K_function_4[5][5][5] = 9
K_function_4[5][6][5] = 3
K_function_4[5][7][5] = 2
K_function_4[5][8][5] = 1
K_function_4[5][9][5] = 8

K_function_4[6][0][5] = 6
K_function_4[6][1][5] = 5
K_function_4[6][2][5] = 7
K_function_4[6][3][5] = 3
K_function_4[6][4][5] = 7
K_function_4[6][5][5] = 13
K_function_4[6][6][5] = 2
K_function_4[6][7][5] = 8
K_function_4[6][8][5] = 6
K_function_4[6][9][5] = 7

K_function_4[7][0][5] = 2
K_function_4[7][1][5] = 8
K_function_4[7][2][5] = 14
K_function_4[7][3][5] = 8
K_function_4[7][4][5] = 12
K_function_4[7][5][5] = 10
K_function_4[7][6][5] = 2
K_function_4[7][7][5] = 3
K_function_4[7][8][5] = 8
K_function_4[7][9][5] = 3

K_function_4[8][0][5] = 5
K_function_4[8][1][5] = 8
K_function_4[8][2][5] = 12
K_function_4[8][3][5] = 15
K_function_4[8][4][5] = 8
K_function_4[8][5][5] = 6
K_function_4[8][6][5] = 9
K_function_4[8][7][5] = 8
K_function_4[8][8][5] = 8
K_function_4[8][9][5] = 1

K_function_4[9][0][5] = 6
K_function_4[9][1][5] = 3
K_function_4[9][2][5] = 7
K_function_4[9][3][5] = 3
K_function_4[9][4][5] = 5
K_function_4[9][5][5] = 6
K_function_4[9][6][5] = 5
K_function_4[9][7][5] = 7
K_function_4[9][8][5] = 6
K_function_4[9][9][5] = 8

















K_function_4[0][0][6] = 8
K_function_4[0][1][6] = 4
K_function_4[0][2][6] = 7
K_function_4[0][3][6] = 3
K_function_4[0][4][6] = 8
K_function_4[0][5][6] = 12
K_function_4[0][6][6] = 6
K_function_4[0][7][6] = 9
K_function_4[0][8][6] = 8
K_function_4[0][9][6] = 11

K_function_4[1][0][6] = 5
K_function_4[1][1][6] = 7
K_function_4[1][2][6] = 3
K_function_4[1][3][6] = 5
K_function_4[1][4][6] = 6
K_function_4[1][5][6] = 7
K_function_4[1][6][6] = 3
K_function_4[1][7][6] = 4
K_function_4[1][8][6] = 1
K_function_4[1][9][6] = 2

K_function_4[2][0][6] = 3
K_function_4[2][1][6] = 2
K_function_4[2][2][6] = 8
K_function_4[2][3][6] = 7
K_function_4[2][4][6] = 12
K_function_4[2][5][6] = 13
K_function_4[2][6][6] = 8
K_function_4[2][7][6] = 6
K_function_4[2][8][6] = 7
K_function_4[2][9][6] = 5


K_function_4[3][0][6] = 6
K_function_4[3][1][6] = 7
K_function_4[3][2][6] = 5
K_function_4[3][3][6] = 8
K_function_4[3][4][6] = 6
K_function_4[3][5][6] = 3
K_function_4[3][6][6] = 2
K_function_4[3][7][6] = 6
K_function_4[3][8][6] = 12
K_function_4[3][9][6] = 5


K_function_4[4][0][6] = 8
K_function_4[4][1][6] = 4
K_function_4[4][2][6] = 8
K_function_4[4][3][6] = 3
K_function_4[4][4][6] = 6
K_function_4[4][5][6] = 8
K_function_4[4][6][6] = 9
K_function_4[4][7][6] = 12
K_function_4[4][8][6] = 2
K_function_4[4][9][6] = 13

K_function_4[5][0][6] = 5
K_function_4[5][1][6] = 3
K_function_4[5][2][6] = 6
K_function_4[5][3][6] = 12
K_function_4[5][4][6] = 8
K_function_4[5][5][6] = 3
K_function_4[5][6][6] = 5
K_function_4[5][7][6] = 3
K_function_4[5][8][6] = 4
K_function_4[5][9][6] = 8

K_function_4[6][0][6] = 3
K_function_4[6][1][6] = 6
K_function_4[6][2][6] = 4
K_function_4[6][3][6] = 7
K_function_4[6][4][6] = 5
K_function_4[6][5][6] = 8
K_function_4[6][6][6] = 3
K_function_4[6][7][6] = 6
K_function_4[6][8][6] = 8
K_function_4[6][9][6] = 6

K_function_4[7][0][6] = 8
K_function_4[7][1][6] = 1
K_function_4[7][2][6] = 1
K_function_4[7][3][6] = 2
K_function_4[7][4][6] = 3
K_function_4[7][5][6] = 6
K_function_4[7][6][6] = 8
K_function_4[7][7][6] = 7
K_function_4[7][8][6] = 8
K_function_4[7][9][6] = 7

K_function_4[8][0][6] = 8
K_function_4[8][1][6] = 2
K_function_4[8][2][6] = 3
K_function_4[8][3][6] = 3
K_function_4[8][4][6] = 5
K_function_4[8][5][6] = 8
K_function_4[8][6][6] = 4
K_function_4[8][7][6] = 6
K_function_4[8][8][6] = 7
K_function_4[8][9][6] = 3

K_function_4[9][0][6] = 8
K_function_4[9][1][6] = 4
K_function_4[9][2][6] = 3
K_function_4[9][3][6] = 8
K_function_4[9][4][6] = 3
K_function_4[9][5][6] = 5
K_function_4[9][6][6] = 8
K_function_4[9][7][6] = 6
K_function_4[9][8][6] = 7
K_function_4[9][9][6] = 8


















K_function_4[0][0][7] = 9
K_function_4[0][1][7] = 5
K_function_4[0][2][7] = 3
K_function_4[0][3][7] = 2
K_function_4[0][4][7] = 6
K_function_4[0][5][7] = 8
K_function_4[0][6][7] = 12
K_function_4[0][7][7] = 3
K_function_4[0][8][7] = 5
K_function_4[0][9][7] = 7

K_function_4[1][0][7] = 3
K_function_4[1][1][7] = 2
K_function_4[1][2][7] = 1
K_function_4[1][3][7] = 8
K_function_4[1][4][7] = 3
K_function_4[1][5][7] = 7
K_function_4[1][6][7] = 6
K_function_4[1][7][7] = 5
K_function_4[1][8][7] = 7
K_function_4[1][9][7] = 6

K_function_4[2][0][7] = 3
K_function_4[2][1][7] = 5
K_function_4[2][2][7] = 8
K_function_4[2][3][7] = 6
K_function_4[2][4][7] = 8
K_function_4[2][5][7] = 3
K_function_4[2][6][7] = 7
K_function_4[2][7][7] = 8
K_function_4[2][8][7] = 6
K_function_4[2][9][7] = 2


K_function_4[3][0][7] = 5
K_function_4[3][1][7] = 6
K_function_4[3][2][7] = 2
K_function_4[3][3][7] = 3
K_function_4[3][4][7] = 4
K_function_4[3][5][7] = 8
K_function_4[3][6][7] = 3
K_function_4[3][7][7] = 6
K_function_4[3][8][7] = 7
K_function_4[3][9][7] = 7


K_function_4[4][0][7] = 3
K_function_4[4][1][7] = 8
K_function_4[4][2][7] = 6
K_function_4[4][3][7] = 8
K_function_4[4][4][7] = 12
K_function_4[4][5][7] = 10
K_function_4[4][6][7] = 10
K_function_4[4][7][7] = 3
K_function_4[4][8][7] = 5
K_function_4[4][9][7] = 7

K_function_4[5][0][7] = 6
K_function_4[5][1][7] = 5
K_function_4[5][2][7] = 8
K_function_4[5][3][7] = 7
K_function_4[5][4][7] = 9
K_function_4[5][5][7] = 6
K_function_4[5][6][7] = 12
K_function_4[5][7][7] = 10
K_function_4[5][8][7] = 4
K_function_4[5][9][7] = 8

K_function_4[6][0][7] = 7
K_function_4[6][1][7] = 2
K_function_4[6][2][7] = 4
K_function_4[6][3][7] = 8
K_function_4[6][4][7] = 5
K_function_4[6][5][7] = 7
K_function_4[6][6][7] = 3
K_function_4[6][7][7] = 6
K_function_4[6][8][7] = 8
K_function_4[6][9][7] = 2

K_function_4[7][0][7] = 5
K_function_4[7][1][7] = 3
K_function_4[7][2][7] = 12
K_function_4[7][3][7] = 5
K_function_4[7][4][7] = 8
K_function_4[7][5][7] = 8
K_function_4[7][6][7] = 3
K_function_4[7][7][7] = 8
K_function_4[7][8][7] = 6
K_function_4[7][9][7] = 3

K_function_4[8][0][7] = 2
K_function_4[8][1][7] = 1
K_function_4[8][2][7] = 5
K_function_4[8][3][7] = 7
K_function_4[8][4][7] = 6
K_function_4[8][5][7] = 8
K_function_4[8][6][7] = 3
K_function_4[8][7][7] = 3
K_function_4[8][8][7] = 8
K_function_4[8][9][7] = 8

K_function_4[9][0][7] = 6
K_function_4[9][1][7] = 3
K_function_4[9][2][7] = 4
K_function_4[9][3][7] = 5
K_function_4[9][4][7] = 8
K_function_4[9][5][7] = 4
K_function_4[9][6][7] = 3
K_function_4[9][7][7] = 5
K_function_4[9][8][7] = 7
K_function_4[9][9][7] = 12














K_function_4[0][0][8] = 8
K_function_4[0][1][8] = 12
K_function_4[0][2][8] = 9
K_function_4[0][3][8] = 3
K_function_4[0][4][8] = 5
K_function_4[0][5][8] = 9
K_function_4[0][6][8] = 6
K_function_4[0][7][8] = 3
K_function_4[0][8][8] = 8
K_function_4[0][9][8] = 6

K_function_4[1][0][8] = 2
K_function_4[1][1][8] = 3
K_function_4[1][2][8] = 6
K_function_4[1][3][8] = 1
K_function_4[1][4][8] = 2
K_function_4[1][5][8] = 7
K_function_4[1][6][8] = 3
K_function_4[1][7][8] = 6
K_function_4[1][8][8] = 7
K_function_4[1][9][8] = 8

K_function_4[2][0][8] = 6
K_function_4[2][1][8] = 7
K_function_4[2][2][8] = 1
K_function_4[2][3][8] = 3
K_function_4[2][4][8] = 6
K_function_4[2][5][8] = 9
K_function_4[2][6][8] = 8
K_function_4[2][7][8] = 3
K_function_4[2][8][8] = 2
K_function_4[2][9][8] = 2


K_function_4[3][0][8] = 8
K_function_4[3][1][8] = 6
K_function_4[3][2][8] = 8
K_function_4[3][3][8] = 3
K_function_4[3][4][8] = 2
K_function_4[3][5][8] = 8
K_function_4[3][6][8] = 6
K_function_4[3][7][8] = 3
K_function_4[3][8][8] = 8
K_function_4[3][9][8] = 7


K_function_4[4][0][8] = 6
K_function_4[4][1][8] = 3
K_function_4[4][2][8] = 6
K_function_4[4][3][8] = 8
K_function_4[4][4][8] = 6
K_function_4[4][5][8] = 7
K_function_4[4][6][8] = 8
K_function_4[4][7][8] = 6
K_function_4[4][8][8] = 2
K_function_4[4][9][8] = 1

K_function_4[5][0][8] = 3
K_function_4[5][1][8] = 6
K_function_4[5][2][8] = 5
K_function_4[5][3][8] = 2
K_function_4[5][4][8] = 6
K_function_4[5][5][8] = 3
K_function_4[5][6][8] = 14
K_function_4[5][7][8] = 5
K_function_4[5][8][8] = 3
K_function_4[5][9][8] = 7

K_function_4[6][0][8] = 8
K_function_4[6][1][8] = 5
K_function_4[6][2][8] = 7
K_function_4[6][3][8] = 5
K_function_4[6][4][8] = 6
K_function_4[6][5][8] = 12
K_function_4[6][6][8] = 15
K_function_4[6][7][8] = 13
K_function_4[6][8][8] = 2
K_function_4[6][9][8] = 1

K_function_4[7][0][8] = 5
K_function_4[7][1][8] = 8
K_function_4[7][2][8] = 1
K_function_4[7][3][8] = 6
K_function_4[7][4][8] = 8
K_function_4[7][5][8] = 12
K_function_4[7][6][8] = 15
K_function_4[7][7][8] = 6
K_function_4[7][8][8] = 8
K_function_4[7][9][8] = 7

K_function_4[8][0][8] = 6
K_function_4[8][1][8] = 8
K_function_4[8][2][8] = 12
K_function_4[8][3][8] = 12
K_function_4[8][4][8] = 6
K_function_4[8][5][8] = 14
K_function_4[8][6][8] = 8
K_function_4[8][7][8] = 3
K_function_4[8][8][8] = 13
K_function_4[8][9][8] = 8

K_function_4[9][0][8] = 9
K_function_4[9][1][8] = 6
K_function_4[9][2][8] = 8
K_function_4[9][3][8] = 12
K_function_4[9][4][8] = 11
K_function_4[9][5][8] = 5
K_function_4[9][6][8] = 6
K_function_4[9][7][8] = 3
K_function_4[9][8][8] = 7
K_function_4[9][9][8] = 5












K_function_4[0][0][9] = 8
K_function_4[0][1][9] = 2
K_function_4[0][2][9] = 6
K_function_4[0][3][9] = 7
K_function_4[0][4][9] = 5
K_function_4[0][5][9] = 8
K_function_4[0][6][9] = 7
K_function_4[0][7][9] = 5
K_function_4[0][8][9] = 12
K_function_4[0][9][9] = 6

K_function_4[1][0][9] = 8
K_function_4[1][1][9] = 6
K_function_4[1][2][9] = 8
K_function_4[1][3][9] = 12
K_function_4[1][4][9] = 8
K_function_4[1][5][9] = 15
K_function_4[1][6][9] = 3
K_function_4[1][7][9] = 3
K_function_4[1][8][9] = 6
K_function_4[1][9][9] = 12

K_function_4[2][0][9] = 8
K_function_4[2][1][9] = 2
K_function_4[2][2][9] = 3
K_function_4[2][3][9] = 9
K_function_4[2][4][9] = 8
K_function_4[2][5][9] = 6
K_function_4[2][6][9] = 8
K_function_4[2][7][9] = 11
K_function_4[2][8][9] = 8
K_function_4[2][9][9] = 3


K_function_4[3][0][9] = 4
K_function_4[3][1][9] = 5
K_function_4[3][2][9] = 12
K_function_4[3][3][9] = 8
K_function_4[3][4][9] = 3
K_function_4[3][5][9] = 6
K_function_4[3][6][9] = 8
K_function_4[3][7][9] = 12
K_function_4[3][8][9] = 8
K_function_4[3][9][9] = 2


K_function_4[4][0][9] = 12
K_function_4[4][1][9] = 5
K_function_4[4][2][9] = 8
K_function_4[4][3][9] = 6
K_function_4[4][4][9] = 8
K_function_4[4][5][9] = 3
K_function_4[4][6][9] = 5
K_function_4[4][7][9] = 8
K_function_4[4][8][9] = 4
K_function_4[4][9][9] = 3

K_function_4[5][0][9] = 5
K_function_4[5][1][9] = 3
K_function_4[5][2][9] = 6
K_function_4[5][3][9] = 5
K_function_4[5][4][9] = 8
K_function_4[5][5][9] = 12
K_function_4[5][6][9] = 3
K_function_4[5][7][9] = 5
K_function_4[5][8][9] = 6
K_function_4[5][9][9] = 7

K_function_4[6][0][9] = 8
K_function_4[6][1][9] = 8
K_function_4[6][2][9] = 7
K_function_4[6][3][9] = 13
K_function_4[6][4][9] = 3
K_function_4[6][5][9] = 1
K_function_4[6][6][9] = 4
K_function_4[6][7][9] = 8
K_function_4[6][8][9] = 6
K_function_4[6][9][9] = 5

K_function_4[7][0][9] = 8
K_function_4[7][1][9] = 3
K_function_4[7][2][9] = 6
K_function_4[7][3][9] = 7
K_function_4[7][4][9] = 8
K_function_4[7][5][9] = 6
K_function_4[7][6][9] = 12
K_function_4[7][7][9] = 5
K_function_4[7][8][9] = 8
K_function_4[7][9][9] = 3

K_function_4[8][0][9] = 4
K_function_4[8][1][9] = 5
K_function_4[8][2][9] = 12
K_function_4[8][3][9] = 13
K_function_4[8][4][9] = 14
K_function_4[8][5][9] = 6
K_function_4[8][6][9] = 8
K_function_4[8][7][9] = 2
K_function_4[8][8][9] = 3
K_function_4[8][9][9] = 5

K_function_4[9][0][9] = 8
K_function_4[9][1][9] = 2
K_function_4[9][2][9] = 3
K_function_4[9][3][9] = 6
K_function_4[9][4][9] = 8
K_function_4[9][5][9] = 3
K_function_4[9][6][9] = 7
K_function_4[9][7][9] = 8
K_function_4[9][8][9] = 6
K_function_4[9][9][9] = 12







K_function_5 = np.zeros((10, 10, 10))

K_function_5[0][0][0] = 9
K_function_5[0][1][0] = 8
K_function_5[0][2][0] = 3
K_function_5[0][3][0] = 8
K_function_5[0][4][0] = 6
K_function_5[0][5][0] = 8
K_function_5[0][6][0] = 10
K_function_5[0][7][0] = 11
K_function_5[0][8][0] = 13
K_function_5[0][9][0] = 5

K_function_5[1][0][0] = 8
K_function_5[1][1][0] = 12
K_function_5[1][2][0] = 13
K_function_5[1][3][0] = 8
K_function_5[1][4][0] = 8
K_function_5[1][5][0] = 13
K_function_5[1][6][0] = 8
K_function_5[1][7][0] = 9
K_function_5[1][8][0] = 6
K_function_5[1][9][0] = 3

K_function_5[2][0][0] = 8
K_function_5[2][1][0] = 6
K_function_5[2][2][0] = 15
K_function_5[2][3][0] = 8
K_function_5[2][4][0] = 9
K_function_5[2][5][0] = 8
K_function_5[2][6][0] = 12
K_function_5[2][7][0] = 3
K_function_5[2][8][0] = 6
K_function_5[2][9][0] = 8


K_function_5[3][0][0] = 7
K_function_5[3][1][0] = 12
K_function_5[3][2][0] = 3
K_function_5[3][3][0] = 6
K_function_5[3][4][0] = 8
K_function_5[3][5][0] = 9
K_function_5[3][6][0] = 6
K_function_5[3][7][0] = 8
K_function_5[3][8][0] = 13
K_function_5[3][9][0] = 2


K_function_5[4][0][0] = 8
K_function_5[4][1][0] = 12
K_function_5[4][2][0] = 3
K_function_5[4][3][0] = 6
K_function_5[4][4][0] = 8
K_function_5[4][5][0] = 6
K_function_5[4][6][0] = 8
K_function_5[4][7][0] = 5
K_function_5[4][8][0] = 8
K_function_5[4][9][0] = 7

K_function_5[5][0][0] = 6
K_function_5[5][1][0] = 3
K_function_5[5][2][0] = 4
K_function_5[5][3][0] = 8
K_function_5[5][4][0] = 6
K_function_5[5][5][0] = 7
K_function_5[5][6][0] = 13
K_function_5[5][7][0] = 14
K_function_5[5][8][0] = 3
K_function_5[5][9][0] = 8

K_function_5[6][0][0] = 12
K_function_5[6][1][0] = 8
K_function_5[6][2][0] = 11
K_function_5[6][3][0] = 8
K_function_5[6][4][0] = 7
K_function_5[6][5][0] = 6
K_function_5[6][6][0] = 13
K_function_5[6][7][0] = 8
K_function_5[6][8][0] = 8
K_function_5[6][9][0] = 13

K_function_5[7][0][0] = 8
K_function_5[7][1][0] = 5
K_function_5[7][2][0] = 8
K_function_5[7][3][0] = 8
K_function_5[7][4][0] = 6
K_function_5[7][5][0] = 9
K_function_5[7][6][0] = 9
K_function_5[7][7][0] = 12
K_function_5[7][8][0] = 12
K_function_5[7][9][0] = 3

K_function_5[8][0][0] = 8
K_function_5[8][1][0] = 9
K_function_5[8][2][0] = 9
K_function_5[8][3][0] = 6
K_function_5[8][4][0] = 6
K_function_5[8][5][0] = 3
K_function_5[8][6][0] = 5
K_function_5[8][7][0] = 8
K_function_5[8][8][0] = 3
K_function_5[8][9][0] = 6

K_function_5[9][0][0] = 8
K_function_5[9][1][0] = 12
K_function_5[9][2][0] = 6
K_function_5[9][3][0] = 8
K_function_5[9][4][0] = 3
K_function_5[9][5][0] = 10
K_function_5[9][6][0] = 8
K_function_5[9][7][0] = 7
K_function_5[9][8][0] = 8
K_function_5[9][9][0] = 5


K_function_5[0][0][1] = 8
K_function_5[0][1][1] = 9
K_function_5[0][2][1] = 3
K_function_5[0][3][1] = 6
K_function_5[0][4][1] = 8
K_function_5[0][5][1] = 13
K_function_5[0][6][1] = 8
K_function_5[0][7][1] = 7
K_function_5[0][8][1] = 5
K_function_5[0][9][1] = 6

K_function_5[1][0][1] = 8
K_function_5[1][1][1] = 6
K_function_5[1][2][1] = 7
K_function_5[1][3][1] = 6
K_function_5[1][4][1] = 8
K_function_5[1][5][1] = 3
K_function_5[1][6][1] = 8
K_function_5[1][7][1] = 6
K_function_5[1][8][1] = 8
K_function_5[1][9][1] = 12

K_function_5[2][0][1] = 7
K_function_5[2][1][1] = 8
K_function_5[2][2][1] = 4
K_function_5[2][3][1] = 8
K_function_5[2][4][1] = 3
K_function_5[2][5][1] = 8
K_function_5[2][6][1] = 6
K_function_5[2][7][1] = 8
K_function_5[2][8][1] = 9
K_function_5[2][9][1] = 4


K_function_5[3][0][1] = 8
K_function_5[3][1][1] = 3
K_function_5[3][2][1] = 6
K_function_5[3][3][1] = 8
K_function_5[3][4][1] = 6
K_function_5[3][5][1] = 4
K_function_5[3][6][1] = 8
K_function_5[3][7][1] = 5
K_function_5[3][8][1] = 8
K_function_5[3][9][1] = 12


K_function_5[4][0][1] = 8
K_function_5[4][1][1] = 13
K_function_5[4][2][1] = 8
K_function_5[4][3][1] = 7
K_function_5[4][4][1] = 6
K_function_5[4][5][1] = 8
K_function_5[4][6][1] = 3
K_function_5[4][7][1] = 8
K_function_5[4][8][1] = 7
K_function_5[4][9][1] = 6

K_function_5[5][0][1] = 8
K_function_5[5][1][1] = 7
K_function_5[5][2][1] = 6
K_function_5[5][3][1] = 8
K_function_5[5][4][1] = 7
K_function_5[5][5][1] = 8
K_function_5[5][6][1] = 9
K_function_5[5][7][1] = 7
K_function_5[5][8][1] = 3
K_function_5[5][9][1] = 5

K_function_5[6][0][1] = 8
K_function_5[6][1][1] = 3
K_function_5[6][2][1] = 8
K_function_5[6][3][1] = 9
K_function_5[6][4][1] = 7
K_function_5[6][5][1] = 5
K_function_5[6][6][1] = 6
K_function_5[6][7][1] = 8
K_function_5[6][8][1] = 3
K_function_5[6][9][1] = 6

K_function_5[7][0][1] = 8
K_function_5[7][1][1] = 6
K_function_5[7][2][1] = 7
K_function_5[7][3][1] = 8
K_function_5[7][4][1] = 7
K_function_5[7][5][1] = 9
K_function_5[7][6][1] = 6
K_function_5[7][7][1] = 5
K_function_5[7][8][1] = 8
K_function_5[7][9][1] = 6

K_function_5[8][0][1] = 8
K_function_5[8][1][1] = 3
K_function_5[8][2][1] = 6
K_function_5[8][3][1] = 5
K_function_5[8][4][1] = 8
K_function_5[8][5][1] = 6
K_function_5[8][6][1] = 8
K_function_5[8][7][1] = 4
K_function_5[8][8][1] = 5
K_function_5[8][9][1] = 9

K_function_5[9][0][1] = 8
K_function_5[9][1][1] = 6
K_function_5[9][2][1] = 5
K_function_5[9][3][1] = 8
K_function_5[9][4][1] = 5
K_function_5[9][5][1] = 3
K_function_5[9][6][1] = 8
K_function_5[9][7][1] = 5
K_function_5[9][8][1] = 8
K_function_5[9][9][1] = 7
















K_function_5[0][0][2] = 8
K_function_5[0][1][2] = 5
K_function_5[0][2][2] = 3
K_function_5[0][3][2] = 6
K_function_5[0][4][2] = 8
K_function_5[0][5][2] = 3
K_function_5[0][6][2] = 5
K_function_5[0][7][2] = 8
K_function_5[0][8][2] = 6
K_function_5[0][9][2] = 9

K_function_5[1][0][2] = 8
K_function_5[1][1][2] = 3
K_function_5[1][2][2] = 8
K_function_5[1][3][2] = 6
K_function_5[1][4][2] = 8
K_function_5[1][5][2] = 7
K_function_5[1][6][2] = 8
K_function_5[1][7][2] = 9
K_function_5[1][8][2] = 3
K_function_5[1][9][2] = 6

K_function_5[2][0][2] = 8
K_function_5[2][1][2] = 6
K_function_5[2][2][2] = 8
K_function_5[2][3][2] = 4
K_function_5[2][4][2] = 5
K_function_5[2][5][2] = 3
K_function_5[2][6][2] = 6
K_function_5[2][7][2] = 8
K_function_5[2][8][2] = 6
K_function_5[2][9][2] = 8


K_function_5[3][0][2] = 5
K_function_5[3][1][2] = 8
K_function_5[3][2][2] = 9
K_function_5[3][3][2] = 6
K_function_5[3][4][2] = 8
K_function_5[3][5][2] = 5
K_function_5[3][6][2] = 7
K_function_5[3][7][2] = 13
K_function_5[3][8][2] = 5
K_function_5[3][9][2] = 8


K_function_5[4][0][2] = 9
K_function_5[4][1][2] = 7
K_function_5[4][2][2] = 6
K_function_5[4][3][2] = 8
K_function_5[4][4][2] = 3
K_function_5[4][5][2] = 6
K_function_5[4][6][2] = 8
K_function_5[4][7][2] = 4
K_function_5[4][8][2] = 8
K_function_5[4][9][2] = 13

K_function_5[5][0][2] = 5
K_function_5[5][1][2] = 8
K_function_5[5][2][2] = 7
K_function_5[5][3][2] = 8
K_function_5[5][4][2] = 6
K_function_5[5][5][2] = 8
K_function_5[5][6][2] = 7
K_function_5[5][7][2] = 8
K_function_5[5][8][2] = 3
K_function_5[5][9][2] = 6
K_function_5[6][0][2] = 8
K_function_5[6][1][2] = 5
K_function_5[6][2][2] = 7
K_function_5[6][3][2] = 6
K_function_5[6][4][2] = 8
K_function_5[6][5][2] = 6
K_function_5[6][6][2] = 8
K_function_5[6][7][2] = 5
K_function_5[6][8][2] = 14
K_function_5[6][9][2] = 8

K_function_5[7][0][2] = 7
K_function_5[7][1][2] = 3
K_function_5[7][2][2] = 8
K_function_5[7][3][2] = 6
K_function_5[7][4][2] = 8
K_function_5[7][5][2] = 7
K_function_5[7][6][2] = 9
K_function_5[7][7][2] = 6
K_function_5[7][8][2] = 8
K_function_5[7][9][2] = 3

K_function_5[8][0][2] = 7
K_function_5[8][1][2] = 8
K_function_5[8][2][2] = 4
K_function_5[8][3][2] = 3
K_function_5[8][4][2] = 3
K_function_5[8][5][2] = 6
K_function_5[8][6][2] = 6
K_function_5[8][7][2] = 8
K_function_5[8][8][2] = 7
K_function_5[8][9][2] = 6

K_function_5[9][0][2] = 8
K_function_5[9][1][2] = 8
K_function_5[9][2][2] = 8
K_function_5[9][3][2] = 7
K_function_5[9][4][2] = 6
K_function_5[9][5][2] = 6
K_function_5[9][6][2] = 3
K_function_5[9][7][2] = 8
K_function_5[9][8][2] = 7
K_function_5[9][9][2] = 6
















K_function_5[0][0][3] = 4
K_function_5[0][1][3] = 8
K_function_5[0][2][3] = 9
K_function_5[0][3][3] = 7
K_function_5[0][4][3] = 8
K_function_5[0][5][3] = 7
K_function_5[0][6][3] = 3
K_function_5[0][7][3] = 6
K_function_5[0][8][3] = 8
K_function_5[0][9][3] = 4

K_function_5[1][0][3] = 8
K_function_5[1][1][3] = 7
K_function_5[1][2][3] = 6
K_function_5[1][3][3] = 3
K_function_5[1][4][3] = 5
K_function_5[1][5][3] = 8
K_function_5[1][6][3] = 6
K_function_5[1][7][3] = 7
K_function_5[1][8][3] = 8
K_function_5[1][9][3] = 6

K_function_5[2][0][3] = 8
K_function_5[2][1][3] = 3
K_function_5[2][2][3] = 8
K_function_5[2][3][3] = 5
K_function_5[2][4][3] = 6
K_function_5[2][5][3] = 8
K_function_5[2][6][3] = 5
K_function_5[2][7][3] = 7
K_function_5[2][8][3] = 5
K_function_5[2][9][3] = 6


K_function_5[3][0][3] = 8
K_function_5[3][1][3] = 8
K_function_5[3][2][3] = 8
K_function_5[3][3][3] = 5
K_function_5[3][4][3] = 6
K_function_5[3][5][3] = 8
K_function_5[3][6][3] = 12
K_function_5[3][7][3] = 14
K_function_5[3][8][3] = 8
K_function_5[3][9][3] = 6

K_function_5[4][0][3] = 8
K_function_5[4][1][3] = 5
K_function_5[4][2][3] = 4
K_function_5[4][3][3] = 3
K_function_5[4][4][3] = 8
K_function_5[4][5][3] = 8
K_function_5[4][6][3] = 6
K_function_5[4][7][3] = 3
K_function_5[4][8][3] = 12
K_function_5[4][9][3] = 3

K_function_5[5][0][3] = 8
K_function_5[5][1][3] = 6
K_function_5[5][2][3] = 9
K_function_5[5][3][3] = 3
K_function_5[5][4][3] = 6
K_function_5[5][5][3] = 8
K_function_5[5][6][3] = 6
K_function_5[5][7][3] = 8
K_function_5[5][8][3] = 5
K_function_5[5][9][3] = 9

K_function_5[6][0][3] = 3
K_function_5[6][1][3] = 8
K_function_5[6][2][3] = 5
K_function_5[6][3][3] = 8
K_function_5[6][4][3] = 4
K_function_5[6][5][3] = 9
K_function_5[6][6][3] = 3
K_function_5[6][7][3] = 5
K_function_5[6][8][3] = 8
K_function_5[6][9][3] = 6

K_function_5[7][0][3] = 8
K_function_5[7][1][3] = 6
K_function_5[7][2][3] = 3
K_function_5[7][3][3] = 6
K_function_5[7][4][3] = 8
K_function_5[7][5][3] = 5
K_function_5[7][6][3] = 6
K_function_5[7][7][3] = 8
K_function_5[7][8][3] = 6
K_function_5[7][9][3] = 8

K_function_5[8][0][3] = 7
K_function_5[8][1][3] = 5
K_function_5[8][2][3] = 1
K_function_5[8][3][3] = 8
K_function_5[8][4][3] = 9
K_function_5[8][5][3] = 8
K_function_5[8][6][3] = 6
K_function_5[8][7][3] = 8
K_function_5[8][8][3] = 3
K_function_5[8][9][3] = 5

K_function_5[9][0][3] = 8
K_function_5[9][1][3] = 2
K_function_5[9][2][3] = 6
K_function_5[9][3][3] = 8
K_function_5[9][4][3] = 5
K_function_5[9][5][3] = 6
K_function_5[9][6][3] = 8
K_function_5[9][7][3] = 8
K_function_5[9][8][3] = 6
K_function_5[9][9][3] = 7















K_function_5[0][0][4] = 8
K_function_5[0][1][4] = 6
K_function_5[0][2][4] = 8
K_function_5[0][3][4] = 3
K_function_5[0][4][4] = 6
K_function_5[0][5][4] = 8
K_function_5[0][6][4] = 7
K_function_5[0][7][4] = 5
K_function_5[0][8][4] = 8
K_function_5[0][9][4] = 4

K_function_5[1][0][4] = 8
K_function_5[1][1][4] = 7
K_function_5[1][2][4] = 8
K_function_5[1][3][4] = 9
K_function_5[1][4][4] = 8
K_function_5[1][5][4] = 3
K_function_5[1][6][4] = 7
K_function_5[1][7][4] = 3
K_function_5[1][8][4] = 8
K_function_5[1][9][4] = 4

K_function_5[2][0][4] = 5
K_function_5[2][1][4] = 8
K_function_5[2][2][4] = 7
K_function_5[2][3][4] = 9
K_function_5[2][4][4] = 6
K_function_5[2][5][4] = 8
K_function_5[2][6][4] = 2
K_function_5[2][7][4] = 3
K_function_5[2][8][4] = 3
K_function_5[2][9][4] = 6


K_function_5[3][0][4] = 7
K_function_5[3][1][4] = 8
K_function_5[3][2][4] = 5
K_function_5[3][3][4] = 7
K_function_5[3][4][4] = 9
K_function_5[3][5][4] = 8
K_function_5[3][6][4] = 7
K_function_5[3][7][4] = 6
K_function_5[3][8][4] = 8
K_function_5[3][9][4] = 3


K_function_5[4][0][4] = 8
K_function_5[4][1][4] = 6
K_function_5[4][2][4] = 8
K_function_5[4][3][4] = 7
K_function_5[4][4][4] = 5
K_function_5[4][5][4] = 7
K_function_5[4][6][4] = 5
K_function_5[4][7][4] = 8
K_function_5[4][8][4] = 7
K_function_5[4][9][4] = 5

K_function_5[5][0][4] = 6
K_function_5[5][1][4] = 6
K_function_5[5][2][4] = 4
K_function_5[5][3][4] = 5
K_function_5[5][4][4] = 9
K_function_5[5][5][4] = 7
K_function_5[5][6][4] = 5
K_function_5[5][7][4] = 3
K_function_5[5][8][4] = 8
K_function_5[5][9][4] = 9

K_function_5[6][0][4] = 8
K_function_5[6][1][4] = 3
K_function_5[6][2][4] = 5
K_function_5[6][3][4] = 8
K_function_5[6][4][4] = 7
K_function_5[6][5][4] = 5
K_function_5[6][6][4] = 9
K_function_5[6][7][4] = 3
K_function_5[6][8][4] = 8
K_function_5[6][9][4] = 6

K_function_5[7][0][4] = 8
K_function_5[7][1][4] = 5
K_function_5[7][2][4] = 7
K_function_5[7][3][4] = 8
K_function_5[7][4][4] = 3
K_function_5[7][5][4] = 6
K_function_5[7][6][4] = 8
K_function_5[7][7][4] = 6
K_function_5[7][8][4] = 3
K_function_5[7][9][4] = 2

K_function_5[8][0][4] = 8
K_function_5[8][1][4] = 6
K_function_5[8][2][4] = 8
K_function_5[8][3][4] = 6
K_function_5[8][4][4] = 3
K_function_5[8][5][4] = 5
K_function_5[8][6][4] = 8
K_function_5[8][7][4] = 8
K_function_5[8][8][4] = 7
K_function_5[8][9][4] = 5

K_function_5[9][0][4] = 8
K_function_5[9][1][4] = 6
K_function_5[9][2][4] = 8
K_function_5[9][3][4] = 9
K_function_5[9][4][4] = 2
K_function_5[9][5][4] = 3
K_function_5[9][6][4] = 8
K_function_5[9][7][4] = 5
K_function_5[9][8][4] = 6
K_function_5[9][9][4] = 7



















K_function_5[0][0][5] = 3
K_function_5[0][1][5] = 5
K_function_5[0][2][5] = 8
K_function_5[0][3][5] = 6
K_function_5[0][4][5] = 8
K_function_5[0][5][5] = 8
K_function_5[0][6][5] = 5
K_function_5[0][7][5] = 6
K_function_5[0][8][5] = 8
K_function_5[0][9][5] = 14

K_function_5[1][0][5] = 8
K_function_5[1][1][5] = 6
K_function_5[1][2][5] = 7
K_function_5[1][3][5] = 2
K_function_5[1][4][5] = 3
K_function_5[1][5][5] = 5
K_function_5[1][6][5] = 8
K_function_5[1][7][5] = 7
K_function_5[1][8][5] = 6
K_function_5[1][9][5] = 8

K_function_5[2][0][5] = 7
K_function_5[2][1][5] = 8
K_function_5[2][2][5] = 7
K_function_5[2][3][5] = 6
K_function_5[2][4][5] = 8
K_function_5[2][5][5] = 3
K_function_5[2][6][5] = 8
K_function_5[2][7][5] = 6
K_function_5[2][8][5] = 8
K_function_5[2][9][5] = 7


K_function_5[3][0][5] = 6
K_function_5[3][1][5] = 4
K_function_5[3][2][5] = 3
K_function_5[3][3][5] = 5
K_function_5[3][4][5] = 8
K_function_5[3][5][5] = 8
K_function_5[3][6][5] = 6
K_function_5[3][7][5] = 8
K_function_5[3][8][5] = 7
K_function_5[3][9][5] = 13


K_function_5[4][0][5] = 8
K_function_5[4][1][5] = 5
K_function_5[4][2][5] = 9
K_function_5[4][3][5] = 6
K_function_5[4][4][5] = 8
K_function_5[4][5][5] = 6
K_function_5[4][6][5] = 8
K_function_5[4][7][5] = 3
K_function_5[4][8][5] = 8
K_function_5[4][9][5] = 6

K_function_5[5][0][5] = 8
K_function_5[5][1][5] = 3
K_function_5[5][2][5] = 6
K_function_5[5][3][5] = 8
K_function_5[5][4][5] = 7
K_function_5[5][5][5] = 3
K_function_5[5][6][5] = 5
K_function_5[5][7][5] = 8
K_function_5[5][8][5] = 6
K_function_5[5][9][5] = 8

K_function_5[6][0][5] = 3
K_function_5[6][1][5] = 7
K_function_5[6][2][5] = 9
K_function_5[6][3][5] = 12
K_function_5[6][4][5] = 6
K_function_5[6][5][5] = 8
K_function_5[6][6][5] = 6
K_function_5[6][7][5] = 8
K_function_5[6][8][5] = 1
K_function_5[6][9][5] = 3

K_function_5[7][0][5] = 8
K_function_5[7][1][5] = 6
K_function_5[7][2][5] = 8
K_function_5[7][3][5] = 5
K_function_5[7][4][5] = 6
K_function_5[7][5][5] = 8
K_function_5[7][6][5] = 6
K_function_5[7][7][5] = 14
K_function_5[7][8][5] = 8
K_function_5[7][9][5] = 3

K_function_5[8][0][5] = 8
K_function_5[8][1][5] = 9
K_function_5[8][2][5] = 4
K_function_5[8][3][5] = 5
K_function_5[8][4][5] = 8
K_function_5[8][5][5] = 3
K_function_5[8][6][5] = 9
K_function_5[8][7][5] = 8
K_function_5[8][8][5] = 7
K_function_5[8][9][5] = 8

K_function_5[9][0][5] = 6
K_function_5[9][1][5] = 9
K_function_5[9][2][5] = 3
K_function_5[9][3][5] = 8
K_function_5[9][4][5] = 5
K_function_5[9][5][5] = 6
K_function_5[9][6][5] = 8
K_function_5[9][7][5] = 9
K_function_5[9][8][5] = 6
K_function_5[9][9][5] = 8

















K_function_5[0][0][6] = 6
K_function_5[0][1][6] = 8
K_function_5[0][2][6] = 9
K_function_5[0][3][6] = 6
K_function_5[0][4][6] = 3
K_function_5[0][5][6] = 8
K_function_5[0][6][6] = 3
K_function_5[0][7][6] = 5
K_function_5[0][8][6] = 8
K_function_5[0][9][6] = 7

K_function_5[1][0][6] = 3
K_function_5[1][1][6] = 5
K_function_5[1][2][6] = 8
K_function_5[1][3][6] = 8
K_function_5[1][4][6] = 7
K_function_5[1][5][6] = 3
K_function_5[1][6][6] = 14
K_function_5[1][7][6] = 6
K_function_5[1][8][6] = 8
K_function_5[1][9][6] = 7

K_function_5[2][0][6] = 5
K_function_5[2][1][6] = 8
K_function_5[2][2][6] = 7
K_function_5[2][3][6] = 6
K_function_5[2][4][6] = 8
K_function_5[2][5][6] = 5
K_function_5[2][6][6] = 7
K_function_5[2][7][6] = 8
K_function_5[2][8][6] = 3
K_function_5[2][9][6] = 8


K_function_5[3][0][6] = 9
K_function_5[3][1][6] = 8
K_function_5[3][2][6] = 7
K_function_5[3][3][6] = 8
K_function_5[3][4][6] = 6
K_function_5[3][5][6] = 8
K_function_5[3][6][6] = 5
K_function_5[3][7][6] = 8
K_function_5[3][8][6] = 7
K_function_5[3][9][6] = 6


K_function_5[4][0][6] = 8
K_function_5[4][1][6] = 9
K_function_5[4][2][6] = 3
K_function_5[4][3][6] = 6
K_function_5[4][4][6] = 1
K_function_5[4][5][6] = 8
K_function_5[4][6][6] = 3
K_function_5[4][7][6] = 5
K_function_5[4][8][6] = 8
K_function_5[4][9][6] = 7

K_function_5[5][0][6] = 8
K_function_5[5][1][6] = 3
K_function_5[5][2][6] = 8
K_function_5[5][3][6] = 6
K_function_5[5][4][6] = 8
K_function_5[5][5][6] = 6
K_function_5[5][6][6] = 3
K_function_5[5][7][6] = 2
K_function_5[5][8][6] = 8
K_function_5[5][9][6] = 7

K_function_5[6][0][6] = 9
K_function_5[6][1][6] = 3
K_function_5[6][2][6] = 5
K_function_5[6][3][6] = 8
K_function_5[6][4][6] = 9
K_function_5[6][5][6] = 14
K_function_5[6][6][6] = 4
K_function_5[6][7][6] = 8
K_function_5[6][8][6] = 9
K_function_5[6][9][6] = 9

K_function_5[7][0][6] = 7
K_function_5[7][1][6] = 5
K_function_5[7][2][6] = 8
K_function_5[7][3][6] = 6
K_function_5[7][4][6] = 8
K_function_5[7][5][6] = 7
K_function_5[7][6][6] = 8
K_function_5[7][7][6] = 7
K_function_5[7][8][6] = 3
K_function_5[7][9][6] = 8

K_function_5[8][0][6] = 7
K_function_5[8][1][6] = 8
K_function_5[8][2][6] = 7
K_function_5[8][3][6] = 5
K_function_5[8][4][6] = 8
K_function_5[8][5][6] = 3
K_function_5[8][6][6] = 5
K_function_5[8][7][6] = 8
K_function_5[8][8][6] = 3
K_function_5[8][9][6] = 8

K_function_5[9][0][6] = 3
K_function_5[9][1][6] = 4
K_function_5[9][2][6] = 8
K_function_5[9][3][6] = 9
K_function_5[9][4][6] = 3
K_function_5[9][5][6] = 8
K_function_5[9][6][6] = 7
K_function_5[9][7][6] = 6
K_function_5[9][8][6] = 8
K_function_5[9][9][6] = 3


















K_function_5[0][0][7] = 5
K_function_5[0][1][7] = 8
K_function_5[0][2][7] = 7
K_function_5[0][3][7] = 5
K_function_5[0][4][7] = 4
K_function_5[0][5][7] = 8
K_function_5[0][6][7] = 3
K_function_5[0][7][7] = 8
K_function_5[0][8][7] = 7
K_function_5[0][9][7] = 3

K_function_5[1][0][7] = 6
K_function_5[1][1][7] = 8
K_function_5[1][2][7] = 7
K_function_5[1][3][7] = 12
K_function_5[1][4][7] = 10
K_function_5[1][5][7] = 3
K_function_5[1][6][7] = 6
K_function_5[1][7][7] = 8
K_function_5[1][8][7] = 7
K_function_5[1][9][7] = 4

K_function_5[2][0][7] = 8
K_function_5[2][1][7] = 9
K_function_5[2][2][7] = 3
K_function_5[2][3][7] = 8
K_function_5[2][4][7] = 4
K_function_5[2][5][7] = 7
K_function_5[2][6][7] = 5
K_function_5[2][7][7] = 6
K_function_5[2][8][7] = 8
K_function_5[2][9][7] = 3


K_function_5[3][0][7] = 8
K_function_5[3][1][7] = 5
K_function_5[3][2][7] = 8
K_function_5[3][3][7] = 6
K_function_5[3][4][7] = 8
K_function_5[3][5][7] = 7
K_function_5[3][6][7] = 6
K_function_5[3][7][7] = 8
K_function_5[3][8][7] = 12
K_function_5[3][9][7] = 13


K_function_5[4][0][7] = 5
K_function_5[4][1][7] = 8
K_function_5[4][2][7] = 6
K_function_5[4][3][7] = 3
K_function_5[4][4][7] = 8
K_function_5[4][5][7] = 7
K_function_5[4][6][7] = 5
K_function_5[4][7][7] = 3
K_function_5[4][8][7] = 6
K_function_5[4][9][7] = 8

K_function_5[5][0][7] = 7
K_function_5[5][1][7] = 5
K_function_5[5][2][7] = 8
K_function_5[5][3][7] = 9
K_function_5[5][4][7] = 3
K_function_5[5][5][7] = 5
K_function_5[5][6][7] = 8
K_function_5[5][7][7] = 7
K_function_5[5][8][7] = 5
K_function_5[5][9][7] = 3

K_function_5[6][0][7] = 8
K_function_5[6][1][7] = 7
K_function_5[6][2][7] = 6
K_function_5[6][3][7] = 7
K_function_5[6][4][7] = 8
K_function_5[6][5][7] = 6
K_function_5[6][6][7] = 5
K_function_5[6][7][7] = 8
K_function_5[6][8][7] = 3
K_function_5[6][9][7] = 4

K_function_5[7][0][7] = 8
K_function_5[7][1][7] = 7
K_function_5[7][2][7] = 6
K_function_5[7][3][7] = 8
K_function_5[7][4][7] = 9
K_function_5[7][5][7] = 8
K_function_5[7][6][7] = 3
K_function_5[7][7][7] = 4
K_function_5[7][8][7] = 7
K_function_5[7][9][7] = 8

K_function_5[8][0][7] = 6
K_function_5[8][1][7] = 15
K_function_5[8][2][7] = 8
K_function_5[8][3][7] = 12
K_function_5[8][4][7] = 6
K_function_5[8][5][7] = 1
K_function_5[8][6][7] = 8
K_function_5[8][7][7] = 3
K_function_5[8][8][7] = 9
K_function_5[8][9][7] = 7

K_function_5[9][0][7] = 7
K_function_5[9][1][7] = 8
K_function_5[9][2][7] = 1
K_function_5[9][3][7] = 3
K_function_5[9][4][7] = 6
K_function_5[9][5][7] = 8
K_function_5[9][6][7] = 7
K_function_5[9][7][7] = 6
K_function_5[9][8][7] = 7
K_function_5[9][9][7] = 8














K_function_5[0][0][8] = 5
K_function_5[0][1][8] = 8
K_function_5[0][2][8] = 3
K_function_5[0][3][8] = 8
K_function_5[0][4][8] = 6
K_function_5[0][5][8] = 8
K_function_5[0][6][8] = 7
K_function_5[0][7][8] = 3
K_function_5[0][8][8] = 8
K_function_5[0][9][8] = 7

K_function_5[1][0][8] = 3
K_function_5[1][1][8] = 6
K_function_5[1][2][8] = 8
K_function_5[1][3][8] = 5
K_function_5[1][4][8] = 8
K_function_5[1][5][8] = 9
K_function_5[1][6][8] = 3
K_function_5[1][7][8] = 8
K_function_5[1][8][8] = 6
K_function_5[1][9][8] = 8

K_function_5[2][0][8] = 7
K_function_5[2][1][8] = 6
K_function_5[2][2][8] = 8
K_function_5[2][3][8] = 6
K_function_5[2][4][8] = 5
K_function_5[2][5][8] = 8
K_function_5[2][6][8] = 13
K_function_5[2][7][8] = 8
K_function_5[2][8][8] = 9
K_function_5[2][9][8] = 5


K_function_5[3][0][8] = 8
K_function_5[3][1][8] = 3
K_function_5[3][2][8] = 6
K_function_5[3][3][8] = 8
K_function_5[3][4][8] = 5
K_function_5[3][5][8] = 9
K_function_5[3][6][8] = 7
K_function_5[3][7][8] = 5
K_function_5[3][8][8] = 6
K_function_5[3][9][8] = 8


K_function_5[4][0][8] = 5
K_function_5[4][1][8] = 8
K_function_5[4][2][8] = 3
K_function_5[4][3][8] = 8
K_function_5[4][4][8] = 13
K_function_5[4][5][8] = 8
K_function_5[4][6][8] = 4
K_function_5[4][7][8] = 6
K_function_5[4][8][8] = 5
K_function_5[4][9][8] = 14

K_function_5[5][0][8] = 8
K_function_5[5][1][8] = 9
K_function_5[5][2][8] = 7
K_function_5[5][3][8] = 3
K_function_5[5][4][8] = 6
K_function_5[5][5][8] = 8
K_function_5[5][6][8] = 13
K_function_5[5][7][8] = 10
K_function_5[5][8][8] = 8
K_function_5[5][9][8] = 9

K_function_5[6][0][8] = 8
K_function_5[6][1][8] = 3
K_function_5[6][2][8] = 6
K_function_5[6][3][8] = 8
K_function_5[6][4][8] = 7
K_function_5[6][5][8] = 6
K_function_5[6][6][8] = 14
K_function_5[6][7][8] = 5
K_function_5[6][8][8] = 8
K_function_5[6][9][8] = 7

K_function_5[7][0][8] = 8
K_function_5[7][1][8] = 3
K_function_5[7][2][8] = 8
K_function_5[7][3][8] = 15
K_function_5[7][4][8] = 9
K_function_5[7][5][8] = 8
K_function_5[7][6][8] = 3
K_function_5[7][7][8] = 8
K_function_5[7][8][8] = 7
K_function_5[7][9][8] = 8

K_function_5[8][0][8] = 3
K_function_5[8][1][8] = 6
K_function_5[8][2][8] = 8
K_function_5[8][3][8] = 9
K_function_5[8][4][8] = 8
K_function_5[8][5][8] = 6
K_function_5[8][6][8] = 5
K_function_5[8][7][8] = 8
K_function_5[8][8][8] = 6
K_function_5[8][9][8] = 8

K_function_5[9][0][8] = 5
K_function_5[9][1][8] = 6
K_function_5[9][2][8] = 8
K_function_5[9][3][8] = 7
K_function_5[9][4][8] = 9
K_function_5[9][5][8] = 9
K_function_5[9][6][8] = 8
K_function_5[9][7][8] = 6
K_function_5[9][8][8] = 8
K_function_5[9][9][8] = 7












K_function_5[0][0][9] = 8
K_function_5[0][1][9] = 6
K_function_5[0][2][9] = 8
K_function_5[0][3][9] = 13
K_function_5[0][4][9] = 5
K_function_5[0][5][9] = 13
K_function_5[0][6][9] = 14
K_function_5[0][7][9] = 15
K_function_5[0][8][9] = 8
K_function_5[0][9][9] = 9

K_function_5[1][0][9] = 8
K_function_5[1][1][9] = 8
K_function_5[1][2][9] = 2
K_function_5[1][3][9] = 8
K_function_5[1][4][9] = 9
K_function_5[1][5][9] = 6
K_function_5[1][6][9] = 8
K_function_5[1][7][9] = 7
K_function_5[1][8][9] = 9
K_function_5[1][9][9] = 3

K_function_5[2][0][9] = 8
K_function_5[2][1][9] = 7
K_function_5[2][2][9] = 5
K_function_5[2][3][9] = 6
K_function_5[2][4][9] = 8
K_function_5[2][5][9] = 9
K_function_5[2][6][9] = 3
K_function_5[2][7][9] = 6
K_function_5[2][8][9] = 8
K_function_5[2][9][9] = 5


K_function_5[3][0][9] = 3
K_function_5[3][1][9] = 6
K_function_5[3][2][9] = 8
K_function_5[3][3][9] = 9
K_function_5[3][4][9] = 5
K_function_5[3][5][9] = 6
K_function_5[3][6][9] = 5
K_function_5[3][7][9] = 8
K_function_5[3][8][9] = 6
K_function_5[3][9][9] = 8


K_function_5[4][0][9] = 6
K_function_5[4][1][9] = 5
K_function_5[4][2][9] = 8
K_function_5[4][3][9] = 9
K_function_5[4][4][9] = 8
K_function_5[4][5][9] = 6
K_function_5[4][6][9] = 5
K_function_5[4][7][9] = 8
K_function_5[4][8][9] = 6
K_function_5[4][9][9] = 8

K_function_5[5][0][9] = 9
K_function_5[5][1][9] = 8
K_function_5[5][2][9] = 13
K_function_5[5][3][9] = 5
K_function_5[5][4][9] = 14
K_function_5[5][5][9] = 4
K_function_5[5][6][9] = 7
K_function_5[5][7][9] = 8
K_function_5[5][8][9] = 9
K_function_5[5][9][9] = 9

K_function_5[6][0][9] = 6
K_function_5[6][1][9] = 8
K_function_5[6][2][9] = 7
K_function_5[6][3][9] = 9
K_function_5[6][4][9] = 6
K_function_5[6][5][9] = 8
K_function_5[6][6][9] = 8
K_function_5[6][7][9] = 9
K_function_5[6][8][9] = 8
K_function_5[6][9][9] = 5

K_function_5[7][0][9] = 7
K_function_5[7][1][9] = 5
K_function_5[7][2][9] = 8
K_function_5[7][3][9] = 9
K_function_5[7][4][9] = 7
K_function_5[7][5][9] = 8
K_function_5[7][6][9] = 5
K_function_5[7][7][9] = 13
K_function_5[7][8][9] = 7
K_function_5[7][9][9] = 8

K_function_5[8][0][9] = 7
K_function_5[8][1][9] = 5
K_function_5[8][2][9] = 8
K_function_5[8][3][9] = 6
K_function_5[8][4][9] = 9
K_function_5[8][5][9] = 8
K_function_5[8][6][9] = 5
K_function_5[8][7][9] = 7
K_function_5[8][8][9] = 8
K_function_5[8][9][9] = 7

K_function_5[9][0][9] = 8
K_function_5[9][1][9] = 3
K_function_5[9][2][9] = 5
K_function_5[9][3][9] = 6
K_function_5[9][4][9] = 8
K_function_5[9][5][9] = 9
K_function_5[9][6][9] = 8
K_function_5[9][7][9] = 5
K_function_5[9][8][9] = 8
K_function_5[9][9][9] = 7








K_function_6 = np.zeros((10, 10))

K_function_6[0][0] = 5
K_function_6[0][1] = 8
K_function_6[0][2] = 9
K_function_6[0][3] = 7
K_function_6[0][4] = 13
K_function_6[0][5] = 12
K_function_6[0][6] = 10
K_function_6[0][7] = 9
K_function_6[0][8] = 8
K_function_6[0][9] = 3

K_function_6[1][0] = 8
K_function_6[1][1] = 12
K_function_6[1][2] = 8
K_function_6[1][3] = 9
K_function_6[1][4] = 3
K_function_6[1][5] = 1
K_function_6[1][6] = 2
K_function_6[1][7] = 8
K_function_6[1][8] = 3
K_function_6[1][9] = 8

K_function_6[2][0] = 7
K_function_6[2][1] = 4
K_function_6[2][2] = 8
K_function_6[2][3] = 8
K_function_6[2][4] = 3
K_function_6[2][5] = 6
K_function_6[2][6] = 4
K_function_6[2][7] = 7
K_function_6[2][8] = 5
K_function_6[2][9] = 7

K_function_6[3][0] = 3
K_function_6[3][1] = 6
K_function_6[3][2] = 8
K_function_6[3][3] = 4
K_function_6[3][4] = 8
K_function_6[3][5] = 8
K_function_6[3][6] = 3
K_function_6[3][7] = 4
K_function_6[3][8] = 8
K_function_6[3][9] = 6


K_function_6[4][0] = 7
K_function_6[4][1] = 13
K_function_6[4][2] = 5
K_function_6[4][3] = 7
K_function_6[4][4] = 3
K_function_6[4][5] = 7
K_function_6[4][6] = 5
K_function_6[4][7] = 6
K_function_6[4][8] = 1
K_function_6[4][9] = 8

K_function_6[5][0] = 13
K_function_6[5][1] = 5
K_function_6[5][2] = 2
K_function_6[5][3] = 8
K_function_6[5][4] = 7
K_function_6[5][5] = 5
K_function_6[5][6] = 15
K_function_6[5][7] = 6
K_function_6[5][8] = 8
K_function_6[5][9] = 14

K_function_6[6][0] = 8
K_function_6[6][1] = 7
K_function_6[6][2] = 6
K_function_6[6][3] = 6
K_function_6[6][4] = 1
K_function_6[6][5] = 8
K_function_6[6][6] = 6
K_function_6[6][7] = 7
K_function_6[6][8] = 9
K_function_6[6][9] = 1

K_function_6[7][0] = 5
K_function_6[7][1] = 3
K_function_6[7][2] = 5
K_function_6[7][3] = 6
K_function_6[7][4] = 7
K_function_6[7][5] = 3
K_function_6[7][6] = 1
K_function_6[7][7] = 4
K_function_6[7][8] = 5
K_function_6[7][9] = 6

K_function_6[8][0] = 7
K_function_6[8][1] = 8
K_function_6[8][2] = 5
K_function_6[8][3] = 7
K_function_6[8][4] = 5
K_function_6[8][5] = 8
K_function_6[8][6] = 13
K_function_6[8][7] = 7
K_function_6[8][8] = 8
K_function_6[8][9] = 4

K_function_6[9][0] = 2
K_function_6[9][1] = 1
K_function_6[9][2] = 8
K_function_6[9][3] = 8
K_function_6[9][4] = 3
K_function_6[9][5] = 5
K_function_6[9][6] = 7
K_function_6[9][7] = 5
K_function_6[9][8] = 8
K_function_6[9][9] = 3




first_strategy_list = np.zeros(N)

max_element = K_function_1.max()
for first_player_counter in range(0, len(first_player_strategies)):
    for second_player_counter in range(0, len(second_player_strategies)):
        if(K_function_1[first_player_counter][second_player_counter] == max_element):
            first_strategy_index = first_player_counter
            second_strategy_index = second_player_counter


first_strategy_list[0] = first_strategy_index
first_strategy_list[1] = second_strategy_index









K_max_3 = 0
second_index = int(first_strategy_list[1])
for third_player_counter in range(0, len(third_player_strategies)):
    for forth_player_counter in range(0, len(forth_player_strategies)):
        w = int(K_function_3[second_index][int(third_player_counter)][int(forth_player_counter)])

        if(w > int(K_max_3)):
            K_max_3 = w
            forth_strategy_index = forth_player_counter
            third_strategy_index = third_player_counter
        
first_strategy_list[2] = third_strategy_index
first_strategy_list[3] = forth_strategy_index





K_max_5 = 0
for fifth_player_counter in range(0, len(fifth_player_strategies)):
    for sixth_player_counter in range(0, len(sixth_player_strategies)):
        forth_index = int(first_strategy_list[3])
        w = int(K_function_5[forth_index][int(fifth_player_counter)][int(sixth_player_counter)])

        if(w > int(K_max_5)):
            K_max_5 = w
            fifth_strategy_index = fifth_player_counter
            sixth_strategy_index = sixth_player_counter
        
first_strategy_list[4] = fifth_strategy_index
first_strategy_list[5] = sixth_strategy_index

K_max_2 = K_function_2[int(first_strategy_list[0])][int(first_strategy_list[1])][int(first_strategy_list[2])]
K_max_3 = K_function_3[int(first_strategy_list[1])][int(first_strategy_list[2])][int(first_strategy_list[3])]
K_max_4 = K_function_4[int(first_strategy_list[2])][int(first_strategy_list[3])][int(first_strategy_list[4])]
K_max_5 = K_function_5[int(first_strategy_list[3])][int(first_strategy_list[4])][int(first_strategy_list[5])]
K_max_6 = K_function_6[int(first_strategy_list[4])][int(first_strategy_list[5])]

index_first_player = int(first_strategy_list[0])
index_second_player = int(first_strategy_list[1])
index_third_player = int(first_strategy_list[2])
K_2 = K_function_2[index_first_player][index_second_player][index_third_player]
u = 0
player_2_pairs = list()
player_2_meanings = list()


for first_player_counter in range(0, len(first_player_strategies)):
    for second_player_counter in range(0, len(second_player_strategies)):
        for third_player_counter in range(0, len(third_player_strategies)):
            
            
            if(K_function_2[first_player_counter][second_player_counter][third_player_counter] > K_2):
                player_2_meanings.append(K_function_2[first_player_counter][second_player_counter][third_player_counter])
                temple_list_player_2 = list()
                temple_list_player_2.append(first_player_counter)
                temple_list_player_2.append(second_player_counter)
                temple_list_player_2.append(third_player_counter)
                u = u + 1
                player_2_pairs.append(temple_list_player_2)



                
                
index_second_player = int(first_strategy_list[1])
index_third_player = int(first_strategy_list[2])
index_forth_player = int(first_strategy_list[3])
K_3 = K_function_3[index_second_player][index_third_player][index_forth_player]
u = 0
player_3_pairs = list()
player_3_meanings = list()


for second_player_counter in range(0, len(second_player_strategies)):
    for third_player_counter in range(0, len(third_player_strategies)):
        for forth_player_counter in range(0, len(forth_player_strategies)):
            
            
            if(K_function_3[second_player_counter][third_player_counter][forth_player_counter] > K_3):
                player_3_meanings.append(K_function_3[second_player_counter][third_player_counter][forth_player_counter])
                temple_list_player_2 = list()
                temple_list_player_2.append(second_player_counter)
                temple_list_player_2.append(third_player_counter)
                temple_list_player_2.append(forth_player_counter)
                u = u + 1
                player_3_pairs.append(temple_list_player_2)


                
                


index_third_player = int(first_strategy_list[2])
index_forth_player = int(first_strategy_list[3])
index_fifth_player = int(first_strategy_list[4])
K_4 = K_function_4[index_third_player][index_forth_player][index_fifth_player]
u = 0
player_4_pairs = list()
player_4_meanings = list()


for third_player_counter in range(0, len(third_player_strategies)):
    for forth_player_counter in range(0, len(forth_player_strategies)):
        for fifth_player_counter in range(0, len(fifth_player_strategies)):
            
            
            if(K_function_4[third_player_counter][forth_player_counter][fifth_player_counter] > K_4):
                player_4_meanings.append(K_function_4[third_player_counter][forth_player_counter][fifth_player_counter])
                temple_list_player_2 = list()
                temple_list_player_2.append(third_player_counter)
                temple_list_player_2.append(forth_player_counter)
                temple_list_player_2.append(fifth_player_counter)
                u = u + 1
                player_4_pairs.append(temple_list_player_2)
                
                
                
                
                
                
index_forth_player = int(first_strategy_list[3])
index_fifth_player = int(first_strategy_list[4])
index_sixth_player = int(first_strategy_list[5])
K_5 = K_function_5[index_forth_player][index_fifth_player][index_sixth_player]
u = 0
player_5_pairs = list()
player_5_meanings = list()


for forth_player_counter in range(0, len(forth_player_strategies)):
    for fifth_player_counter in range(0, len(fifth_player_strategies)):
        for sixth_player_counter in range(0, len(sixth_player_strategies)):
            
            
            if(K_function_5[forth_player_counter][fifth_player_counter][sixth_player_counter] > K_5):
                player_5_meanings.append(K_function_5[forth_player_counter][fifth_player_counter][sixth_player_counter])
                temple_list_player_2 = list()
                temple_list_player_2.append(forth_player_counter)
                temple_list_player_2.append(fifth_player_counter)
                temple_list_player_2.append(sixth_player_counter)
                u = u + 1
                player_5_pairs.append(temple_list_player_2)
                
                
                
                
index_forth_player = int(first_strategy_list[3])
index_fifth_player = int(first_strategy_list[4])
index_sixth_player = int(first_strategy_list[5])
K_6 = K_function_6[index_fifth_player][index_sixth_player]
u = 0
player_6_pairs = list()
player_6_meanings = list()



for fifth_player_counter in range(0, len(fifth_player_strategies)):
    for sixth_player_counter in range(0, len(sixth_player_strategies)):
        
        if(K_function_6[fifth_player_counter][sixth_player_counter] > K_6):
            player_6_meanings.append(K_function_6[fifth_player_counter][sixth_player_counter])
            temple_list_player_2 = list()
            temple_list_player_2.append(fifth_player_counter)
            temple_list_player_2.append(sixth_player_counter)
            u = u + 1
            player_6_pairs.append(temple_list_player_2)



K_max_6 = K_function_6[int(first_strategy_list[4])][int(first_strategy_list[5])]
#print(u)

K_first_strategy_max = max_element + K_max_2 + K_max_3 + K_max_4 + K_max_5 + K_max_6

final_strategies_list = list()
K_max_final = list()
counter_for_second_player = 0

for main_counter_j in range (0, len(player_2_pairs)):
    first_strategy_i = int(player_2_pairs[main_counter_j][0])
    second_strategy_i = int(player_2_pairs[main_counter_j][1])
    third_strategy_i = int(player_2_pairs[main_counter_j][2])

    for forth_player_counter in range(0, len(forth_player_strategies)):
        for fifth_player_counter in range(0, len(fifth_player_strategies)):
            for sixth_player_counter in range(0, len(sixth_player_strategies)):
                K_all = K_function_1[first_strategy_i][second_strategy_i] + K_function_2[first_strategy_i][second_strategy_i][third_strategy_i] + K_function_3[second_strategy_i][third_strategy_i][forth_player_counter] + K_function_4[third_strategy_i][forth_player_counter][fifth_player_counter] + K_function_5[forth_player_counter][fifth_player_counter][sixth_player_counter] + K_function_6[fifth_player_counter][sixth_player_counter]
                counter_for_second_player += 1
                if(K_all > K_first_strategy_max):
                    temple_strategies_list = list()
                    K_max_final.append(K_all)
                    temple_strategies_list.append(first_strategy_i)
                    temple_strategies_list.append(second_strategy_i)
                    temple_strategies_list.append(third_strategy_i)
                    temple_strategies_list.append(forth_player_counter)
                    temple_strategies_list.append(fifth_player_counter)
                    temple_strategies_list.append(sixth_player_counter)
                    final_strategies_list.append(temple_strategies_list)
                    
                    
                    
                    
                    
                    
for main_counter_j in range (0, len(player_3_pairs)):
    second_strategy_i = int(player_3_pairs[main_counter_j][0])
    third_strategy_i = int(player_3_pairs[main_counter_j][1])
    forth_strategy_i = int(player_3_pairs[main_counter_j][2])

    for first_player_counter in range(0, len(first_player_strategies)):
        for fifth_player_counter in range(0, len(fifth_player_strategies)):
            for sixth_player_counter in range(0, len(sixth_player_strategies)):
                K_all = K_function_1[first_player_counter][second_strategy_i] + K_function_2[first_player_counter][second_strategy_i][third_strategy_i] + K_function_3[second_strategy_i][third_strategy_i][forth_strategy_i] + K_function_4[third_strategy_i][forth_strategy_i][fifth_player_counter] + K_function_5[forth_strategy_i][fifth_player_counter][sixth_player_counter] + K_function_6[fifth_player_counter][sixth_player_counter]
                counter_for_second_player += 1
                if(K_all > K_first_strategy_max):
                    temple_strategies_list = list()
                    K_max_final.append(K_all)
                    temple_strategies_list.append(first_player_counter)
                    temple_strategies_list.append(second_strategy_i)
                    temple_strategies_list.append(third_strategy_i)
                    temple_strategies_list.append(forth_strategy_i)
                    temple_strategies_list.append(fifth_player_counter)
                    temple_strategies_list.append(sixth_player_counter)
                    final_strategies_list.append(temple_strategies_list)
print(counter_for_second_player)                 
                    

for main_counter_j in range (0, len(player_4_pairs)):
    third_strategy_i = int(player_4_pairs[main_counter_j][0])
    forth_strategy_i = int(player_4_pairs[main_counter_j][1])
    fifth_strategy_i = int(player_4_pairs[main_counter_j][2])

    for first_player_counter in range(0, len(first_player_strategies)):
        for second_player_counter in range(0, len(second_player_strategies)):
            for sixth_player_counter in range(0, len(sixth_player_strategies)):
                K_all = K_function_1[first_player_counter][second_player_counter] + K_function_2[first_player_counter][second_player_counter][third_strategy_i] + K_function_3[second_player_counter][third_strategy_i][forth_strategy_i] + K_function_4[third_strategy_i][forth_strategy_i][fifth_strategy_i] + K_function_5[forth_strategy_i][fifth_strategy_i][sixth_player_counter] + K_function_6[fifth_strategy_i][sixth_player_counter]
                counter_for_second_player += 1
                if(K_all > K_first_strategy_max):
                    temple_strategies_list = list()
                    K_max_final.append(K_all)
                    temple_strategies_list.append(first_player_counter)
                    temple_strategies_list.append(second_player_counter)
                    temple_strategies_list.append(third_strategy_i)
                    temple_strategies_list.append(forth_strategy_i)
                    temple_strategies_list.append(fifth_strategy_i)
                    temple_strategies_list.append(sixth_player_counter)
                    final_strategies_list.append(temple_strategies_list)


                    
                    
                    
for main_counter_j in range (0, len(player_5_pairs)):
    forth_strategy_i = int(player_5_pairs[main_counter_j][0])
    fifth_strategy_i = int(player_5_pairs[main_counter_j][1])
    sixth_strategy_i = int(player_5_pairs[main_counter_j][2])

    for first_player_counter in range(0, len(first_player_strategies)):
        for second_player_counter in range(0, len(second_player_strategies)):
            for third_player_counter in range(0, len(third_player_strategies)):
                K_all = K_function_1[first_player_counter][second_player_counter] + K_function_2[first_player_counter][second_player_counter][third_player_counter] + K_function_3[second_player_counter][third_player_counter][forth_strategy_i] + K_function_4[third_player_counter][forth_strategy_i][fifth_strategy_i] + K_function_5[forth_strategy_i][fifth_strategy_i][sixth_strategy_i] + K_function_6[fifth_strategy_i][sixth_strategy_i]
                counter_for_second_player += 1
                if(K_all > K_first_strategy_max):
                    temple_strategies_list = list()
                    K_max_final.append(K_all)
                    temple_strategies_list.append(first_player_counter)
                    temple_strategies_list.append(second_player_counter)
                    temple_strategies_list.append(third_player_counter)
                    temple_strategies_list.append(forth_strategy_i)
                    temple_strategies_list.append(fifth_strategy_i)
                    temple_strategies_list.append(sixth_strategy_i)
                    final_strategies_list.append(temple_strategies_list)   
                    
                    
                    
                    
print(counter_for_second_player)
                    
for main_counter_j in range (0, len(player_6_pairs)):
    
    fifth_strategy_i = int(player_6_pairs[main_counter_j][0])
    sixth_strategy_i = int(player_6_pairs[main_counter_j][1])
    
    for first_player_counter in range(0, len(first_player_strategies)):
        for second_player_counter in range(0, len(second_player_strategies)):
            for third_player_counter in range(0, len(third_player_strategies)):
                for forth_player_counter in range(0, len(forth_player_strategies)):
                    K_all = K_function_1[first_player_counter][second_player_counter] + K_function_2[first_player_counter][second_player_counter][third_player_counter] + K_function_3[second_player_counter][third_player_counter][forth_player_counter] + K_function_4[third_player_counter][forth_player_counter][fifth_strategy_i] + K_function_5[forth_player_counter][fifth_strategy_i][sixth_player_counter]
                    counter_for_second_player += 1
                    if(K_all > K_first_strategy_max):
                        temple_strategies_list = list()
                        K_max_final.append(K_all)
                        temple_strategies_list.append(first_player_counter)
                        temple_strategies_list.append(second_player_counter)
                        temple_strategies_list.append(third_player_counter)
                        temple_strategies_list.append(forth_player_counter)
                        temple_strategies_list.append(fifth_strategy_i)
                        temple_strategies_list.append(sixth_strategy_i)
                        final_strategies_list.append(temple_strategies_list)



max_element_final = int(max(K_max_final))
max_element_final_index = K_max_final.index(max_element_final)
print("max sum: ")
print(max_element_final)
print("strategy: ")
#print(max_element_final_index)
print(final_strategies_list[max_element_final_index])
print("number of iterations: ")
print(counter_for_second_player)

print(first_strategy_list)


# In[10]:


print(len(player_5_pairs))

