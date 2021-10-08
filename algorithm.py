def find_w_not_in_path(path_list,matrix):
    num_verticies = len(matrix[0])
    found = 0 
    for row in range(num_verticies):
        if row+1 not in path_list:
            return row
def find_hamilton_path(adjacency_matrix):
    # if <= 3 verticies. find path manually
    path_list = []
    vertex_count =0
    num_verticies = len(adjacency_matrix[0])
    if num_verticies>1:
        # connect 1st 2 verticies
        for row in range(num_verticies):
            for col in range(num_verticies):
                if adjacency_matrix[row][col] == 1:
                    path_list.append(row+1)
                    path_list.append(col+1)
                    vertex_count +=2
                    break
            else:
                continue 
            break
        if vertex_count != num_verticies: # >= 3 verticies
            # connect 3rd vertex
            # if 3rd vertex is (w,v1)
            if adjacency_matrix[2][0] == 1:
                path_list.insert(0,2)
            elif adjacency_matrix[1][2]: # if 3rd vertex is (v2,w)
                path_list.append(3)
            else:
                path_list = [1,3,2]
            vertex_count +=1
            while vertex_count<num_verticies:
                w = find_w_not_in_path(path_list,adjacency_matrix)
                # there exists vi,vi+1 such that (vi,w),(w,vi+1) is in the edge list
                # find such vi
                if(adjacency_matrix[w][path_list[0]-1]==1):
                    path_list.insert(0,w+1)
                elif adjacency_matrix[path_list[-1]-1][w]==1:
                    path_list.append(w+1)
                
                # the vi is not at the start or end of the path
                # it's somewhere in the middle
                else:
                    for row in range(num_verticies):
                        for col in range(num_verticies):
                     
                            result = adjacency_matrix[row][w] ==1 and adjacency_matrix[w][row+1]==1
                        
                            if result:
                                path_list.insert(row+1,w+1)
                                
                                break
                        else:
                            continue 
                        break
                vertex_count+=1
    return path_list
                    
matrix = [[0,1,1,0],
          [0,0,0,0],
          [0,1,0,0],
          [1,0,1,0]]

himilton_path = find_hamilton_path(matrix)

print(himilton_path)