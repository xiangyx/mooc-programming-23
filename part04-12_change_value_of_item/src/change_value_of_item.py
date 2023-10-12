# Write your solution here

l = [1,2,3,4,5]

while True:

    idx = int(input("Index: "))
    if idx == -1: 
        break

    val = int(input("New value: ")) 
    l[idx] = val
    print(l)
