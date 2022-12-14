
# part 1

with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    filled = set()
    
    lowest_y = 0
    lowest_x = 500
    highest_x = 500
    
    for row in data.splitlines():
        
        edges = [edge.strip() for edge in row.split('->')]
        
        for edge_index, edge in enumerate(edges):
            
            [x, y] = [int(coord) for coord in edge.split(',')]
                        
            filled.add(str(x) + ':' + str(y))
            [lowest_x, highest_x] = [min(lowest_x, x), max(highest_x, x)]
            if y > lowest_y:
                lowest_y = y
            
            if edge_index > 0:
                [x_prev, y_prev] = [int(coord) for coord in edges[edge_index - 1].split(',')]
                if x_prev != x:
                    if x_prev < x:
                        for i in range(x_prev, x):
                            filled.add(str(i) + ':' + str(y))
                            [lowest_x, highest_x] = [min(lowest_x, i), max(highest_x, i)]
                            if y > lowest_y:
                                lowest_y = y
                    else:
                        for i in range(x, x_prev):
                            filled.add(str(i) + ':' + str(y))
                            [lowest_x, highest_x] = [min(lowest_x, i), max(highest_x, i)]
                            if y > lowest_y:
                                y = lowest_y
                elif y_prev != y:
                    if y_prev < y:
                        for i in range(y_prev, y):
                            filled.add(str(x) + ':' + str(i))
                            [lowest_x, highest_x] = [min(lowest_x, x), max(highest_x, x)]
                            if i > lowest_y:
                                lowest_y = i
                    else:
                        for i in range(y, y_prev):
                            filled.add(str(x) + ':' + str(i))
                            [lowest_x, highest_x] = [min(lowest_x, x), max(highest_x, x)]
                            if i > lowest_y:
                                lowest_y = i
            
    contained = True
    sand_count = -1

    while contained:
        position = [500, 0]
        settled = False
        while not settled:
            [x, y] = position
            if (str(x) + ':' + str(y+1)) not in filled:
                position = [x, y+1]
            elif (str(x-1) + ':' + str(y+1)) not in filled:
                position = [x-1, y+1]
            elif (str(x+1) + ':' + str(y+1)) not in filled:
                position = [x+1, y+1]
            elif not (position[1] > lowest_y or position[0] < lowest_x or position[0] > highest_x):                
                settled = True
                filled.add(str(position[0]) + ':' + str(position[1]))
                
            if position[1] > lowest_y or position[0] < lowest_x or position[0] > highest_x:
                contained = False
                settled = True

        sand_count += 1
        
    print(sand_count)
                

# part 2

with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    filled = set()
    
    lowest_y = 0
    
    for row in data.splitlines():
        
        edges = [edge.strip() for edge in row.split('->')]
        
        for edge_index, edge in enumerate(edges):
            
            [x, y] = [int(coord) for coord in edge.split(',')]
                        
            filled.add(str(x) + ':' + str(y))
            
            if y > lowest_y:
                lowest_y = y
            
            if edge_index > 0:
                [x_prev, y_prev] = [int(coord) for coord in edges[edge_index - 1].split(',')]
                if x_prev != x:
                    if x_prev < x:
                        for i in range(x_prev, x):
                            filled.add(str(i) + ':' + str(y))
                            if y > lowest_y:
                                lowest_y = y
                    else:
                        for i in range(x, x_prev):
                            filled.add(str(i) + ':' + str(y))
                            if y > lowest_y:
                                y = lowest_y
                elif y_prev != y:
                    if y_prev < y:
                        for i in range(y_prev, y):
                            filled.add(str(x) + ':' + str(i))
                            if i > lowest_y:
                                lowest_y = i
                    else:
                        for i in range(y, y_prev):
                            filled.add(str(x) + ':' + str(i))
                            if i > lowest_y:
                                lowest_y = i
        
    lowest_y += 2
    
    blocked = False
    
    sand_count = 0
    
    while not blocked:
        position = [500, 0]
        
        if (str(position[0]) + ':' + str(position[1])) in filled:
            blocked = True
            break
            
        settled = False
        
        while not settled:
            [x, y] = position
            if (str(x) + ':' + str(y+1)) not in filled:
                position = [x, y+1]
            elif (str(x-1) + ':' + str(y+1)) not in filled:
                position = [x-1, y+1]
            elif (str(x+1) + ':' + str(y+1)) not in filled:
                position = [x+1, y+1]
            elif position[1] != lowest_y:
                settled = True
                filled.add(str(position[0]) + ':' + str(position[1]))
            if position[1] == lowest_y - 1:
                settled = True
                filled.add(str(position[0]) + ':' + str(position[1]))
 
        sand_count += 1

    print(sand_count)
                





