from collections import deque

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def perform_move(start, move):
    return [sum(val) for val in zip(start, move)]

def valid_position(prev_position, position, rows):
    [prev_row_index, prev_col_index] = prev_position
    [row_index, col_index] = position
 
    if row_index < 0 or row_index >= len(rows):
        return False
    if col_index < 0 or col_index >= len(rows[0]):
        return False
    
    prev_val = rows[prev_row_index][prev_col_index]
    val = rows[row_index][col_index]
    if ord(val) > ord(prev_val):
        if (prev_val != 'S') and (ord(val) - ord(prev_val) > 1):
            return False
    if val == 'E':
        if(ord('z') - ord(prev_val) > 1):
            return False
    
    return True

# part 1 
with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    rows = data.splitlines()
        
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            if col == 'S':
                start = [row_index, col_index]
    
    visited = [start]
    
    queue = deque([start])
    
    path_length = -1
    
    found_answer = False
    
#     BFS
    
    while len(queue) and not found_answer:
        path_length += 1
        for i in range(len(queue)):
            position = queue.popleft()
            value = rows[position[0]][position[1]]
            if value == 'E':
                found_answer = True
                print(path_length)
                break
            for move in moves:
                next_position = perform_move(position, move)
                if valid_position(position, next_position, rows) and next_position not in visited and next_position not in queue:
                    queue.append(next_position)
            visited.append(position)
    
    

# part 2
with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    rows = data.splitlines()
    
    low_points = []
        
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            if col == 'a' or col == 'S':
                low_points.append([row_index, col_index])
    
    path_lengths = []
    
    for low_point in low_points:
        
        visited = [low_point]

        queue = deque([low_point])

        path_length = -1

        found_answer = False

        while len(queue) and not found_answer:
            path_length += 1
            for i in range(len(queue)):
                position = queue.popleft()
                value = rows[position[0]][position[1]]
                if value == 'E':
                    found_answer = True
                    path_lengths.append(path_length)
                    break
                for move in moves:
                    next_position = perform_move(position, move)
                    if valid_position(position, next_position, rows) and next_position not in visited and next_position not in queue:
                        queue.append(next_position)
                visited.append(position)
    path_lengths.sort()
    print(path_lengths[0])
