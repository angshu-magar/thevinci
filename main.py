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
    coordinate_arrray = list() #list to store every block coordinates
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
            coordinate_arrray.append((img_size[0] / 2, 0.05 * img_size[1]))
            chart.draw_oval("START", coordinate_arrray[0])

        elif block[0].upper() == "IO":
            print(commands_array.index(block))
            if flag == 1:
                #Decision block has been trigerred and this is yes block
                flag +=1
                print(block[0])
                print("This is yes block after decision")
                continue
            elif flag == 2:
                flag += 1
                print(block[0])
                print("This is no block after decision")
                #Decision blcok has been trigerred and this is no block
            else:
                print(block[0])
                pass

        elif block[0].upper() == "DECIDE":
            print(commands_array.index(block))
            print(block[0])
            flag = 1

        elif block[0].upper() == "PROCESS":
            print(commands_array.index(block))
            if flag == 1:
                #Decision block has been trigerred and this is yes block
                flag += 1
                print(block[0])
                print("This is yes block after decision")
                continue
            elif flag == 2:
                flag += 1
                print(block[0])
                print("This is no block after decision")
                #Decision blcok has been trigerred and this is no block
                pass
            else:
                print(block[0])

        elif block[0].upper() == "LOOP":
            pass

        elif block[0].upper() == "END":
            print(commands_array.index(block))
            print(block[0])

        else:
            print("There is some error in the command file")
            exit()

    chart.save()


if __name__ == "__main__":
    main()
