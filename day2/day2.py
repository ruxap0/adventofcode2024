def solve(lst):
    n = 1
    count = 0

    if lst[0] < lst[1]:
        while n < len(lst):
            if lst[n - 1] > lst[n] or lst[n] - lst[n - 1] > 3 or lst[n] == lst[n - 1]:
                print("False")
                return False
            else:
                n += 1
                count += 1
    else:
        while n < len(lst):
            if lst[n - 1] < lst[n] or lst[n] - lst[n - 1] < -3 or lst[n] == lst[n - 1]:
                print("False")
                return False
            else:
                n += 1
                count += 1
        
    if count == len(lst) - 1:
        print("True")
        return True



answer = 0
with open('day2/input2.txt') as f:
    lst = []
    for lign in f.readlines():
        lst = lign.strip().split(' ')
        lst = [int(i) for i in lst]
        print(lst)

        answer += int(solve(lst))

print(answer)