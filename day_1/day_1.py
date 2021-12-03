# %%
from pathlib import Path
# %%
path = "input.txt"
with open(path) as f:
    contents = f.read()
input = contents.splitlines()
input = [int(i) for i in input]
# %%
counter = []
previous = input[0]
for i in input:
    if i > previous:
        counter.append(True)
    else:
        counter.append(False)
    previous = i
sum(counter)
# %%
def part_1() -> int:
    with open(Path(__file__).parent / "input.txt") as file:  # noqa: F841
        previous = int(file.readline())

        increases = 0
        for value in map(int, file):
            increases += value > previous
            previous = value
        return increases

part_1()

# %%
def part_2(input) -> int:
    counter = 0
    previous=sum(input[0:3])
    for i in range(0, len(input)):
        total = sum(input[i:i+3])
        if total > previous:
            counter += 1
        previous = total
    
    return(counter)

part_2(input)

# %%
