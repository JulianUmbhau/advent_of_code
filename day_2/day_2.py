# %%
import pandas as pd
from pathlib import Path
# %%
path = "input.txt"
with open(path) as f:
    contents = f.read()
input = contents.splitlines()

input = [i.split(" ") for i in input]
# %%
direction = []
value = []

for i,x in input:
    direction.append(i)
    value.append(int(x))

df = pd.DataFrame({'direction':direction, 'value':value})

# %%
def day_2_task_1(df):
    forward_value = df.loc[df['direction'] == "forward",['value']].sum(axis=0)
    up_value = df.loc[df["direction"] == "up", ["value"]].sum(axis=0)
    down_value = df.loc[df["direction"] == "down", ["value"]].sum(axis=0)
    depth = down_value - up_value

    return(depth * forward_value)

day_2_task_1(df)

# %%
def day_2_task_2(df):
    aim = 0
    horizontal = 0
    depth = 0
    for i in range(len(df)):
        direction = df["direction"].loc[i]
        value = df["value"].loc[i]
        if direction == "forward":
            horizontal = horizontal + value
            depth = (aim * value) + depth
        elif direction == "up":
            aim = aim - value
        elif direction == "down":
            aim = aim + value
    return(depth * horizontal)

day_2_task_2(df)

# %%
