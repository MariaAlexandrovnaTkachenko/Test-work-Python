Array = []
m = map(int, input().split())
for i in m:
    Array.append(i)
for j in Array:
    if j % 3 == 0:
        print(j, end=' ')
