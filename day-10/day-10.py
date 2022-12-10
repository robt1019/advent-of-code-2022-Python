# part 1
interesting_cycles = [20,60,100,140,180,220]

def evaluate_cycle(cycle, curren_val):
    if cycle in interesting_cycles:
        return cycle * current_val
    return 0
    

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    rows = read_data.splitlines()
    
    current_val = 1
    cycle = 0
    answer_total = 0
    
    for instruction in rows:
        if instruction != 'noop':
            for i in range(2):
                cycle += 1
                answer_total += evaluate_cycle(cycle, current_val)
            current_val += int(instruction.split(' ')[1])
        else:
            cycle += 1
            answer_total += evaluate_cycle(cycle, current_val)
    
    print(answer_total)
            
# part 2
screen_width = 40

def cycle_to_row_coord(cycle):
    return [(cycle - 1) // screen_width, (cycle - 1) % screen_width]

def print_rows(rows):
    for row in rows:
        print(''.join(row))
        
def pixel_value(cycle, sprite_position):
    sprite_col = sprite_position % screen_width
    cycle_col = (cycle - 1) % screen_width
    if cycle_col in [sprite_col-1, sprite_col, sprite_col + 1]:
        return '#'
    return '.'
    
def draw_pixel(cycle, rows, sprite_position):
    [row_index, col_index] = cycle_to_row_coord(cycle)
    
    if col_index == 0:
        rows.append([])
    rows[row_index].append(pixel_value(cycle, sprite_position))

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    data = read_data.splitlines()
    
    sprite_position = 1
    
    cycle = 1
    
    rows = []
    
    for instruction in data:
        if instruction != 'noop':
            for i in range(2):
                draw_pixel(cycle, rows, sprite_position)
                cycle += 1
            sprite_position += int(instruction.split(' ')[1])                     
        else:
            draw_pixel(cycle, rows, sprite_position)
            cycle += 1
            
print_rows(rows)
        