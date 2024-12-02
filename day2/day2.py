answer = 0

with open('day2/input2.txt') as f:
    list = []
    for lign in f.readlines():
        count = 0
        quit = False
        list = lign.strip().split(' ')
        list = [int(i) for i in list]
        print(list)

        n = 1

        if(list[0] < list[1]):
            while(n < len(list) and not quit):
                if(list[n - 1] > list[n] or list[n] - list[n - 1] >= 4 or list[n] - list[n - 1] == 0):
                    print("False")
                    quit = True
                else:
                    n += 1
                    count += 1
        else:
            while(n < len(list) and not quit):
                if(list[n - 1] < list[n] or list[n] - list[n - 1] < - 3) or list[n] - list[n - 1] == 0:
                    print("False")
                    quit = True
                else:
                    n += 1
                    count += 1
        
        if(count == len(list) - 1):
            print("True")
            answer += 1

print(answer)
