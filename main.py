import sys
from shape import *

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
    h = ShapeDrawer("hello.png")
    h.draw_oval()
    return 0

main()
