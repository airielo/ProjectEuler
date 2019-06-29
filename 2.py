fibRange=[1,2]
while fibRange[-1]<4000000:
    lastEl=sum(fibRange[-2:])
    fibRange.append(lastEl)
print(fibRange[:-1])
evens=sum(i for i in fibRange[:-1] if i%2==0)
print(evens)
