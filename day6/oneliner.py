for a in [4,14]: print((lambda a: min([x for x in range(a-1, len(str(open("day6/input.txt", "r").read()).strip())) if len(set(str(open("day6/input.txt", "r").read()).strip()[x-a:x])) == a])) (a))
