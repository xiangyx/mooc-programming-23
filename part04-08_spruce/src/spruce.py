# Write your solution here
def spruce(height):
    print("a spruce!")
    i = 1
    while height >= i:
        print(" " * (height - i), end = "")
        print("*" * (2 * i - 1))
        i += 1
    print(" " * (height-1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)