data = str(open("day6/input.txt", "r").read()).strip()

def test(data, q):
    for x in range(q-1, len(data)):
        if len(set(data[x-q:x])) == q:
            return x

print(f"Part one: {test(data, 4)}\nPart two: {test(data, 14)}")
