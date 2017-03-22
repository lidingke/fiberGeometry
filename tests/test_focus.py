import time
import random
from collections import deque

def mode(x):
    if x<0:
        return 100.0
    elif x<50:
        return 100.0-2*x
    elif x<55:
        return 0.0
    elif x<105:
        return 2*x-110.0
    else:
        return 100.0

def forward(distance, back):
    if back:
        distance = distance + 0.5
    else :
        distance = distance - 0.5
    return distance

def test_focus():
    RUNNING = True
    oldsharp = deque(maxlen=5)
    distance = random.randint(0,100)
    back = True
    while RUNNING:
        time.sleep(1)
        oldsharp.append(mode(distance))
        print oldsharp
        if len(oldsharp) > 2:
            if oldsharp[-2] >= oldsharp[-1]:
                distance = forward(distance, back)
            else:
                distance = forward(distance, back)
                back = not back

            print distance, oldsharp[-2], oldsharp[-1]

            if len(oldsharp) == 5:
                istrue = (oldsharp[4] >= oldsharp[2]) and (oldsharp[0] >= oldsharp[2])
                if istrue:
                    RUNNING = False



