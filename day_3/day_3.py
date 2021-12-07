# %%
from pathlib import Path
# %%
path = "input.txt"
with open(path) as f:
    contents = f.read()
input = contents.splitlines()
input = [int(i) for i in input]
# %%
