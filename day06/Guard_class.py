class Guard:
    def __init__(self, orientation: str, x_pos: int, y_pos: int):
        self.orientation = orientation
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.in_area = True
        self.visited_positions = 1
    
    def display(self):
        print(f"Orientation: {self.orientation}\nx: {self.x_pos}\ny: {self.y_pos}\nIn area: {self.in_area}\nVisited positions: {self.visited_positions}")

    def update_orientation(self, new_orientation):
        self.orientation = new_orientation

    def update_x(self, new_x_pos):
        self.x_pos = new_x_pos

    def update_y(self, new_y_pos):
        self.y_pos = new_y_pos

    def exit_area(self):
        self.in_area = False
    
    def update_position_count(self):
        self.visited_positions += 1