# Write your solution here
def greatest_number(a, b, c):
    max_ab = max(a, b)
    # if max_ab >= c:
    #     return max_ab
    # return c
    return max(max_ab, c)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)