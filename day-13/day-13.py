import json

from collections import deque

def is_in_order(left, right):
    
    for i in range(max(len(left), len(right))):
        
        if i > (len(left) - 1):
            return True
        
        if i > (len(right) - 1):
            return False

        left_element = left[i]
        
        right_element = right[i]
        
        if isinstance(left_element, int) and isinstance(right_element, int):
            if left_element < right_element:
                return True
            elif left_element > right_element:
                return False
            else:
                continue
        elif isinstance(left_element, int):
            left_element = [left_element]
        elif isinstance(right_element, int):
            right_element = [right_element]
         
        result = is_in_order(left_element, right_element)
        
        if result == None:
            continue
            
        return result

# part 1

with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    packets = data.split('\n\n')
    
    in_order_count = 0
    
    for packet_index, packet in enumerate(packets):
        [left, right] = [json.loads(x) for x in packet.splitlines()]
        if is_in_order(left, right):
            in_order_count += packet_index + 1
    print(in_order_count)
    


# part 2
def merge_sort(packets):
    
    if len(packets) == 1:
        return [packets[0]]
        
    left = packets[:len(packets)//2]
    
    right = packets[len(packets)//2:]
    
    left_sorted = deque(merge_sort(left))
    
    right_sorted = deque(merge_sort(right))
    
    sorted = []
    
    while len(left_sorted) > 0 and len(right_sorted) > 0:
        if is_in_order(left_sorted[0], right_sorted[0]):
            sorted.append(left_sorted.popleft())
        else:
            sorted.append(right_sorted.popleft())
    
    while len(left_sorted) > 0:
        sorted.append(left_sorted.popleft())

    while len(right_sorted) > 0:
        sorted.append(right_sorted.popleft())
        
    return sorted
    

with open('input.txt', encoding="utf-8") as f:
    
    data = f.read()
    
    pairs = data.split('\n\n')
    
    packets = [[[2]], [[6]]]
    
    for pair in pairs:
        [left, right] = [json.loads(x) for x in pair.splitlines()]
        packets.append(left)
        packets.append(right)
            
    
    sorted = merge_sort(packets)
    
    answer = 1
    
    for i, item in enumerate(sorted):
        if item == [[2]] or item == [[6]]:
            answer *= (i+1)
    
    print(answer)
    




