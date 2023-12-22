"""Day 22 - Problem 1 of Advent of Code 2023"""
with open("input.txt") as input_file:
    input_text = input_file.read().splitlines()
bricks = []
grid_height = [[0 for _ in range(10)] for _ in range(10)]
removable = set()
reference = {}
for brick in input_text:
    coordinate_1, coordinate_2 = brick.split("~")
    x1, y1, z1 = coordinate_1.split(",")
    x2, y2, z2 = coordinate_2.split(",")
    bricks.append((int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)))
bricks.sort(key=lambda brick_coordinates: brick_coordinates[2])
for idx, brick in enumerate(bricks):
    removable.add(idx)
    x1, y1, z1, x2, y2, z2 = brick
    if x1 == x2 and y1 == y2:
        if grid_height[x1][y1] == 0:
            grid_height[x1][y1] = z2 - z1 + 1
            reference[(x1, y1, grid_height[x1][y1])] = idx
        else:
            removable -= {reference[(x1, y1, grid_height[x1][y1])]}
            grid_height[x1][y1] += z2 - z1 + 1
            reference[(x1, y1, grid_height[x1][y1])] = idx
    elif x1 == x2:
        max_height_y = max(range(y1, y2 + 1), key=lambda y_coordinate: grid_height[x1][y_coordinate])
        max_height = grid_height[x1][max_height_y]
        if max_height == 0:
            for y in range(y1, y2 + 1):
                grid_height[x1][y] = 1
                reference[(x1, y, 1)] = idx
        else:
            multiple_supporting = False
            for y in range(y1, y2 + 1):
                same_height = grid_height[x1][y] == max_height
                if same_height and reference[(x1, y, max_height)] != reference[(x1, max_height_y, max_height)]:
                    multiple_supporting = True
                    break
            if not multiple_supporting:
                removable -= {reference[(x1, max_height_y, max_height)]}
            for y in range(y1, y2 + 1):
                grid_height[x1][y] = max_height + 1
                reference[(x1, y, grid_height[x1][y1])] = idx
    elif y1 == y2:
        max_height_x = max(range(x1, x2 + 1), key=lambda x_coordinate: grid_height[x_coordinate][y1])
        max_height = grid_height[max_height_x][y1]
        if max_height == 0:
            for x in range(x1, x2 + 1):
                grid_height[x][y1] = 1
                reference[(x, y1, 1)] = idx
        else:
            multiple_supporting = False
            for x in range(x1, x2 + 1):
                same_height = grid_height[x][y1] == max_height
                if same_height and reference[(x, y1, max_height)] != reference[(max_height_x, y1, max_height)]:
                    multiple_supporting = True
                    break
            if not multiple_supporting:
                removable -= {reference[(max_height_x, y1, max_height)]}
            for x in range(x1, x2 + 1):
                grid_height[x][y1] = max_height + 1
                reference[(x, y1, grid_height[x1][y1])] = idx
print(len(removable))
