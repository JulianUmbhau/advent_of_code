# %%
from pathlib import Path
# %%
__file__

path = "input.txt"
with open(path) as f:
    contents = f.read()
input = contents.splitlines()
input = [i for i in input]

# %%
