"""ADS_CSCSE01/maze.py
Lab-1: 

1.3. Write the code for the Maze problems. Show the input and output in the Graphical Form. 
Also show the intermediate stages in the output so that the working of the algorithm is clear.
"""

import numpy as np

from matplotlib import pyplot as plt
from typing import List, Tuple

def solve_maze(maze: List[List[int]]) -> List[Tuple[int]]:

    rows = len(maze)
    cols = len(maze[0])
    start = (0, 0)                      # start of the stack
    end = (rows - 1, cols - 1)          # end of the stack

    stack = [start]
    visited = set()

    while stack:
        current = stack[-1]
        if current == end:
            break

        neighbors = get_neighbors(current, maze)

        if unvisited_neighbors := [n for n in neighbors if n not in visited]:
            next_cell = unvisited_neighbors[0]
            stack.append(next_cell)
            visited.add(next_cell)

        else:
            stack.pop()

    return stack


def get_neighbors(cell: int, maze: List[List[int]]) -> List[Tuple[int]]:
    row, col = cell
    neighbors = []

    # Defining the possible moves (up, down, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == '0':
            neighbors.append((new_row, new_col))

    return neighbors


def visualize_maze_step_by_step(maze: List[List[int]], solution_path: List[Tuple[int]]) -> None:

    for row in maze:
        print(" ". join(row))
    print()

    for step, (row, col) in enumerate(solution_path):
        maze[row][col] = f'{step}'
        for r in maze:
            print(" ". join(r))
        print()


def visualize_maze(maze: List[List[int]], solution_path: List[Tuple[int]]) -> None:
    maze = np.array(maze, dtype=int)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(maze, cmap='binary')

    for step, (row, col) in enumerate(solution_path):
        maze[row, col] = 2                              # Marking the path with different value
        ax.imshow(maze, cmap='binary', alpha=0.3)
        plt.pause(1)

    plt.show()


if __name__ == '__main__':
    maze =[
        ['0', '1', '0', '0', '0'],
        ['0', '1', '0', '1', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0']
    ]

    solution_path = solve_maze(maze)
    print("Solution Path: ", solution_path)
    visualize_maze_step_by_step(maze, solution_path)
    visualize_maze(maze, solution_path)
