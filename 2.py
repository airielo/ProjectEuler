#generate Fibonacci list
fibRange=[1,2]
while fibRange[-1]<4000000:
    lastEl=sum(fibRange[-2:])
    fibRange.append(lastEl)
print(fibRange[:-1])

#conditional sum
evens=sum(i for i in fibRange[:-1] if i%2==0)
print(evens)

# 2nd approach for Fibonacci list

res = [1,2]
a=1
b=2
while b <100:
    a, b = b, a+b
    res.append(b)
res
