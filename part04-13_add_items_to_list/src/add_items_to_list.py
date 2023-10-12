# Write your solution here

num = int(input("How many items: "))
i = 1
l = []
while i <= num:
    item = int(input(f"Item {i}: "))
    l.append(item)
    i += 1

print(l)