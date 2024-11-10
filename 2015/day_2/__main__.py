import os

import wrapper

# length * width * height
# formula for the paper: 2*l*w + 2*w*h + 2*h*l
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

if __name__ == "__main__":
    wrapper = wrapper.Wrapper()
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{path}/input.txt", "r") as file:
        presents = [map(int, present_dimensions.split("x")) for present_dimensions in file.read().splitlines()]
        total_area = sum([wrapper.calculate_area(length, width, height) for length, width, height in presents])
        print(f"first challenge: {total_area}")

    with open(f"{path}/input2.txt", "r") as file:
        presents = [map(int, present_dimensions.split("x")) for present_dimensions in file.read().splitlines()]
        total_ribbon = sum([wrapper.calculate_ribbon(length, width, height) for length, width, height in presents])
        print(f"second challenge: {total_ribbon}")
