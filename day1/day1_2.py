list1 = []
list2 = []
answer = 0

with open('day1/textfile1.txt') as f:
    for l in f.readlines():
        n1, n2 = l.strip().split('   ')
        list1.append(int(n1))
        list2.append(int(n2))

    for number in list1:
        count = list2.count(number)
        answer += count * number
        

print(answer)