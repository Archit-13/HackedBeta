'''
- Need to find the occureance of the place
- If the place occurrence is periodically then predict the next occurance
- add all the occurance of the same place
'''

name = ""
lines = open(name, "r+")
lines = readlines(lines)
list = {}
for line in lines:
    line_splitted = line.split()
    #this could be changed
    if line_splitted[3] in list:
        table.append(line_splitted[1])

    else:
        list[line.splitted[3]] = [1, line_splitted[1], line_splitted[2]]


