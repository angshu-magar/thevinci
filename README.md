# thevinci
> Creates flowchart from pseudocode

## Dependencies
* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/download/releases/3.0/)
* [pip](https://pypi.org/project/pip/)

## Getting Started
```
# Clone this repo
git clone https://github.com/angshu-magar/thevinci
cd thevinci

# Install requirements
pip install -r requirements.txt

# Running the code
python3 main.py commands.txt

#Output
flowchart.png
```

### Output
```
START:
IO: Print this is program to print numbers that can divide the input number
PROCESS: a = 0
IO: Input num
PROCESS: a = a + 1
DECIDE: Is num % a == 0
IO: Print a
IO: Do nothing
PROCESS: connector
LOOP: Is a >= num: no_5
END:
```
![alt text](https://github.com/angshu-magar/thevinci/blob/main/flowchart.png)

## How to make your own flowchart

You can make your own flowchart by writing a pseudocode in a text file and passing the text file as an argument into main.py.

For eg: `python3 main.py your_file.txt`

## Syntax

### 1. Start/End(Oval):
```
START:
END:
```
Creates two ovals with `START` and `END` text inside them.

![alt text](https://github.com/angshu-magar/thevinci/blob/main/examples/start%26end.png)

### 2. Input/Output(Parallelogram):
```
IO: x = 0
IO: Input a
IO: Input b
```
Creates three parallelograms with `x = 0`, `Input a` and `Input b` text inside them.

![alt text](https://github.com/angshu-magar/thevinci/blob/main/examples/io.png)

### 3. Process(Rectangle):
```
PROCESS: x = x + 1
PROCESS: rem = a % b
```
Creates two rectangles with `x = x + 1` and `rem = a % b` text inside them.

![alt text](https://github.com/angshu-magar/thevinci/blob/main/examples/process.png)

### 4. Decision(Diamond):
```
DECIDE: If a > b
IO: a is greater
IO: b is greater
```
Creates a diamond with `If a > b` text inside it and points an arrow as *yes* to next block and *no* points an arrow to the block after that.

![alt text](https://github.com/angshu-magar/thevinci/blob/main/examples/decision.png)

### 5. Loop(Diamond that goes to a previous block when a condition is met):
```
LOOP: If b > a: yes_3
```
Creates a diamond with `If b > a` text inside it and if the condition is *yes* the goes to block 3 and *no* goes to the next block

![alt text](https://github.com/angshu-magar/thevinci/blob/main/examples/loop.png)

## Limitation

* Cannot create more than two branches from a block.
* Cannot enter multiline text.
* Cannot create complex branching.
