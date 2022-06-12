IN = int(input())

num_list = []
x, y, c, count = 0, 0, 0, -1
f = 'r'
end = False

for i in range(IN):
    num_list.append(list(map(int, input().split()))) 

def run_r():
    global end, x, c, count
    count += 1
    temp_x = []
    temp_c = {}
    for i in num_list:
        if i[1] == y and i[0] > x: 
            temp_x.append(i[0])
            temp_c[i[0]] = (i[2])
    if len(temp_x) == 0:
        end = True
    else: 
        temp_x.sort()
        x = temp_x[0]
        c = temp_c[x]

def run_l():
    global end, x, c, count
    count += 1
    temp_x = []
    temp_c = {}
    for i in num_list:
        if i[1] == y and i[0] < x: 
            temp_x.append(i[0])
            temp_c[i[0]] = (i[2])
    if len(temp_x) == 0:
        end = True
    else: 
        temp_x.sort()
        x = temp_x[-1]
        c = temp_c[x]

def run_u():
    global end, y, c, count
    count += 1
    temp_y = []
    temp_c = {}
    for i in num_list:
        if i[0] == x and i[1] > y: 
            temp_y.append(i[1])
            temp_c[i[1]] = (i[2])
    if len(temp_y) == 0:
        end = True
    else: 
        temp_y.sort()
        y = temp_y[0]
        c = temp_c[y]

def run_d():
    global end, y, c, count
    count += 1
    temp_y = []
    temp_c = {}
    for i in num_list:
        if i[0] == x and i[1
        ] < y: 
            temp_y.append(i[1])
            temp_c[i[1]] = (i[2])
    if len(temp_y) == 0:
        end = True
    else: 
        temp_y.sort()
        y = temp_y[-1]
        c = temp_c[y]

while end == False:
    if f == 'r': run_r()
    elif f == 'l': run_l()
    elif f == 'u': run_u()
    elif f == 'd': run_d()
    
    if c == 0:
        if f == 'r': f = 'u'
        elif f == 'l': f = 'd'
        elif f == 'u': f = 'r'
        elif f == 'd': f = 'l'
    elif c == 1:
        if f == 'r': f = 'd'
        elif f == 'l': f = 'u'
        elif f == 'u': f = 'l'
        elif f == 'd': f = 'r'

print(count)