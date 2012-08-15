#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

## MAZE GENERATOR ##

Based on Depth-first search algorithm:
http://en.wikipedia.org/wiki/Maze_visit_the_celleration_algorithm#Depth-first_search

  1. Start at a particular cell and call it the "exit."
  2. Mark the current cell as visited, and get a list of its neighbors.
     For each neighbor, starting with a randomly selected neighbor:
       1. If that neighbor hasn't been visited, remove the wall between
          this cell and that neighbor, and then recurse with that neighbor as
          the current cell.

__author__ = "Leonardo Vidarte"


"""

import random


def get_neighbors(cell, maze):
    """
    Get the cells next to the cell

    Example:
      Given the cell a
      The neighbors cells are b

      # # b # #
      # # # # #
      b # a # b
      # # # # #
      # # b # #

    """
    x, y = cell
    neighbors = []
    maze_size = len(maze)

    # Up
    if y - 2 > 0:
        neighbors.append((x, y-2))
    # Down
    if y + 2 < maze_size:
        neighbors.append((x, y+2))
    # Left
    if x - 2 > 0:
        neighbors.append((x-2, y))
    # Right
    if x + 2 < maze_size:
        neighbors.append((x+2, y))

    return neighbors

def remove_the_wall(maze, cell, neighbor):
    """
    Remove the wall between two cells

    Example:
      Given the cells a and b
      The wall between them is w

      # # # # #
      # # # # #
      # a w b #
      # # # # #
      # # # # #

    """
    x0, y0 = cell
    x1, y1 = neighbor
    if x0 == x1:
        x = x0
        y = (y0 + y1) / 2
    if y0 == y1:
        x = (x0 + x1) / 2
        y = y0
    maze[y][x] = 0

def get_start(cell, step, _=[None, None]):
    if step > _[1]:
        _[0] = cell
        _[1] = step
    return (_[0], _[1] * 2)

def visit_the_cell(maze, cell, cells_visited, step):
    x, y = cell
    maze[y][x] = 0 
    cells_visited.append(cell)
    neighbors = get_neighbors(cell, maze)
    random.shuffle(neighbors)
    for neighbor in neighbors:
        if not neighbor in cells_visited:
            remove_the_wall(maze, cell, neighbor)
            visit_the_cell(maze, neighbor, cells_visited, step+1)
    start_cell, min_steps = get_start(cell, step)
    return (maze, start_cell, min_steps)

def create_maze(size=21, exit_cell=(1,1)):
    maze = [[1 for _ in range(size)] for _ in range(size)] # full maze (all 1's)
    maze, start_cell, min_steps = visit_the_cell(maze, exit_cell, cells_visited=[], step=0)
    return (maze, start_cell, min_steps)

def show_maze(maze, exit_cell, start_cell):
    x0, y0 = exit_cell
    maze[y0][x0] = 'X'
    x1, y1 = start_cell
    maze[y1][x1] = '@'
    for row in maze:
        line = ''
        for cell in row:
            if cell == 1:
                line += '# '
            elif cell == 0:
                line += '  '
            else:
                line += str(cell) + ' '
        print line


if __name__ == '__main__':
    maze_size = 21 # Must be odd
    exit_cell = (maze_size-2, maze_size-2)
    maze, start_cell, min_steps = create_maze(maze_size, exit_cell)
    show_maze(maze, exit_cell, start_cell)
    print "Steps from @ to X:", min_steps

