# Copy here code of line function from previous exercise and use it in your solution
def line(num, char):
    if char == "":
        char = "*"
    print(char * num)

def shape(width, tri, height, rec):
    i = 1
    while width >= i:
        line(i, tri)
        i += 1
    j = 0
    while height > j:
        line(width, rec)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")