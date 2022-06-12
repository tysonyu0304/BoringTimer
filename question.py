import random

x, y, c, count = 0, 0, 0, 0
choose = 'r'

def control(a, b):
    r = random.randint(1,2)
    if r == 1: return a
    else: return b

def move_x(c):
    global x
    x = x + random.randint(1,10) * c

def move_y(c):
    global y
    y = y + random.randint(1,10) * c

list_n = []

for i in range(random.randint(1,20)):
    if choose == 'r': 
        move_x(1)
        choose = control('u','d')
        if choose == 'u': c = 0
        else: c = 1
    elif choose == 'l': 
        move_x(-1)
        choose = control('u','d')
        if choose == 'u': c = 1
        else: c = 0
    elif choose == 'u': 
        move_y(1)
        choose = control('r','l')
        if choose == 'r': c = 0
        else: c = 1
    elif choose == 'd': 
        move_y(-1)
        choose = control('r','l')
        if choose == 'r': c = 1
        else: c = 0
    count += 1
    out = [x, y, c]
    list_n.append(out)

print(count)
print(list_n)
