# Write your solution here
while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        break

    if editor in {"notepad", "word"}:
        print("awful")
    else:
        print("not good")

print("an excellent choice!")