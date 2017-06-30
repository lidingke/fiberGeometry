from __future__ import division
num = 0
for a in range(101):
    for b in range((101-a)//2):
        for c in range((101-a-2*b)//5):
            for d in range((101-a-2*b-5*c)//10):
                if (a+2*b+5*c+10*d) == 100:
                    num = num + 1

print(num)
