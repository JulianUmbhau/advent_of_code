# %%
from pathlib import Path
# %%
path = "input.txt"
with open(path) as f:
    contents = f.read()
input = contents.splitlines()
input = [i for i in input]

# %%
def part_one(input):
    gamma = dict()
    epsilon = dict()
    for l in range(len(input[1])):

        bit_size = 0

        for bit in input:
            bit_size = bit_size + int(bit[l])
        
        if bit_size > 500:
            gamma[l] = 1
            epsilon[l] = 0
        else:
            gamma[l] = 0
            epsilon[l] = 1

    gamma_final = list(gamma.values())
    gamma_final_bin = ''.join(map(str, gamma_final))
    gamma_value = int(gamma_final_bin, 2)

    epsilon_final = list(epsilon.values())
    epsilon_final_bin = ''.join(map(str, epsilon_final))
    epsilon_value = int(epsilon_final_bin, 2)

    return gamma_value * epsilon_value
 
part_one(input)

# %%
def find_most_prevalent_bit(input, loc, task):
    if len(input) == 1:
        return(input)
    
    count = 0
    for i in input:
        if int(i[loc]) == 1:
            count += 1
    
    print(count)

    keepers = []
    def append_rows(input, loc, task):
        if task == "oxygen":
            for i in input:
                diff = len(input)/2
                if count >= diff and int(i[loc]) == 1:
                    keepers.append(i)
                elif count < diff and int(i[loc]) == 0:
                    keepers.append(i)
        elif task == "CO2":
            for i in input:
                diff = len(input)/2
                if count >= diff and int(i[loc]) == 0:
                    keepers.append(i)
                elif count < diff and int(i[loc]) == 1:
                    keepers.append(i)
        return keepers
       
    keepers = append_rows(input, loc, task)
        
    return keepers

input_filtered = input
for j in range(len(input[0])):
    input_filtered = find_most_prevalent_bit(input_filtered, j, "oxygen")

test = ''.join(map(str, input_filtered))
oxygen = int(test, 2)

input_filtered = input
for j in range(len(input[0])):
    input_filtered = find_most_prevalent_bit(input_filtered, j, "CO2")

test = ''.join(map(str, input_filtered))
Co2 = int(test, 2)



# %%
oxygen * Co2
# %%
