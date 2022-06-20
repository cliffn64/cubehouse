########################################################################################
#   author Clifford Nel   .🚲2022
#   script to print cube house
#           5
#           ^
#        3 / \ 4
#         | x |
#        1-----2
#########################################################################################

def build_cube(cube, rule_str):
    global dead_end_char
    test_char = cube[-1]
    for i in range(0, len(rule_str)):
        if len(dead_end_char) != 0:
            if rule_str[i] <= dead_end_char:
                continue
            if rule_str[i] > dead_end_char:
                dead_end_char = ''
        test_chr = rule_str[i:i + 1]
        findstr1 = test_char + test_chr
        findstr2 = findstr1[::-1]
        if (findstr1 not in cube) and (findstr2 not in cube):
            cube = cube + rule_str[i]
            return cube
    dead_end_char = cube[-1]
    cube = cube[:-1]
    return cube


rules = {
    "1":"234",
    "2":"134",
    "3":"1245",
    "4":"1235",
    "5":"34"}
dead_end_char = ""
cube = '1'
cube_count = 0

while True:
    if len(cube) == 0:
        if int(dead_end_char) + 1 >= 5:
            break  # no more possible solutions
        cube = str(int(dead_end_char) + 1)
        dead_end_char = ""
    cube_last_char = cube[-1]
    cube = build_cube(cube, rules[cube_last_char])
    if len(cube) == 9:
        cube_count = cube_count + 1
        print(cube + " cube solution = " + str(cube_count))
        dead_end_char = cube[-1]
        cube = cube[:-1]
print('The count of the solutions for the house is = ' + str(cube_count))
