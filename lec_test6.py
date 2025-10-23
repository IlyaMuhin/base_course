kol = int(input())
a = 1
for x in range(1, kol + 1):
    for i in range(1, kol + 1):
        print(i * a, end = ' ')
    print()
    a+=1