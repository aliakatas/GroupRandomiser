import os 
import random

####################################
def read_list_from_csv(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    out = []
    for line in lines:
        content = line.split(',')
        out.append(content[0])
    
    return out

####################################
def create_random_groups(names, group_size=2, allow_less=False):
    n = len(names)
    groups = []

    while n > group_size:
        group = []
        for i in range(group_size):
            name = random.choice(names)
            group.append(name)
            names.remove(name)
        
        groups.append(group)
        n = len(names)
    
    if allow_less:
        groups.append(names)
    else:
        n_rem = len(names)
        for i in range(n_rem):
            group = random.choice(groups)
            group.append(names[i])
    
    return groups

####################################
if __name__ == "__main__":
    print('')
    groupSize = 3
    print('Reading list of names...', end='')
    # Do it
    print('OK')

    print(f'Randomising the groups of {groupSize}...', end='')
    # Do the thing...
    print('OK')

    print(f'Writing results to file...', end='')
    # Do the thing...
    print('OK')
    
    print('Done.\n')
    


        





