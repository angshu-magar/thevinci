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

    #testing
    #image was too low res
    img_size = (794, 1123)
    chart = shape.ShapeDrawer("flowchart.png", img_size)
    coordinate_array = list() #list to store every block coordinates
    base_coordinates = (img_size[0] / 2, 0.05 * img_size[1])
    flag = 0 #flag to check if decision block has been trigerred
    # temp.draw_oval("START", (img_size[0] / 2, 0.05 * img_size[1]))
    # temp.draw_rectangle("a, b", (img_size[0] / 2, 0.15 * img_size[1]))
    # temp.draw_parallelogram("INPUT a", (img_size[0] / 2, 0.25 * img_size[1]))
    # temp.draw_diamond("IF a > 0", (img_size[0] / 2, 0.35 * img_size[1]))
    # temp.save()
    commands = sys.argv[1]
    commands_array = process_commands(commands)
    # print(commands_array)
    for block in commands_array:
        if block[0].upper() == "START":
            print(commands_array.index(block))
            print(block[0])
            coordinate_array.append(base_coordinates)
            chart.draw_oval("START", coordinate_array[0])

        elif block[0].upper() == "IO":
            print(commands_array.index(block))
            if flag == 1:
                #Decision block has been trigerred and this is yes block
                flag +=1
                coordinate_array.append((base_coordinates[0] - 100, coordinate_array[-1][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_parallelogram(block[1],coordinate_array[-1])
                # chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))
                print(block[0])
                print("This is yes block after decision")
                continue
            elif flag == 2:
                flag += 1
                coordinate_array.append((base_coordinates[0] + 100, coordinate_array[-2][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_parallelogram(block[1],coordinate_array[-1])
                print(block[0])
                print("This is no block after decision")
                #Decision blcok has been trigerred and this is no block
            else:
                coordinate_array.append((base_coordinates[0], coordinate_array[-1][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_parallelogram(block[1],coordinate_array[-1])
                chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))
                print(block[0])
                pass

        elif block[0].upper() == "DECIDE":
            print(commands_array.index(block))
            coordinate_array.append((base_coordinates[0], coordinate_array[-1][1] + 100))
            c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
            c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
            radius = shape.math.sqrt((c2[0] - coordinate_array[-1][0]) ** 2 + (c2[1] - coordinate_array[-1][1]) ** 2) + 20
            chart.draw_diamond(block[1], coordinate_array[-1])
            chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], coordinate_array[-1][1] - radius))
            print(block[0])
            flag = 1

        elif block[0].upper() == "PROCESS":
            print(commands_array.index(block))
            if flag == 1:
                #Decision block has been trigerred and this is yes block
                flag += 1
                coordinate_array.append((base_coordinates[0] - 100, coordinate_array[-1][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_rectangle(block[1], coordinate_array[-1])
                # chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))
                print(block[0])
                print("This is yes block after decision")
                continue
            elif flag == 2:
                flag += 1
                coordinate_array.append((base_coordinates[0] + 100, coordinate_array[-2][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_rectangle(block[1], coordinate_array[-1])
                # chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))
                print(block[0])
                print("This is no block after decision")
                #Decision blcok has been trigerred and this is no block
                pass
            else:
                print(block[0])
                coordinate_array.append((base_coordinates[0], coordinate_array[-1][1] + 100))
                c1 = chart.return_bounding_coor(block[1], coordinate_array[-2])
                c2 = chart.return_bounding_coor(block[1], coordinate_array[-1])
                chart.draw_rectangle(block[1], coordinate_array[-1])
                chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))

        elif block[0].upper() == "LOOP":
            pass

        elif block[0].upper() == "END":
            coordinate_array.append((base_coordinates[0], coordinate_array[-1][1] + 100))
            chart.draw_oval(block[0], coordinate_array[-1])
            c1 = chart.return_bounding_coor(block[0], coordinate_array[-2])
            c2 = chart.return_bounding_coor(block[0], coordinate_array[-1])
            chart.draw_line((coordinate_array[-2][0], c1[3] + 20, coordinate_array[-1][0], c2[1] - 20))
            print(commands_array.index(block))
            print(block[0])

        else:
            print("There is some error in the command file")
            exit()

    chart.save()


if __name__ == "__main__":
    main()
