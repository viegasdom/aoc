import nav
import os

# ( -> means go up a floor
# ) -> means go down a floor
# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
if __name__ == "__main__":
    navigator = nav.Navigator()    
    file_path = os.path.dirname(os.path.realpath(__file__))

    with open(f"{file_path}/input.txt", "r") as file:
        path = file.read()
        print(f"first challenge: {navigator.navigate(path)}")

    with open(f"{file_path}/input2.txt", "r") as file:
        path2 = file.read()
        print(f"second challenge: {navigator.first_basement_position(path2)}")
