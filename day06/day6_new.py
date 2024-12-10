import numpy as np

with open("day6_input", "r") as infile:
    area_matrix = np.matrix([[x for x in line.strip()] for line in infile])

visited_places_matrix = np.zeros(area_matrix.shape)
guard = np.argwhere(area_matrix == "^")[0]
guard_original = guard.copy()

obstacle_locations = set(map(tuple, np.argwhere(area_matrix == "#")))


guard_movement_vector = (-1, 0)
# move up (-1, 0)
# move right (0, 1)
# move down (1, 0)
# move left (0, -1)

# part 1
false_obstacle_locations = set()
while 0 <= guard[0] < area_matrix.shape[0] and 0 <= guard[1] < area_matrix.shape[1]:
    visited_places_matrix[guard[0], guard[1]] = 1
    false_obstacle_locations.add((guard[0], guard[1]))

    if (guard[0] + guard_movement_vector[0], guard[1] + guard_movement_vector[1]) in obstacle_locations:
        guard_movement_vector = (guard_movement_vector[1], -guard_movement_vector[0])
    guard = (guard[0] + guard_movement_vector[0], guard[1] + guard_movement_vector[1])

print(int(np.sum(visited_places_matrix)))



# part 2
false_obstacle_locations = set(map(tuple, np.argwhere(visited_places_matrix == 1)))
false_obstacle_locations.remove((guard_original[0], guard_original[1]))
# print(len(false_obstacle_locations))


loop_count = 0
while len(false_obstacle_locations) > 0:
    guard = np.argwhere(area_matrix == "^")[0]
    guard_movement_vector = (-1, 0)
    encountered_obstacles_with_dir = set()
    false_obstacle = false_obstacle_locations.pop()
    obstacle_locations.add(false_obstacle)

    while 0 <= guard[0] < area_matrix.shape[0] and 0 <= guard[1] < area_matrix.shape[1]:
        if (guard[0] + guard_movement_vector[0], guard[1] + guard_movement_vector[1]) in obstacle_locations:
            encountered_obstacle = (guard[0] + guard_movement_vector[0], guard[1] + guard_movement_vector[1], guard_movement_vector)
            if encountered_obstacle in encountered_obstacles_with_dir:
                loop_count += 1
                break
            else:
                encountered_obstacles_with_dir.add(encountered_obstacle)

            guard_movement_vector = (guard_movement_vector[1], -guard_movement_vector[0])
        else:
            guard = (guard[0] + guard_movement_vector[0], guard[1] + guard_movement_vector[1])

    obstacle_locations.remove(false_obstacle)
print(loop_count)
