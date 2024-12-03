import re

answer = 0
do = True

with open("day3/input3.txt") as f:
    mem = f.read()

    lst = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", mem)

    print(lst)
    for op in lst:
        if op == "do()":
            do = True
        elif op == "don't()":
            do = False
        else:
            n1, n2 = op.replace("mul(", "").replace(")", "").split(',')
            if do:
                answer += int(n1) * int(n2)
    


print(answer)
        