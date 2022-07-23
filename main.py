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
    pass

if __name__ == "__main__":
    main()
