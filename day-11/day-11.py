# part 1

from collections import deque


def update_item(operation, item):
    a = item if operation[0] == 'old' else int(operation[0])
    b = item if operation[2] == 'old' else int(operation[2])
    if operation[1] == '*':
        return (a * b) // 3
    return (a + b) // 3

def to_monkey_data(monkey):
        monkey_data = monkey.splitlines()
        items = [int(item.strip()) for item in monkey_data[1].split(':')[1].split(',')]
        operation = monkey_data[2].split('= ')[1].split(' ')
        divisible_by_test = int(monkey_data[3].split(' ')[-1])
        test_true_next_monkey = monkey_data[4].split(' ')[-1]
        test_false_next_monkey = monkey_data[5].split(' ')[-1]
        
        return {
            'items': items,
            'operation': operation,
            'divisible_by_test': divisible_by_test,
            'test_true_next_monkey': test_true_next_monkey,
            'test_false_next_monkey': test_false_next_monkey,
            'inspection_count': 0
        }
    

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    data = read_data.split('\n\n')
    
    monkies = {}
    
    monkey_inspection_counts = [0] * len(data)
        
    for monkey_index, monkey in enumerate(data):
        
        monkies[str(monkey_index)] = to_monkey_data(monkey)
        
    for i in range(20):
        
        for j in range(len(monkies)):

            monkey = monkies[str(j)]

            updated_items = deque([update_item(monkey['operation'], item) for item in monkey['items']])

            while(len(updated_items) > 0):

                item = updated_items.popleft()
                
                monkey_inspection_counts[j] += 1

                if item % monkey['divisible_by_test'] == 0:
                    monkies[monkey['test_true_next_monkey']]['items'].append(item)
                else:
                    monkies[monkey['test_false_next_monkey']]['items'].append(item)
                    
            monkey['items'] = []

    monkey_inspection_counts.sort(reverse=True)
    
    print(monkey_inspection_counts[0] * monkey_inspection_counts[1])


# part 2

from collections import deque

def update_item(operation, item):
    a = item if operation[0] == 'old' else int(operation[0])
    b = item if operation[2] == 'old' else int(operation[2])
    if operation[1] == '*':
        return (a * b)
    return (a + b)

def to_monkey_data(monkey):
        monkey_data = monkey.splitlines()
        items = [int(item.strip()) for item in monkey_data[1].split(':')[1].split(',')]
        operation = monkey_data[2].split('= ')[1].split(' ')
        divisible_by_test = int(monkey_data[3].split(' ')[-1])
        test_true_next_monkey = monkey_data[4].split(' ')[-1]
        test_false_next_monkey = monkey_data[5].split(' ')[-1]
        
        return {
            'items': items,
            'operation': operation,
            'divisible_by_test': divisible_by_test,
            'test_true_next_monkey': test_true_next_monkey,
            'test_false_next_monkey': test_false_next_monkey,
            'inspection_count': 0
        }
    

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    data = read_data.split('\n\n')
    
    monkies = {}
    
    divisor_product = 1
    
    monkey_inspection_counts = [0] * len(data)
        
    for monkey_index, monkey in enumerate(data):
        
        monkies[str(monkey_index)] = to_monkey_data(monkey)
        
        divisor_product *= monkies[str(monkey_index)]['divisible_by_test']
        
    for i in range(10000):
        
        for j in range(len(monkies)):

            monkey = monkies[str(j)]

            updated_items = deque([update_item(monkey['operation'], item) for item in monkey['items']])

            while(len(updated_items) > 0):

                item = updated_items.popleft()
                
                monkey_inspection_counts[j] += 1

                if item % monkey['divisible_by_test'] == 0:
                    monkies[monkey['test_true_next_monkey']]['items'].append(item % divisor_product)
                else:
                    monkies[monkey['test_false_next_monkey']]['items'].append(item % divisor_product)
                    
            monkey['items'] = []

    monkey_inspection_counts.sort(reverse=True)
    
    print(monkey_inspection_counts[0] * monkey_inspection_counts[1])



