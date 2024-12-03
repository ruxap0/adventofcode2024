import re

answer = 0

with open("day3/input3.txt") as f:
    mem = f.read()

    lst = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", mem)

    for op in lst:
        n1, n2 = op.replace("mul(", "").replace(")", "").split(',')
        answer += int(n1) * int(n2)
    


print(answer)
        
