# This is a sample Python script.
import collections


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    queue = collections.deque()
    queue.append((0, 0))

    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (min(row, col) < 0
                        or row == ROWS
                        or col == COLS
                        or (row, col) in visit
                        or grid[row][col] == 1):
                    continue

                visit.add((row, col))
                queue.append((row, col))
        length += 1


# Press the green button in the gutter to run the script.
# Find the shortest path from top left to bottom righ point

if __name__ == '__main__':
    grid = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]

    print(bfs(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
