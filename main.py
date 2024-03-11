import random

def generate_lists(n, m, c):
    with open("lists.txt", "w") as f:
        for i in range(n):
            new_list = [random.choice(c) for j in range(m)]

            f.write(" ".join(map(str, new_list)) + "\n")
            print(f"List {i+1} generated and added to lists.txt")

if __name__ == "__main__":
    n = int(input("Enter the number of lists: "))
    m = int(input("Enter the number of elements per list: "))
    p = int(input("Enter the range of elements: "))
    c = list(range(1, p+1))
    generate_lists(n, m, c)
