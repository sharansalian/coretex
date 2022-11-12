# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def max_sum():
    for i in range(0, 6):
        print("i =", i)
        for j in range(i, 6):
            print("j = ", j)


def directions():
    return [[1, 0], [-1, 0], [0, 1], [0, -1]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for dr, dc in directions():
        print("dr =", dr, dc)
    print(directions())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
