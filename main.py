import functions as fns

####################################
if __name__ == "__main__":
    print('')
    groupSize = 2
    dataFile = "./data/namelist.csv"
    groupFile = "./data/groups.csv"
    
    print('Reading list of names...', end='')
    names = fns.read_list_from_csv(dataFile)
    print('OK')

    print(f'Randomising the groups of {groupSize}...', end='')
    groups = fns.create_random_groups(names, group_size=groupSize)
    print('OK')

    print(f'Writing results to file...', end='')
    # show_all_groups(groups)
    fns.save_to_csv(groupFile, groups)
    print('OK')
    
    print('Done.\n')
    


        





