fibRange=[1,2]
while fibRange[-1]<100:
    lastEl=sum(fibRange[-2:])
    fibRange.append(lastEl)
print(fibRange[:-1])

