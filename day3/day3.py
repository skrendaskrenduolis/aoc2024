import re

with open("day3_input", "r") as infile:
    corrupted_text = "".join(infile.readlines())

    # part 1
    uncorrupt_mul_list = re.findall(r"mul\((\d+),(\d+)\)", corrupted_text)
    uncorrupt_mul_answer = sum([int(x[0])*int(x[1]) for x in uncorrupt_mul_list])
    print(uncorrupt_mul_answer)

    # part 2
    allowed_muls_sum = 0
    
    dont_split_list = re.split(r"don't\(\)", corrupted_text)
    first_item = re.findall(r"mul\((\d+),(\d+)\)", dont_split_list.pop(0))
    allowed_muls_sum += sum([int(x[0])*int(x[1]) for x in first_item])
    
    for item in dont_split_list:
        allowed_muls = re.findall(r"mul\((\d+),(\d+)\)", item[item.find("do()"):])
        allowed_muls_sum += sum([int(x[0])*int(x[1]) for x in allowed_muls])

    print(allowed_muls_sum)
