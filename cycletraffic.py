from itertools import cycle
import time

lights = [
    ('Green',3),
    ('Yellow',0.5),
    ('Red',3)
]

colors = cycle(lights)

while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)
