class Wrapper:
    def calculate_area(self, length: int, width: int, height: int) -> int:
        length_width = length * width
        width_height = width * height
        height_length = height * length
        slack = min(length_width, width_height, height_length)
        return 2 * (length_width + width_height + height_length) + slack

    def calculate_ribbon(self, length: int, width: int, height: int) -> int:
        dimension1, dimension2 = sorted([length, width, height])[:2]
        return 2 * (dimension1 + dimension2) + length * width * height
