from collections import Counter

# Part 1
with open("day1_input", "r") as infile:
    left_location_list = []
    right_location_list = []

    for line in infile:
        line_list = line.split()
        
        left_location_list.append(int(line_list[0]))
        right_location_list.append(int(line_list[1]))

    left_location_list.sort()
    right_location_list.sort()

    distance_between_list = []
    for left, right in zip(left_location_list, right_location_list):
        distance_between_list.append(abs(left - right))
    
    print(sum(distance_between_list))


# Part 2
    number_dict = dict()
    for number in left_location_list:
        if number not in number_dict:
            m = left_location_list.count(number)
            n = right_location_list.count(number)
            number_dict[number] = m*number*n
    
    print(sum(number_dict.values()))



def create_custom_hashmap(array_a, array_b):
    # Count occurrences in array A and B
    count_a = Counter(array_a)
    count_b = Counter(array_b)
    
    # Create the result hashmap
    result = {}
    for key in count_a:
        result[key] = count_a[key] * count_b.get(key, 0) * key
        
    return result

hashmap = create_custom_hashmap(left_location_list, right_location_list)
print(len(left_location_list))
print(sum(hashmap.values()))