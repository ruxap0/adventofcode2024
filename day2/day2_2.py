answer = 0

with open('day2/input2.txt') as f:
    list = []
    for lign in f.readlines():
        list = lign.strip().split(' ')
        list = [int(i) for i in list]

        count = 0
        n = 1
        quit = False
        attention = False
        
        if list[0] > list[len(list) - 1]: # La liste est triée dans l'ordre décroissant
            while n < len(list) and quit == False:
                if list[n] > list[n - 1] or list[n] == list[n - 1] or list[n - 1] - list[n] > 3:
                    if(not attention):
                        if list[0] < list[1]:
                            list.pop(1)
                        elif list[len(list) - 2] < list[len(list) - 1]:
                            list.pop(len(list) - 2)
                        else:
                            list.pop(n)
                        attention = True
                        n = 1
                        count = 0
                    else:
                        quit = True
                else:
                    n += 1
                    count += 1
        else: # La liste est triée dans l'ordre croissant
            while n < len(list) and quit == False:
                if list[n] < list[n - 1] or list[n] == list[n - 1] or list[n] - list[n - 1] > 4:
                    if(not attention):
                        if(list[0] > list[1]):
                            list.pop(1)
                        elif list[len(list) - 2] > list[len(list) - 1]:
                            list.pop(len(list) - 2)
                        else:
                            list.pop(n)
                        attention = True
                        n = 1
                        count = 0
                    else:
                        quit = True
                else:
                    n += 1
                    count += 1

        if count == len(list) - 1:
            answer += 1

print(answer)
                