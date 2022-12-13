#!/usr/bin/env python
# coding: utf-8

# In[22]:


import json

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
            
        if is_in_order(left_element, right_element):
            return True

with open('input.txt', encoding="utf-8") as f:
    data = f.read()
    
    packets = data.split('\n\n')
    
    in_order_count = 0
    
    for packet_index, packet in enumerate(packets):
        [left, right] = [json.loads(x) for x in packet.splitlines()]
        if is_in_order(left, right):
            in_order_count += packet_index + 1
    print(in_order_count)
    


# In[23]:





# In[ ]:




