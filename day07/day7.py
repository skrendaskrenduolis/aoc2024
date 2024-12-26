def recursive_two_ops(goal_number, num_list, current_val):
    if current_val == goal_number and len(num_list) == 0:
        return current_val
    elif current_val != goal_number and len(num_list) == 0:
        return 0
    else:
        next_number = num_list.pop(0)
        num_list_add = num_list.copy()
        num_list_mul = num_list.copy()
        current_val_add = current_val+next_number
        current_val_mul = current_val*next_number        
        a = recursive_two_ops(goal_number, num_list_add, current_val_add)
        b = recursive_two_ops(goal_number, num_list_mul, current_val_mul)
        if a != 0:
            return a
        return b
    
def recursive_three_ops(goal_number, num_list, current_val):
    if current_val == goal_number and len(num_list) == 0:
        return current_val
    elif current_val != goal_number and len(num_list) == 0:
        return 0
    else:
        next_number = num_list.pop(0)
        num_list_add = num_list.copy()
        num_list_mul = num_list.copy()
        num_list_concat = num_list.copy()
        current_val_add = current_val+next_number
        current_val_mul = current_val*next_number        
        current_val_concat = int(str(current_val)+str(next_number))
        a = recursive_three_ops(goal_number, num_list_add, current_val_add)
        b = recursive_three_ops(goal_number, num_list_mul, current_val_mul)
        c = recursive_three_ops(goal_number, num_list_concat, current_val_concat)
        if a != 0:
            return a
        elif b != 0:
            return b
        return c

two_ops_sum = 0
with open("day7_input", "r") as infile:
    for line in infile:
        line_list = line.split()
        goal = int(line_list[0][:-1])
        number_list = list(map(int, line_list[1:]))
        current_value = number_list.pop(0)

        test_result_two_ops = recursive_two_ops(goal, number_list, current_value)
        two_ops_sum += test_result_two_ops
print(two_ops_sum)

  
three_ops_sum = 0
with open("day7_input", "r") as infile:
    for line in infile:
        line_list = line.split()
        goal = int(line_list[0][:-1])
        number_list = list(map(int, line_list[1:]))
        current_value = number_list.pop(0)


        test_result_three_ops = recursive_three_ops(goal, number_list, current_value)
        three_ops_sum += test_result_three_ops
print(three_ops_sum)
