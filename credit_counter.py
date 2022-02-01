

def credit_counter(role_names):

    global count1
    count1 = 0
    global count2
    count2 = 0
    global count3
    count3 = 0
    global count4
    count4 = 0
    global count5
    count5 = 0
    global count6
    count6 = 0

    other_medal_2 = 'other medal 2'
    other_medal_1 = 'other medal 1'
    level_1000 = 'level 1000'
    level_750 = 'level 750'
    level_500 = 'level 500'
    level_250 = 'level 250'


    if any(ext in other_medal_2 for ext in role_names):
        print(other_medal_2)
        count1 = 60000
    if any(ext in other_medal_1 for ext in role_names):
        print(other_medal_1)
        count2 = 50000
    if any(ext in level_1000 for ext in role_names):
        print(level_1000)
        count3 = 4000
    if any(ext in level_750 for ext in role_names):
        print(level_750)
        count4 = 3000
    if any(ext in level_500 for ext in role_names):
        print(level_500)
        count5 = 2000
    if any(ext in level_250 for ext in role_names):
        print(level_250)
        count6 = 1000

    total = count1 + count2 + count3 + count4 + count5 + count6

    return total