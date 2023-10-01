# Write your solution here
def same_chars(str, idx1, idx2):
    if max(idx1, idx2) >= len(str):
        return False
    return str[idx1] == str[idx2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))