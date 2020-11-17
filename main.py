import os 
import random

####################################
def read_list_from_csv(fname, start=1):
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    print(lines[start:])
    out = []
    for line in lines[start:]:
        content = line.split(',')
        out.append(content[0].strip())
    
    return out

####################################
def create_random_groups(names, group_size=2, allow_less=False):
    n = len(names)
    groups = []

    while n >= group_size:
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
def show_one_group(group, id):
    print(f'Group {id}')
    print('------------')
    for item in group:
        print(f'{item} ', end='')
    print('')

####################################
def show_all_groups(groups):
    print('+++++++++++++++++++++++++++++++++')
    for i, group in zip(range(len(groups)), groups):
        show_one_group(group, i)
    print('_________________________________')

####################################
def save_to_csv(fname, groups):
    n = len(groups)
    with open(fname, 'w') as w:
        for i, group in zip(range(n), groups):
            names = ', '.join(group)
            w.write(f'Group {i + 1}, {names} \n')

####################################
if __name__ == "__main__":
    print('')
    groupSize = 2
    dataFile = "./data/namelist.csv"
    groupFile = "./data/groups.csv"
    
    print('Reading list of names...', end='')
    names = read_list_from_csv(dataFile)
    print('OK')

    print(f'Randomising the groups of {groupSize}...', end='')
    groups = create_random_groups(names, group_size=groupSize)
    print('OK')

    print(f'Writing results to file...', end='')
    # show_all_groups(groups)
    save_to_csv(groupFile, groups)
    print('OK')
    
    print('Done.\n')
    


        





