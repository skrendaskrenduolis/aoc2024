from Guard_class import Guard

with open("day6_input_test", "r") as infile:
    line_counter = 0
    area_matrix = []
    obstacle_set = set()
    for line in infile:
        line = line.strip()
        guard_search_pos = line.find("^")
        if guard_search_pos != -1:
            guard = Guard("up", line_counter, guard_search_pos)

        obs_search_index = 0
        obstacle_search_pos = 999999
        while obstacle_search_pos != -1:
            obstacle_search_pos = line.find("#", obs_search_index)
            obstacle_set.add((line_counter, obstacle_search_pos))
            obs_search_index = obstacle_search_pos+1

        area_matrix.append(list(line))
        line_counter += 1
    

obstacle_found = False
while guard.in_area:
    match guard.orientation:
        case "up":
            for i in range(guard.x_pos, -1, -1):
                if area_matrix[i][guard.y_pos] == ".":
                    guard.update_position_count()
                if (i, guard.y_pos) in obstacle_set:
                    guard.update_x(i+1)
                    guard.update_orientation("right")
                    obstacle_found = True
                    break
                area_matrix[i][guard.y_pos] = "X"


        case "down":
            for i in range(guard.x_pos, len(area_matrix)):
                if area_matrix[i][guard.y_pos] == ".":
                    guard.update_position_count()                
                if (i, guard.y_pos) in obstacle_set:
                    guard.update_x(i-1)
                    guard.update_orientation("left")
                    obstacle_found = True
                    break
                area_matrix[i][guard.y_pos] = "X"

        case "right":
            for i in range(guard.y_pos, len(area_matrix[0])):
                if area_matrix[guard.x_pos][i] == ".":
                    guard.update_position_count()                
                if (guard.x_pos, i) in obstacle_set:
                    guard.update_y(i-1)
                    guard.update_orientation("down")
                    obstacle_found = True
                    break
                area_matrix[guard.x_pos][i] = "X"

        case "left":
            for i in range(guard.y_pos, -1, -1):
                if area_matrix[guard.x_pos][i] == ".":
                    guard.update_position_count()  
                if (guard.x_pos, i) in obstacle_set:
                    guard.update_y(i+1)
                    guard.update_orientation("up")
                    obstacle_found = True
                    break
                area_matrix[guard.x_pos][i] = "X"
        
        case _:
            break
    
    if obstacle_found:
        obstacle_found = False
        continue
    guard.exit_area()

guard.display()
print("\n".join("".join(row) for row in area_matrix))
# with open("day6_1_solution", "w") as outfile:
#     outfile.write("\n".join("".join(row) for row in area_matrix))
