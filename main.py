import sys, shape

def process_commands(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        processed_commands = list()
        for line in contents:
            line = line.split(":")
            line = [l.strip() for l in line if l!="\n"]
            if len(line) == 1:
                processed_commands.append((line[0],))
            else:
                processed_commands.append(tuple(line))
    return processed_commands

def main():
    img_size = (1240, 1754)
    chart = shape.ShapeDrawer("flowchart.png", img_size)
    coordinate_array = list() #list to store every block coordinates
    base_coordinates = (img_size[0] / 2, 0.05 * img_size[1]) #Coordinates of start block
    flag = 0 #flag to check if decision block has been trigerred
    commands = sys.argv[1]
    commands_array = process_commands(commands)
    for block in commands_array:
        #Coordinates calculation and drawing connectors
        if len(coordinate_array) == 0:
            coordinate_array.append(base_coordinates)
        elif flag == 1:
            flag += 1
            prev_block = commands_array[commands_array.index(block)-1]
            prev_block_boun_coor = chart.return_bounding_coor(prev_block[1], coordinate_array[-1])
            radius = shape.math.sqrt((prev_block_boun_coor[2] - coordinate_array[-1][0]) ** 2 + (prev_block_boun_coor[3] - coordinate_array[-1][1]) ** 2) + 20
            coordinate_array.append((coordinate_array[-1][0] - 250, coordinate_array[-1][1] + radius + 50))
            c1 = chart.return_bounding_coor(block[1], coordinate_array[-1])[1] - 20
            chart.draw_line((coordinate_array[-2][0] - radius, coordinate_array[-2][1], coordinate_array[-1][0], coordinate_array[-2][1], coordinate_array[-1][0], c1),"yes")
        elif flag == 2:
            flag += 1
            prev_block = commands_array[commands_array.index(block)-2]
            prev_block_boun_coor = chart.return_bounding_coor(prev_block[1], coordinate_array[-1])
            radius = shape.math.sqrt((prev_block_boun_coor[2] - coordinate_array[-1][0]) ** 2 + (prev_block_boun_coor[3] - coordinate_array[-1][1]) ** 2) + 20
            coordinate_array.append((coordinate_array[-2][0] + 250, coordinate_array[-1][1]))
            c1 = chart.return_bounding_coor(block[1], coordinate_array[-1])[1] - 20
            chart.draw_line((coordinate_array[-3][0] + radius, coordinate_array[-3][1], coordinate_array[-1][0], coordinate_array[-3][1], coordinate_array[-1][0], c1), "no")
        else:
            prev_block = commands_array[commands_array.index(block)-1]
            if prev_block[0].upper() not in ["START", "END"]:
                prev_block_boun_coor = chart.return_bounding_coor(prev_block[1], coordinate_array[-1])
            else:
                prev_block_boun_coor = chart.return_bounding_coor(prev_block[0], coordinate_array[-1])
            coordinate_array.append((base_coordinates[0], prev_block_boun_coor[3] + 20 + 50))
            if block[0].upper() == "END":
                new_block_top_coor = chart.return_bounding_coor(block[0], coordinate_array[-1])
            else:
                new_block_top_coor = chart.return_bounding_coor(block[1], coordinate_array[-1])

            if flag == 3:
                flag += 1
                chart.draw_line((coordinate_array[-2][0], prev_block_boun_coor[3] + 20, coordinate_array[-2][0], new_block_top_coor[3], new_block_top_coor[2] + 20, new_block_top_coor[3]))
                chart.draw_line((coordinate_array[-3][0], prev_block_boun_coor[3] + 20, coordinate_array[-3][0], new_block_top_coor[3], new_block_top_coor[0] - 20, new_block_top_coor[3]))
            elif flag == 6:
                radius = shape.math.sqrt((prev_block_boun_coor[2] - coordinate_array[-2][0]) ** 2 + (prev_block_boun_coor[3] - coordinate_array[-2][1]) ** 2) + 20
                flag += 1
                coordinate_array[-1] = list(coordinate_array[-1])
                coordinate_array[-1][1] = coordinate_array[-2][1] + radius + 50
                if block[0].upper() == "END":
                    new_block_top_coor = chart.return_bounding_coor(block[0], coordinate_array[-1])
                else:
                    new_block_top_coor = chart.return_bounding_coor(block[1], coordinate_array[-1])
                c2 = int(commands_array[commands_array.index(block)-1][2][3:]) - 1
                c2_bound = chart.return_bounding_coor(commands_array[c2][1], coordinate_array[c2])
                msg = commands_array[commands_array.index(block)-1][2][:3]
                chart.draw_line((base_coordinates[0] + radius, coordinate_array[-2][1],
                                 base_coordinates[0] + radius + 100, coordinate_array[-2][1],
                                 base_coordinates[0] + radius + 100, coordinate_array[c2][1],
                                 c2_bound[2] + 20, coordinate_array[c2][1]
                                 ), msg)
                if msg == "yes":
                    msg = "no"
                chart.draw_line((base_coordinates[0], coordinate_array[-2][1] + radius, base_coordinates[0], new_block_top_coor[1] - 20), msg)
            else:
                chart.draw_line((base_coordinates[0], prev_block_boun_coor[3] + 20 , base_coordinates[0], new_block_top_coor[1] - 20))

        if block[0].upper() == "START":
            chart.draw_oval("START", coordinate_array[0])

        elif block[0].upper() == "IO":
            chart.draw_parallelogram(block[1],coordinate_array[-1])

        elif block[0].upper() == "DECIDE":
            c1 = chart.return_bounding_coor(block[1], coordinate_array[-1])
            radius = shape.math.sqrt((c1[2] - coordinate_array[-1][0]) ** 2 + (c1[3] - coordinate_array[-1][1]) ** 2)
            coordinate_array[-1] = list(coordinate_array[-1])
            coordinate_array[-1][1] += radius
            coordinate_array[-1] = tuple(coordinate_array[-1])
            chart.draw_diamond(block[1], coordinate_array[-1])
            flag = 1

        elif block[0].upper() == "PROCESS":
            chart.draw_rectangle(block[1], coordinate_array[-1])

        elif block[0].upper() == "LOOP":
            c1 = chart.return_bounding_coor(block[1], coordinate_array[-1])
            radius = shape.math.sqrt((c1[2] - coordinate_array[-1][0]) ** 2 + (c1[3] - coordinate_array[-1][1]) ** 2)
            coordinate_array[-1] = list(coordinate_array[-1])
            coordinate_array[-1][1] += radius
            coordinate_array[-1] = tuple(coordinate_array[-1])
            chart.draw_diamond(block[1], coordinate_array[-1])
            flag = 6

        elif block[0].upper() == "END":
            chart.draw_oval(block[0], coordinate_array[-1])

        else:
            print("There is some error in the command file")
            exit()

    chart.save()


if __name__ == "__main__":
    main()
