import numpy as np


def safety_check(input_list: list) -> bool:
    diff_array = np.diff(np.fromiter(map(int, input_list), dtype=int))

    if (np.all(diff_array < 0) and not np.any((diff_array < -3) | (diff_array > -1))) or \
          (np.all(diff_array > 0) and not np.any((diff_array < 1) | (diff_array > 3))):
        return True
    
    return False



with open("day2_input", "r") as infile:
    dampened_report_counter = 0
    safe_report_counter = 0
    for line in infile:
        line_list = line.split()

        # part 1        
        safe_report = safety_check(line_list)
        if safe_report:
            safe_report_counter += 1
            continue
        
        # part 2
        for i in range(0, len(line_list)):
            check_correctness = safety_check(line_list[:i] + line_list[i+1:])
            if check_correctness:
                dampened_report_counter += 1
                break
        
    # part 1
    print(safe_report_counter)                
    
    # part 2
    print(safe_report_counter + dampened_report_counter)
