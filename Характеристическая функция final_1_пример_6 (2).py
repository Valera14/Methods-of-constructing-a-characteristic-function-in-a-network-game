
# coding: utf-8

# In[1]:


import numpy as np
N = 3
L = list()
N_links = np.zeros([N, N])
c_cost = np.zeros([N, N])

N_links[0][0] = 0
N_links[1][0] = 1
N_links[2][0] = 1
#N_links[3][0] = 1

N_links[0][1] = 1
N_links[1][1] = 0
N_links[2][1] = 1
#N_links[3][1] = 1

N_links[0][2] = 1
N_links[1][2] = 1
N_links[2][2] = 0
#N_links[3][2] = 0

#N_links[0][3] = 1
#N_links[1][3] = 1
#N_links[2][3] = 0
#N_links[3][3] = 0


c_cost[0][0] = 0
c_cost[1][0] = 4
c_cost[2][0] = 8


#c_cost[5][0] = 8
#c_cost[3][0] = 5

c_cost[0][1] = 4
c_cost[1][1] = 0
c_cost[2][1] = 3

#c_cost[5][1] = 32
#c_cost[3][1] = 19

c_cost[0][2] = 8
c_cost[1][2] = 3
c_cost[2][2] = 0

#c_cost[5][2] = 3


#c_cost[5][4] = 7


#c_cost[3][2] = 0

#c_cost[0][3] = 5
#c_cost[1][3] = 19
#c_cost[2][3] = 0
#c_cost[3][3] = 0

L.append(1)
L.append(1)
L.append(1)

#L.append(3)


#L.append(2)

C = list()
C_n = list()

for i in range(0, N):
    for k in range(0, N):
        if(c_cost[k][i] != 0):
            C.append([k, i])

   

n = len(C)
for u in range(0,n):
    C_n.append(u)

    
for i in range (0, n):
    for k in range(0, n):
        if(C[i][0] == C[k][1] and C[i][1] == C[k][0]):
            if(C_n[i] != C_n[k]):
                C_n[k] = C_n[i]
                
                

myset = set(C_n)
C_n_unique = list(myset)

level = list()
level.append(C_n_unique)
Main_matrix = list()
Main_matrix.append(level)
level = list()
for t_l in range(0, len(C_n_unique)-1):
    for y_l in range(0, len(Main_matrix[t_l])):
        for k_l in range(0, len(Main_matrix[t_l][y_l])-1):
            temple_y = Main_matrix[t_l][y_l][0:k_l+1] + Main_matrix[t_l][y_l][k_l+2:]
            level.append(temple_y)
        level.append(Main_matrix[t_l][y_l][1:])
    Main_matrix.append(level)
    level = list()
    
    
T = list()
T.append(2)
for o in range(1, len(C_n_unique)-1):
    T.append((T[0]+o)*(T[o-1]))
    
    
    


counter_f = 0
w = 0
Variants_matrix = list()
for index_o in Main_matrix[len(C_n_unique)-1]:
    path_list = list()
    path_list.append(index_o[0])
    h = len(C_n_unique)-1
    temple_ui = list()
    for p_i in range(1, len(C_n_unique)):
        Main_matrix[h-p_i][0]
        number = 0
        number = counter_f // T[p_i-1]
        temple_ui.append(Main_matrix[h-p_i][number])
    value_gotten = list(set(temple_ui[0]) - set(index_o))
    path_list.append(int(value_gotten[0]))
    for j in range(1, len(temple_ui)):
        value_gotten = list(set(temple_ui[j]) - set(temple_ui[j-1]))
        path_list.append(int(value_gotten[0]))
    path_list.reverse()
    Variants_matrix.append(path_list)
    counter_f = counter_f + 1
    
    
#print(Variants_matrix)
    


Final_sum = list()
Final_paths = list()
C_sum_list = list()
import random
C_temple = list()
C_n_temple = list()
L_temple = list()
for main_counter in range(0, len(Variants_matrix)):
    #print(main_counter)
    C_temple = list()
    C_n_temple = list()
    L_temple = list()
    L_temple = list()
    for t1 in range(0, len(C)):
        C_temple.append(C[t1])
        
    for t2 in range(0, len(C_n)):
        C_n_temple.append(C_n[t2])
    
    for t3 in range(0, len(L)):
        L_temple.append(L[t3])
    
    C_sum = 0
    
    k_temple_counter = 0
    index_path = list()
    while(len(C_n_temple) != 0):
        
        temple_list_variants_matrix = Variants_matrix[main_counter]
        
        
        po_counter = 0
        for gl in C_n_temple:
            if(gl == temple_list_variants_matrix[k_temple_counter]):
                po_counter = po_counter + 1
        if(po_counter == 0):
            break
        
        
        random_number = C_n_temple.index(temple_list_variants_matrix[k_temple_counter])
        k_temple_counter = k_temple_counter + 1
        
        

        row_index = C_temple[random_number][0]
        column_index = C_temple[random_number][1]
        
        C_n_temple_removed = C_n_temple[random_number]
        
        i = C_temple[random_number][0]
        j = C_temple[random_number][1]
        index_path.append([i,j])
        
        del C_n_temple[random_number]
        
        C_sum = C_sum + c_cost[C_temple[random_number][0]][C_temple[random_number][1]]
        del C_temple[random_number]
        
        temple_index = C_n_temple.index(C_n_temple_removed)
        
        del C_n_temple[C_n_temple.index(C_n_temple_removed)]
        
        del C_temple[temple_index]
        
        L_temple[i] = L_temple[i] - 1
        L_temple[j] = L_temple[j] - 1
        
        if (L_temple[i] == 0 and len(L_temple)!=0):
            o = 0
            if (len(C_temple) != 0):
                while(o< len(C_temple)):
                    if(C_temple[o][0]==i or C_temple[o][1]==i):
                        del C_temple[o]
                        del C_n_temple[o]
                        o = 0
                    else:
                        o = o + 1
        if (L_temple[j] == 0 and len(L_temple)!=0):
            o = 0
            if (len(C_temple) != 0):
                while(o< len(C_temple)):
                    if(C_temple[o][0]==j or C_temple[o][1]==j):
                        del C_temple[o]
                        del C_n_temple[o]
                        o = 0
                    else:
                        o = o + 1
        
        
        
    Final_paths.append(index_path)
    Final_sum.append(C_sum)
    C_sum_list.append(C_sum)
    
    
print("maximum payoff = " + str(max(Final_sum)))
index_final = Final_sum.index(max(Final_sum))
print(Final_paths[index_final])


# In[3]:


print(Variants_matrix)

