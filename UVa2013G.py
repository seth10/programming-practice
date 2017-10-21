import sys
n, d = map(int, sys.stdin.readline()[:-1].split(" "))
room = [line[:-1] for line in sys.stdin]

maxBattery = d
battery = d
steps = 0
#             right  down   left    up
directions = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0

# find 'r' to set x (column from left) and y (row from top)
for i, row in enumerate(room):
    if 'r' in row:
        y = i
x = room[y].index('r')
#print y, x

# replace 'r' with '-'
row = list(room[y])
row[x] = '-'
room[y] = ''.join(row)
#for row in room: print row

while battery > 0 and steps <= 100000:
    target = room[y+directions[d][0]][x+directions[d][1]]
    #print y, x, d, target, steps, battery
    if target == 'm':
        print steps+1
        break
    elif target == 'x':
        d += 1
        d %= 4
        steps += 1
        battery -= 1
    elif target == '-':
        y += directions[d][0]
        x += directions[d][1]
        steps += 1
        battery -= 1
    if 'p' in [ room[y][x+1], room[y+1][x], room[y][x-1], room[y-1][x] ]:
        steps += (maxBattery - battery)
        battery = maxBattery
else:
    print "NEVER"

'''
10 30
xxxxxxxxxx
x-x------x
x--------x
xr-xx----x
x--xx----p
xm-------x
xx------xx
xxxx-----x
x--------x
xxxxxxxxxx
'''
