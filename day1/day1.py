list1 = []
list2 = []
answer = 0

with open('day1/textfile1.txt') as f:
    for l in f.readlines():
        n1, n2 = l.strip().split('   ')
        list1.append(int(n1))
        list2.append(int(n2))
    
    list1.sort()
    list2.sort()

    while list1:
        answer += abs(list1[0] - list2[0])
    
        list1.pop(0)
        list2.pop(0)

print(answer)