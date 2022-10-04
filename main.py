import re

rs = "1"
with open('data', 'r') as file:
    data = [ float(i) for i in file.read().split('\n') if i != '']
    for i in range(1, len(data)):
        if data[i] >= data[i-1]:
            rs += "1"
        else:
            rs += "0"

#print(rs)

total_0 = 0
total_1 = 0

for i in range(3,11):
    tc = rs.count(rs[-1*i:])
    tc_0 = rs.count(rs[-1*i:]+'0')
    tc_1 = rs.count(rs[-1*i:]+'1')
    print("Prev.", i , "days (",rs[-1*i:], ") pattern is present ", tc, "times\n\t 0 : ",tc_0, "times \n\t 1 : ", tc_1, "times" )
    total_0 += tc_0
    total_1 += tc_1


print(f'\n\nTotal next BULL : {total_1}\nTotal next BEER {total_0}')

if total_0 > total_1:
    print("\n\nTomorrow prediction : BEER")
else:
    print("\n\nTomorrow prediction : BULL")
