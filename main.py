import sys, shape

def process_commands(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        processed_commands = list()
        for line in contents:
            line = line.split(":")
            line = [l for l in line if l!="\n"]
            if len(line) != 2:
                processed_commands.append((line[0],))
            else:
                processed_commands.append((line[0], line[1].strip()))
    return processed_commands

def main():

    #testing
    #image was too low res
    img_size = (794, 1123)
    temp = ShapeDrawer("flowchart.png", img_size)
    temp.draw_oval("START", (img_size[0] / 2, 0.05 * img_size[1]))
    temp.draw_rectangle("a, b", (img_size[0] / 2, 0.15 * img_size[1]))
    temp.draw_parallelogram("INPUT a", (img_size[0] / 2, 0.25 * img_size[1]))
    temp.draw_diamond("IF a > 0", (img_size[0] / 2, 0.35 * img_size[1]))
    temp.save()

    pass

if __name__ == "__main__":
    main()
