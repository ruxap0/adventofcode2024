def solve(lst):
    n = 1

    if lst[0] < lst[1]:
        while n < len(lst):
            if lst[n - 1] > lst[n] or lst[n] - lst[n - 1] > 3 or lst[n] == lst[n - 1]:
                print("False")
                return False
            else:
                n += 1
    else:
        while n < len(lst):
            if lst[n - 1] < lst[n] or lst[n] - lst[n - 1] < -3 or lst[n] == lst[n - 1]:
                print("False")
                return False
            else:
                n += 1

    return True
    

def dampen(lst):
    if solve(lst):
        return lst
    
    n = 0

    while n < len(lst):
        l = lst.copy()
        l.pop(n)

        if solve(l):
            return l
        n += 1
    
    return lst



# code main
answer = 0
with open('day2/input2.txt') as f:
    lst = []
    for lign in f.readlines():
        lst = lign.strip().split(' ')
        lst = [int(i) for i in lst]
        print(lst)

        lst = dampen(lst)
        answer += int(solve(lst))

print(answer)