# Write your solution here
l = []
while True:
    print(f"The list is now {l}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "d":
        if len(l) == 0:
            l.append(1)
        else:
            l.append(l[-1] + 1)
    if action == "r":
        l.pop()
    if action == "x":
        print("Bye!")
        break