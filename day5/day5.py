import re

def check_correctess(x):
    '''checking if numbers above and below
      current number belong to appropriate subset'''
    
    correct_update_verify = []
    for i in range(len(x)):
        above_set = set(x[:i])
        below_set = set(x[i+1:])
        
        if above_set.issubset(above_below_dict[x[i]]["above"]) and below_set.issubset(above_below_dict[x[i]]["below"]):
            correct_update_verify.append(True)
            continue
        correct_update_verify.append(False)
    return correct_update_verify


def recurse_func(error_list):
    '''
    if neighbor number is supposed to be above current number,
    swap them. repeat until all numbers are in the right place
    '''
    for i in range(0, len(error_list)-1):
        if error_list[i+1] in above_below_dict[error_list[i]]["above"]:
            error_list[i], error_list[i+1] = error_list[i+1], error_list[i]
    check = check_correctess(error_list)
    if all(check):
        return error_list
    recurse_func(error_list)


with open("day5_input", "r") as infile:
    above_below_dict = dict()
    parsing_pages = True
    middle_number_sum = 0
    middle_number_sum_fixed = 0

    for line in infile:
        if line == "\n":
            parsing_pages = False
            continue
        

        line_list = list(map(int, re.split(r'\||,', line.strip())))

        # build the dict showing what numbers are allowed above and what are allowed below
        if parsing_pages:
            if line_list[0] not in above_below_dict:
                above_below_dict[line_list[0]] = {"above": set(), "below": set()}
            if line_list[1] not in above_below_dict:
                above_below_dict[line_list[1]] = {"above": set(), "below": set()}
            above_below_dict[line_list[0]]["below"].add(line_list[1])
            above_below_dict[line_list[1]]["above"].add(line_list[0])
            continue

        # part 1
        # check if numbers ordered correctly, if yes then add middle value to sum
        correct_update_verify = check_correctess(line_list)
        if all(correct_update_verify):
            middle_index = len(line_list) // 2
            middle_number_sum += line_list[middle_index]
            continue

        # part 2
        # for the wrong number list, sort it recursively
        fixed_line_list = recurse_func(line_list)
        middle_index = len(line_list) // 2
        middle_number_sum_fixed += line_list[middle_index]
        

    print(middle_number_sum)
    print(middle_number_sum_fixed)
