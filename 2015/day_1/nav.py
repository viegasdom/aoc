from functools import reduce

class Navigator:

    def __init__(self):
        pass

    def navigate(self, path: str) -> int:
        floor = 0
        for direction in path:
            if direction == "(":
                floor += 1
            elif direction == ")":
                floor -= 1

        return floor
     
    def first_basement_position(self, path: str) -> int:
        floor = 0
        position = 1
        for index, direction in enumerate(path):
            if direction == "(":
                floor += 1
            elif direction == ")":
                floor -= 1

            if floor < 0:
                position = index + 1 
                break

        return position
