
def update_tail(head, tail):
    
    [head_x, head_y] = head
    [tail_x, tail_y] = tail
    
#   tail on same row as head
    if head_y == tail_y:
        if abs(head_x - tail_x) == 2:
            if head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1
                
#   tail in same column as head
    elif head_x == tail_x:
        if abs(head_y - tail_y) == 2:
            if head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1
                
#   tail is diagonal from head
    else:
#       head is two above tail
        if head_y > tail_y and head_y - tail_y == 2:
            if head_x > tail_x:
                tail_y += 1
                tail_x += 1
            else:
                tail_y += 1
                tail_x -= 1
#       head is two below tail          
        elif head_y < tail_y and abs(head_y - tail_y) == 2:
            if head_x > tail_x:
                tail_y -= 1
                tail_x += 1
            else:
                tail_y -= 1
                tail_x -= 1
#       head is two to right of tail
        elif head_x > tail_x and head_x - tail_x == 2:
            if head_y > tail_y:
                tail_y += 1
                tail_x += 1
            else:
                tail_y -= 1
                tail_x += 1
#       head is two to left of tail
        elif head_x < tail_x and abs(head_x - tail_x) == 2:
            if head_y > tail_y:
                tail_y += 1
                tail_x -= 1
            else:
                tail_y -= 1
                tail_x -= 1
    
    tail = [tail_x, tail_y]
    return tail

# part 1

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    rows = read_data.splitlines()

    visited_by_tail = set(['0-0'])
    
    head = [0, 0]
    tail = [0, 0]
    
    for instruction in rows:
        [direction, move_size] = instruction.split(' ')
        
        for i in range(int(move_size)):
            if direction == 'R':
                head[0] += 1
            if direction == 'L':
                head[0] -= 1
            if direction == 'U':
                head[1] += 1
            if direction == 'D':
                head[1] -= 1
            tail = update_tail(head, tail)
            visited_by_tail.add(str(tail[0]) + '-' + str(tail[1]))
    
    print(len(visited_by_tail))

# part 2
        
with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    rows = read_data.splitlines()

    visited_by_tail = set(['0:0'])
    
    head = [0, 0]
    knots = [[0, 0]]*9
    
    for instruction in rows:
        
        [direction, move_size] = instruction.split(' ')
        
        for i in range(int(move_size)):
            if direction == 'R':
                head[0] += 1
            if direction == 'L':
                head[0] -= 1
            if direction == 'U':
                head[1] += 1
            if direction == 'D':
                head[1] -= 1
                
            for knot_index, knot in enumerate(knots):
                if knot_index == 0:
                    knots[knot_index] = update_tail(head, knot)
                else:
                    knots[knot_index] = update_tail(knots[knot_index - 1], knot)
                if knot_index == len(knots) - 1:
                    visited_by_tail.add(str(knots[knot_index][0]) + ':' + str(knots[knot_index][1]))
            
    print(len(visited_by_tail))
        

