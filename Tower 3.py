import random

def disk(name = 'you', name2 = 'friend', floor = 0, floor2 = 0):  # name: name of player, floor: floor of player, 2 : other player
    disk = random.randint(1, 6)
    floor = floor + disk
    print(f'Disk Says {disk}. {name} have to move floor No. {floor}')

    if floor % 5 == 0 and floor < 100: # check whether goto snake area
        print(f'Oh There are Snakes in floor No. {floor}. {name} can not move there.')
        floor = floor - disk

    floors = check(floor,disk,name)    
    print(f'\n\t{name} in floor No. {floors} \n\t{name2} in floor No. {floor2}')

    return floors

def disk_bonus(name = 'you', name2 = 'friend', floor = 0, floor2 = 0): # come here for bonus turn
    disk = random.randint(1, 6)
    floor = floor + disk
    print(f'Disk Says {disk}. {name} have to move floor No. {floor}')
    
    floors = check(floor,disk,name)
    print(f'\n\t{name} in floor No. {floors} \n\t{name2} in floor No. {floor2}')
    
    return floors

def check(floor,disk,name): # check winner
    if floor < 100:
        return floor
    elif floor == 100:
        print (f'\n{name.upper()} IS IN FLOOR NO. {floor}. {name.upper()} WON THE GAME')
        exit()
    else:
        print(f'There is no floor No. {floor}. So {name} have to wait in {floor - disk} floor')
        floor = floor - disk
        return floor
    
p2 = input('Welcome to the Game. Enter your friend\'s name : ')
if p2 =='': p2 = 'friend'

p1_floor = 0
p2_floor = 0
day = 0

while (day < 100 or p1_floor < 100 or p2_floor < 100):
    day += 1 
    print(f'\nday {day} Started')
    if p2_floor % 9 != 0 or p2_floor == 0:  # player 1 normal play
        input('Press Enter to take your chance')
        p1_floor = disk('you',p2,p1_floor,p2_floor)
    else:   # player 1 bonus chance
        print(f'{p2} is in Ladie\'s floor. You Have 2 chances')
        input('Press Enter to take your Bonus chance')
        p1_floor = disk_bonus('you',p2,p1_floor,p2_floor)
        day += 1
        print(f'\nday {day} Started')
        input('Press Enter to take your next chance')
        p1_floor = disk('you',p2,p1_floor,p2_floor)
    
    day += 1
    print(f'\nday {day} Started')   # player 2 normal play
    if p1_floor % 9 != 0 or p1_floor == 0:
        input(f'Press Enter to give {p2} chance')
        p2_floor = disk(p2,'you',p2_floor,p1_floor)
    else:   # player 2 bonus play
        print(f'You are in Ladie\'s floor. {p2} Have 2 chances')
        input(f'Press Enter to give {p2} Bonus chance')
        p2_floor = disk(p2,'you',p2_floor,p1_floor)
        day += 1
        print(f'\nday {day} Started')
        input(f'Press Enter to give {p2} next chance')
        p2_floor = disk(p2,'you',p2_floor,p1_floor)

if day > 100:
    print ('TIME IS OVER, YOU BOTH CAN GO HOME')