########################################################################################
#   author Clifford Nel   2022
#   script to print cube house
#           5
#          / \
#       3 | x |  4
#       1 -----  2
#########################################################################################

def cube_x(v_cube, dx, st):
    global overflow
    for i in range(0, len(dx)):
        if dx[i] <= overflow:
            continue
        if dx[i] > overflow:
            overflow = ''
        findstr1 = st + dx[i:i + 1]
        findstr2 = dx[i:i + 1] + st
        if (v_cube.find(findstr1) >= 0) or (v_cube.find(findstr2) >= 0):
            print
        else:
            v_cube = v_cube + dx[i]
            return v_cube
    overflow = v_cube[-1]
    v_cube = v_cube[:-1]
    return v_cube


d1 = "234"
d2 = "134"
d3 = "1245"
d4 = "1235"
d5 = "34"
overflow = ""
cube = '12'
cube_count = 0

while True:
    if len(cube) == 0:
        if int(overflow) + 1 >= 5:
            break
        cube = str(int(overflow) + 1)
        overflow = ""
    cube_last_char = cube[-1]
    if cube_last_char == "1":
        cube = cube_x(cube, d1, "1")
    if cube_last_char == "2":
        cube = cube_x(cube, d2, "2")
    if cube_last_char == "3":
        cube = cube_x(cube, d3, '3')
    if cube_last_char == "4":
        cube = cube_x(cube, d4, '4')
    if cube_last_char == "5":
        cube = cube_x(cube, d5, '5')
    if len(cube) == 9:
        cube_count = cube_count + 1
        print(cube + " cube solution = " + str(cube_count))
        overflow = cube[-1]
        cube = cube[:-1]
print('count of the solutions for the house is = '+str(cube_count))
